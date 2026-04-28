
let timerID;
let interval;
const timeInput = document.getElementById('timeInput')
const progress = document.getElementById('progress')
const progressText = document.getElementById('progressText')
const startButton = document.getElementById('startButton')
const clearButton = document.getElementById('clearBut0ton')

startButton.addEventListener('click', startProgress)
clearButton.addEventListener('click', clearProgress)

// 모듈화 고민해보기
function startProgress() {
    duration = parseInt(timeInput.value);
    console.log('입력초', duration)
    startButton.disabled = true;

    let elapsed = 0; //초과 시간
    timerID = setInterval(() => {
        // console.log('반복호출');
        elapsed++;
        const ratio = Math.floor((elapsed / duration) * 100); // 진행용 계산
        progress.style.width = `${ratio}%`; // ratio+%
        progressText.textContent = `${ratio}%`;

        if (ratio >= 100) {
            // 타이머 중지
            clearInterval(timerID)
            startButton.disabled = false;
        }
    }, 1000);
}

function clearProgress() {
    if (timerID) { clearInterval(timerID) };
    progress.style.width = '2px' // 살짝 보이게
    timeInput.value = "";
    progressText.textContent = '0%';
    startButton.disabled = false;
}
