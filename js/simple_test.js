// .answer-image-T를 클릭했을 때 처리하는 함수
function toggleSelected(element) {
    element.classList.toggle('selected-answer');
  }

  // .answer-image-T 클래스를 가진 모든 요소들을 선택합니다.
  const answerImageTs = document.querySelectorAll('.answer-image-T');

  // 각 .answer-image-T 요소에 클릭 이벤트 리스너를 추가합니다.
  answerImageTs.forEach((element) => {
    element.addEventListener('click', () => {
      toggleSelected(element);
    });
  });

  function checkAndRedirect() {
    // F가 선택된 개수를 카운트합니다.
    let fCount = document.querySelectorAll('input[value="F"]:checked').length;
    let tCount = document.querySelectorAll('input[value="T"]:checked').length;

    if (fCount >= 3) {
        // F가 3개 이상 선택된 경우 F_page.html로 이동합니다.
        window.location.href = './F_page.html';
    } if(tCount >=3){
        window.location.href = './T_page.html';
    }
    else {
        // F가 3개 미만 선택된 경우 결과를 확인하는 메시지를 표시합니다.
        document.getElementById('finalResult').innerText = '모두 항목을 선택하여야 합니다!';
        document.getElementById('result').style.display = 'block';
    }
}

// answer_container 내의 모든 이미지 요소를 가져옵니다.
const images = document.querySelectorAll('.answer-image');

// 각 이미지에 클릭 이벤트 리스너를 추가합니다.
images.forEach(image => {
  image.addEventListener('click', handleImageClick);
});

function handleImageClick(event) {
  const clickedImage = event.target;
  const questionContainer = clickedImage.closest('.questions');
  const imagesInQuestion = questionContainer.querySelectorAll('.answer-image');

  // 동일한 질문 컨테이너 내의 모든 이미지에서 "selected" 클래스를 제거합니다.
  imagesInQuestion.forEach(image => {
    image.classList.remove('selected');
  });

  // 클릭된 이미지에 "selected" 클래스를 추가합니다.
  clickedImage.classList.add('selected');
}

const result_btn = document.getElementById('btn')

