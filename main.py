from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from model_T import QADataset, test_T_model
from model_F import QADataset,test_F_model
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# CSV 파일 로드
csv_file_path = "1852 F.csv"
df = pd.read_csv(csv_file_path, encoding='cp949')

# 질문과 답변 컬럼 추출
questions = df['Speaker_1'].tolist()
answers = df['Speaker_2'].tolist()

qa_dict = dict(zip(questions, answers))

app = FastAPI()

templates = Jinja2Templates(directory='./')
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/css", StaticFiles(directory='css'), name='css')
app.mount("/img", StaticFiles(directory='img'), name='img')


origins = [
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('index.html', context={'request':request})

@app.get("/simple_test.html", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('simple_test.html', context={'request':request})

@app.get("/F_page.html", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('F_page.html', context={'request':request})

@app.get("/T_page.html", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('T_page.html', context={'request':request})

@app.get("/check_T.html", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('check_T.html', context={'request':request})

@app.get("/new_F.html", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('new_F.html', context={'request':request})

@app.get("/index.html", response_class=HTMLResponse)
def main_page(request: Request):
  return templates.TemplateResponse('index.html', context={'request':request})

@app.post('/check_T.html', response_class=JSONResponse)
async def get_prediction(request: Request):
    input_data = await request.json() # JSON 데이터에서 "text" 키의 값을 추출
    data = input_data["text"]
    # print(data)
    if input_data is None:
        return {"error": "Missing 'text' field in the JSON data."}
    test_dataset = QADataset([data], [data])
    # 모델 테스트
    predictions = test_T_model(test_dataset)
    print(predictions)

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

    predictions = []
    for prediction in total_predictions:
        print(len(prediction))
        if (len(prediction) > 0) and (prediction != ' '):
            predictions.append(prediction)
    print('total_predictions: ', total_predictions)
    print('predictions: ', predictions)
    return {"answers": predictions}


@app.post('/check_F.html', response_class=JSONResponse)
async def get_prediction(request: Request):
    input_data = await request.json() # JSON 데이터에서 "text" 키의 값을 추출
    data = input_data["text"]
    print('------')
    print(data) #, data 가 질문
    if input_data is None:
        return {"error": "Missing 'text' field in the JSON data."}
    test_dataset = QADataset([data], [data])
    # 모델 테스트
    predictions = test_F_model(test_dataset)
    print('----')
    print(predictions) # 답변

    if data in qa_dict:
        answer = qa_dict[data]
        if len(answer) > len(predictions[0]):
            print(len(answer))
            print(len(predictions[0]))
            predictions[0] = answer
            print(predictions)
            return {"answers": predictions}

    print('---------')
    print(predictions)
    print('---------')

    prediction_indexes = []
    specials = ['.', '!', '?']
    predictions_str = ' '.join(predictions)
    for i in range(len(predictions_str)):
        if (predictions_str[i] in specials) and (i != len(predictions_str) -1) and (predictions_str[i+1] not in specials):
            # print(i)
            # print('predictions_str[i]: ', predictions_str[i])
            prediction_indexes.append(i)

    # print(f'len(prediction_indexes): {len(prediction_indexes)}')
    # print(f'prediction_indexes: {prediction_indexes}')
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

    predictions = []
    for prediction in total_predictions:
        print(len(prediction))
        if (len(prediction) > 0) and (prediction != ' '):
            predictions.append(prediction)
    print('total_predictions: ', total_predictions)
    print('predictions: ', predictions)
    return {"answers": predictions}

    # print('total_predictions: ', total_predictions)
    # return {"answers": total_predictions}
