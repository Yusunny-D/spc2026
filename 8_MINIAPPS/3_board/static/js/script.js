document.addEventListener('DOMContentLoaded', async() => {
    const res = await fetch('/list')
    const data = await res.json();

    
    
}),

function makeCard(id, title, message) {
    const card = document.createElement('div');
    card.innerHTML = `
    <div>
        <p>${id}</p>
        <p>${title}</p>
        <p>${message}</p>
        <button>수정</button>
        <button>삭제</button>
    </div>
    `
    document.getElementById('card-list').appendChild(card);
}

document.getElementById('input-submit').addEventListener('click', () => {
    const title = document.getElementById('input-title')
    const message = document.getElementById('input-text')

    fetch('/create', {
        method: 'POST',
        headers: {'Content-Type': 'applicatoin/json'},
        body: JSON.stringify({title, message})
    })
})