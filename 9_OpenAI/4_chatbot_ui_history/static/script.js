document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('user-input');
    const formInput = document.getElementById('user-input-form');
    const resultDiv = document.getElementById('result');

    formInput.addEventListener('submit', async (ev) => {
        ev.preventDefault();

        const chatMessage = chatInput.value;
        // console.log(chatMessage);

        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({chatMessage})
        });
        const data = await response.json()
        console.log(data)

        const chatbotReply = document.createElement('p')
        chatbotReply.innerText = data.reply;
        resultDiv.appendChild(chatbotReply)

        // TODO: 위에 리팩토링 해서 적절하게 분리 1. fetch, 2. 응답 받아서 DOM에 그리는 것

    })
})