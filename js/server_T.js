const postData = {
  text: "입력값을 받아온다." // 원하는 데이터를 'text' 필드에 넣어줍니다.
};

fetch('http://127.0.0.1:8000/check_T.html', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(postData)
})
.then(response => response.json())
.then(data => {
  // 서버에서 받은 JSON 데이터의 'answers' 필드 값을 사용합니다.
  const answers = data.answers;
  console.log(answers);
  // 여기서 원하는 작업을 수행합니다.
})
.catch(error => console.error('Error:', error));
