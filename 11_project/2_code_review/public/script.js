document.getElementById('codeForm').addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const code = document.getElementById('code').value;
    const result = document.getElementById('result');

    const response = await fetch('/api/codecheck', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({code})
    });
    const data = await response.json();
    // console.log(data);
    result.innerText = data.result;

});