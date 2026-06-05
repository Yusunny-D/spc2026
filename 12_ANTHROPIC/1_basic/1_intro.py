import os
import anthropic

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    # haiku, sonnet, opus
    model="claude-haiku-4-5",
    max_tokens=300,
    messages=[{
        "role": 'user', "content": "안녕! 한 문장으로 너를 소개해줘."
    }]
)

print(message.content[0].text)