// script.js

function sendMessage() {
    var userInput = document.getElementById('userInput').value;
    var chatbox = document.getElementById('chatbox');
  
    // 사용자가 입력한 메시지를 챗봇의 응답과 함께 추가합니다.
    chatbox.innerHTML += `
      <div class="message user-message">
        <p>${userInput}</p>
      </div>
  
      <div class="message chatbot-message">
        <p>챗봇의 응답 또는 처리 로직을 여기에 추가합니다.</p>
      </div>
    `;
  
    // 입력창 내용 초기화
    document.getElementById('userInput').value = '';
  }
  