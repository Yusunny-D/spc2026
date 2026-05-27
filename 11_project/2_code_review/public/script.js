document.getElementById('codeForm').addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const codeUrl = document.getElementById('codeUrl').value;
    const result = document.getElementById('result');

    const response = await fetch('/api/codecheck', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({codeUrl})
    });
    // const data = await response.json();
    // // console.log(data);
    // result.innerText = data.result;

});