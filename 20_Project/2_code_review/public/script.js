document.getElementById('codeForm').addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const codeUrl = document.getElementById('codeUrl').value;
    const result = document.getElementById('result');
    const options = document.querySelectorAll('.option');
    let analysis_options = []

    options.forEach(option => {
        if (option.checked === true) {
            console.log(option.value)
            analysis_options.push(option.value)
            }
        }
    )

    // console.log(options)

    const response = await fetch('/api/codecheck', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({codeUrl, 'options': analysis_options})
    });
    const data = await response.json();
    // console.log(data);
    result.innerText = data.result;

});