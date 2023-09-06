## 1. MBTI Chatbot
<div align="center">
  <img width="20%" height="20%" src="https://github.com/JinYeong95/mbtichat/assets/117560090/ebb74f2a-670d-48a0-90b1-a255f4dc8a30"/>
<br>
<br>
Mbti Chatbot은 2022년 7월 19일부터 8월 9까지 개발된 프로젝트입니다.<br>
T와 F로 나눈 채팅 유형을 구분하여 선택하고 대화할 수 있습니다.<br>
다양한 언어모델을 사용하여 사용자가 제시하는 신조어를 빠르게 이해하고 번역하는 역할을 수행합니다.<br>
</div>

## 2. 프로젝트 내용
<div align="center">
MBTI는 최근 가장 인기 있는 개인 성격 검사 도구로, T와 F로 구분되는 대화 방식을 구현하였습니다.<br>
이를 위해 GPT 언어모델, 특히 KoGPT2 모델을 사용하여 챗봇을 구현하였습니다.<br>
이외 사용자에 맞는 대화 유형을 찾기 위해 간단한 5문항을 통해 자신의 성향이 T인지 F인지 체크할 수 있습니다.<br>
</div>

## 3. 데이터셋 수집
<div align="center">
  <img width="80%" height="80%" src="https://github.com/JinYeong95/mbtichat/assets/117560090/2b3e8801-8977-42fa-8bbb-22baf17fabb0"/>
<br>
  1. 모두의 말뭉치 데이터셋에서 주제별 텍스트 일상 대화 데이터를 활용하였습니다.<br>
  2. 단, 여기서 카카오톡 데이터만 활용하였습니다.<br>
  3. 그 외에는 해당 팀원들과 해당 문항을 만들고 T,F 문항 1850개를 만들어 사용하였습니다.<br>
</div>

## 4. 사용 방법

1. 해당 파일을 다운 받습니다.(너무 용량이 커서, 구글드라이브로 대체합니다)
   * [구글드라이브](https://drive.google.com/file/d/1_UiK4ecqCnUxKZjutgTDR64VMp3BYnLR/view)
3. (Visual studio code 기준) 해당 파일을 압축을 해제하여 파일을 visual code studio 위에 놓습니다.
4. !pip install fastapi 'uvicorn[standard]' 를 입력하여 pip를 설치합니다.
5. uvicorn main:app --reload 를 입력하여 실행시킵니다.
6. Uvicorn running on http://127.0.0.1:8000 이라는 문구가 뜰텐데, http://127.0.0.1:8000 를 크롬 등 인터넷을 가동시키는 곳에 주소를 복사하여 입력합니다.
7. F12를 눌러 핸드폰 화면 크기로 전환하고, 사용하시면 됩니다!(T, F, 간단 테스트하기)

## 5. 작동 예시
<div align="center">
  <img width="40%" height="20%" src="https://github.com/JinYeong95/mbtichat/assets/117560090/38814317-4968-452f-a333-74a3ee343724"/>
  <img width="40%" height="20%" src="https://github.com/JinYeong95/mbtichat/assets/117560090/3e17e58e-b63b-4c55-8ce0-a5cbb7f90863"/>
</div>

## 6. STACKS
<div align="center">
  <img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white">
  <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white">
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  
  <br>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <br>
  
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">
  <img src="https://img.shields.io/badge/fastapi-009608?style=for-the-badge&logo=fastapi&logoColor=white">
  <br>

</div>
