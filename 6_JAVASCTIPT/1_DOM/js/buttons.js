// 각자의 버튼이 눌릴 때마다 위의 div의 값을 가져다가 +1 또는 -1을 한다.
// function plus() {
//     const num = parseInt(document.getElementById('number').textContent);
//     console.log(num)
//     number.innerHTML = num+1
// }
// function minus() {
//     const num = parseInt(document.getElementById('number').textContent);
//     console.log(num)
//     number.innerHTML = num-1
// }
// function minus() {
//     document.getElementById('number').textContent -=1;
// }
const button1 = document.getElementById('Pbutton')
const button2 = document.getElementById('Mbutton')

/* 이벤트 핸들러*/
button1.addEventListener('click', () => {
    parseInt(document.getElementById('number').textContent) += 1
})
button2.addEventListener('click', () => {
    document.getElementById('number').textContent -= 1;
    
})