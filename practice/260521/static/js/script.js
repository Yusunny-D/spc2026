const form = document.getElementById('user-input');
const chat = document.getElementById('chat-view');


form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const user = document.createElement('p')
    const data = new FormData(form);
    
    const inputData = data.get('input')
    console.log(inputData)
    user.innerText = inputData
    chat.appendChild(user)

    const response = await fetch('/user_input', {
        method: 'POST',
        body: inputData
    });
    const AIreply = await response.text()
    console.log(AIreply)

    const reply = document.createElement('p')
    reply.innerText = AIreply
    chat.appendChild(reply)

    form.querySelector('input').value = '';

});