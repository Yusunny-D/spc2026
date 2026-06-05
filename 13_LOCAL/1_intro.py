import ollama

ollama.pull('mistral')
response = ollama.chat(model="mistral", messages=[
    {'role': "user", 'content': "인공지능에 대해서 설명해주세요"}
])

print(response['message']['content'])