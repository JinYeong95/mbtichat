const menuContainer = document.getElementById('menu__container');
const menuButton = document.getElementById('menu__btn__container');
const dot = document.getElementById('ddd')

// 메뉴 토글 기능 추가
function toggleMenu() {
    if (menuContainer.style.display == 'none') {
        menuContainer.style.display = 'block';
        // 전체 문서에 클릭 이벤트 리스너를 추가, 메뉴 이외의 부분을 클릭했을 때 메뉴를 숨김
        document.addEventListener("click", function(event) {
            if (event.target !== dot && !menuContainer.contains(event.target)) {
                menuContainer.style.display = 'none';
            }
        });
    } else {
        menuContainer.style.display = 'none';
    }
}


// 채팅 메시지 전송 함수
function sendMessage(isUserMessage, messageText) {
    const chatbox = document.getElementById("chatbox");

    // 새로운 메시지 컨테이너 엘리먼트 생성
    const messageContainer = document.createElement("div");
    messageContainer.className = "message-container";

    // 사용자와 봇 메시지에 적절한 클래스 추가
    const messageClassName = isUserMessage ? "user-message" : "bot-message";

    // 새로운 메시지 엘리먼트 생성
    const messageElement = document.createElement("div");
    messageElement.className = messageClassName;
    messageElement.textContent = messageText;

    // 메시지 엘리먼트를 컨테이너에 추가
    messageContainer.appendChild(messageElement);

    // 컨테이너를 채팅창에 추가
    chatbox.appendChild(messageContainer);

    // 채팅창을 항상 아래로 스크롤하기
    chatbox.scrollTop = chatbox.scrollHeight;
}

//---------------------
// 대화 시작 전에 선택된 상태를 추적하기 위한 변수를 선언
let isInputSelected = false;

// 메시지 입력란을 클릭할 때 선택 상태를 변경하는 함수
function toggleInputSelected() {
    isInputSelected = !isInputSelected;
}

// 페이지 로드 시 메시지 입력란에 클릭 이벤트 리스너를 추가
document.getElementById("userInput").addEventListener("click", function() {
    toggleInputSelected();
});

document.addEventListener("click", function(event) {
    const chatbox = document.getElementById("chatbox");
    const userInput = document.getElementById("userInput");

    // 만약 메시지 입력란이 선택된 상태이고, 클릭한 부분이 메시지 입력란이 아니라면 선택을 해제
    if (isInputSelected && event.target !== userInput && !userInput.contains(event.target)) {
        toggleInputSelected();
    }
});
//---------------------

// sendBtn 클릭 이벤트 처리
document.getElementById("sendBtn").addEventListener("click", function() {
    sendMessageFromInput();
});
// userInput에서 Enter 키가 눌렸을 때 메시지 전송
document.getElementById("userInput").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        sendMessageFromInput();
    }
});

// 메시지 전송 함수
async function sendMessageFromInput() {
    const userInput = document.getElementById("userInput");
    const messageText = userInput.value.trim();
    console.log(messageText)
    const Text = {
    "text":messageText
    }
    if (messageText !== "") {
    sendMessage(true, messageText);
    userInput.value = ""; // 메시지를 보낸 후 입력 필드 초기화
    }
    await fetch('http://127.0.0.1:8000/check_F.html', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(Text)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        async function processBotResponses() {
            const botResponses = data.answers;
        
            for (let i = 0; i < botResponses.length; i++) {
                await new Promise((resolve) => {
                    setTimeout(() => {
                        sendMessage(false, botResponses[i]);
                        resolve();
                    }, 500); // 1000ms(1초)마다 출력됩니다. 원하는 대기 시간을 조정하세요.
                });
            }
        }
        
        processBotResponses();
    })
}

// 페이지 로드 후 1초 뒤에 챗봇의 시작 메시지 출력
setTimeout(function() {
    sendMessage(false, "대화를 시작합니다! 메시지를 입력하세요.");
}, 1000);

// ------
// 대화 저장 기능
document.getElementById("save_convo").addEventListener("click", function() {
    saveConversation();
});
    // 대화를 텍스트파일로 저장 
function saveConversation() {
    const chatbox = document.getElementById("chatbox");
    const messages = chatbox.querySelectorAll(".message-container .user-message, .message-container .bot-message");
    let conversation = "";

    for (const message of messages) {
        conversation += message.textContent + "\n";
    }

    const blob = new Blob([conversation], { type: "text/plain" });
    const url = URL.createObjectURL(blob);   // Blob 객체를 다운로드 할 수 있는 URL 생성 
    const link = document.createElement("a");
    link.href = url;
    link.download = "conversation.txt";
    link.click();
}


// 대화 재시작 기능
document.getElementById("restart_convo").addEventListener("click", function() {
    restartConversation();
});

function restartConversation() {
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML = ""; // 채팅창 비우기

    // 1초 뒤에 챗봇의 시작 메시지 출력
    setTimeout(function() {
        sendMessage(false, "대화를 다시 시작합니다! 메시지를 입력하세요.");
    }, 1000);
}
