import torch
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast, GPT2Config
from torch.utils.data import DataLoader, Dataset

tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
    bos_token='</s>', eos_token='</s>', unk_token='<unk>',
    pad_token='<pad>', mask_token='<mask>')

F_model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
F_model.load_state_dict(torch.load("tuned_33_F.pth", map_location=torch.device('cpu')))

class QADataset(Dataset):
    def __init__(self, questions, answers=None):
        self.questions = questions
        self.answers = answers

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, idx):
        question = self.questions[idx]
        # answer = self.answers[idx]

        # 질문과 답변을 결합하여 입력값과 라벨로 만듦
        input_text = f"{question} {tokenizer.eos_token}"
        inputs = tokenizer(input_text, truncation=True,
                                return_tensors="pt")
        labels = inputs.input_ids.clone()
        labels[labels == tokenizer.pad_token_id] = -100

        # 토큰화된 입력 데이터를 리스트 형태로 반환
        return {"input_ids": inputs.input_ids[0],
                "attention_mask": inputs.attention_mask[0],
                "labels": labels[0]}

def test_F_model(test_dataset, batch_size=32):
    F_model.eval()

    test_dataloader = DataLoader(test_dataset, batch_size=batch_size)

    all_predictions = []

    with torch.no_grad():
        for batch in test_dataloader:
            # 토크나이저를 사용하여 입력 데이터를 토큰화
            inputs = {k: v for k, v in batch.items()}  # 수정된 부분
            outputs = F_model.generate(
                input_ids=inputs['input_ids'],
                attention_mask=inputs['attention_mask'],  # 텍스트가 길 수 있으므로 적절한 max_length 설정
                pad_token_id=tokenizer.pad_token_id,
                # bos_token_id=tokenizer.bos_token_id,
                eos_token_id=tokenizer.eos_token_id,
                # num_beams=4,  # Beam Search 크기
                num_beams=1,
                early_stopping=False  # 최대 길이에 도달하면 멈춤
            )
            print('outputs', outputs)
    # tokenized_outputs = [tokenizer.tokenize(output, skip_special_tokens=True) for output in outputs]
    # print(tokenized_outputs)
    all_predictions.extend(outputs.tolist())
    all_predictions_str = [str(pred) for pred in all_predictions[0]]
    prediction_str = ' '.join(all_predictions_str)
    input_str = [str(pred) for pred in inputs['input_ids'].tolist()[0]]
    input_str = ' '.join(input_str)

    if input_str in prediction_str:
        prediction_str = prediction_str.replace(input_str, '')
    all_predictions_str = prediction_str.split()
    all_predictions = [int(i) for i in all_predictions_str if i]
    print('changed_all_predictions: ', [all_predictions])
    # 예측 결과를 텍스트로 디코딩하여 반환

    decoded_predictions = [tokenizer.decode(prediction, skip_special_tokens=True) for prediction in [all_predictions]]

    return decoded_predictions

while True:
    data = input('문장을 입력하세요: ')
    if data == "종료":
        break
    test_dataset = QADataset([data])
    predictions = test_F_model(test_dataset)
    print(f'질문: {data}')

    prediction_indexes = []
    specials = ['.', '!', '?']
    predictions_str = ' '.join(predictions)
    for i in range(len(predictions_str)):
        if (predictions_str[i] in specials) and (i != len(predictions_str) -1) and (predictions_str[i+1] not in specials):
            # print(i)
            # print('predictions_str[i]: ', predictions_str[i])
            prediction_indexes.append(i)

    print(f'len(prediction_indexes): {len(prediction_indexes)}')
    print(f'prediction_indexes: {prediction_indexes}')
    total_predictions = []
    if len(prediction_indexes) == 1:
        total_predictions.append(predictions_str[:prediction_indexes[0] + 1])
        total_predictions.append(predictions_str[prediction_indexes[0] + 1:])
    elif len(prediction_indexes) > 1:
        modified_prediction_indexes = [num + 1 for num in prediction_indexes]
        modified_prediction_indexes.insert(0, 0)
        modified_prediction_indexes.append(-1)
        print(f'changed prediction_indexes: {modified_prediction_indexes}')
        pairs = []
        for i in range(len(modified_prediction_indexes) - 1):
            pairs.append((modified_prediction_indexes[i], modified_prediction_indexes[i + 1]))
        
        for j in range(len(pairs)):
            total_predictions.append(predictions_str[pairs[j][0]:pairs[j][1]])
    else:
        total_predictions = predictions

    print(f"답변: {total_predictions}")
