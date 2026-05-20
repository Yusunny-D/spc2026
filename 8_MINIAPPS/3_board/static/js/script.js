document.addEventListener('DOMContentLoaded', async() => {
    const res = await fetch('/list')
    const data = await res.json();
    console.log(data);
    const result = document.getElementById('card-list')

    data.forEach(post => {
        makeCard(post.id, post.title, post.message)
    });

});

function makeCard(id, title, message) {
    const card = document.createElement('div');
    card.innerHTML = `
    <div>
        <p>${id}</p>
        <p>${title}</p>
        <p>${message}</p>
        <button class='modify'>수정</button>
        <button class='delete'>삭제</button>
    </div>
    `
    document.getElementById('card-list').appendChild(card);

    card.querySelector('.delete').addEventListener('click', async() => {
    // 버튼을 눌렀어 이벤트 시작....
    // id를 가져와서 백으로 넘겨줘
        console.log(id)

        await fetch('/delete', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id})
        });
        card.remove()
    });

    card.querySelector('.modify').addEventListener('click', () => {
        // console.log(id)
        card.innerHTML =`
        <div>
            <p>${id}</p>
            <input name="title" id="new-title" value='${title}'>
            <input name="message" id="new-text" value='${message}'>
            <button class='done'>완료</button>
        </div>
        `

        card.querySelector('.done').addEventListener('click', async() => {
            const new_title = document.getElementById('new-title').value;
            const new_message = document.getElementById('new-text').value;

            console.log('완료 버튼 눌림')

            await fetch ('/modify', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({id, new_title, new_message})
            });

            location.href = '/'
        });
    });
};

document.getElementById('input-submit').addEventListener('click', async() => {
    const title = document.getElementById('input-title').value;
    const message = document.getElementById('input-text').value;

    await fetch('/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title, message})
    });

    location.reload();

});