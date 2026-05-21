const form = document.getElementById('user-input');


form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    
    const inputData = data.get('input')
    console.log(inputData)

    fetch('/user_input', {
        method: 'POST',
        body: inputData
    });
    
});