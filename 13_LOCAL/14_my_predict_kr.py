import os
from transformers import pipeline

MODEL_DIR = "./my_local_model_kr"

classifier = pipeline("sentiment-analysis", model=MODEL_DIR, tokenizer=MODEL_DIR)

test_sentences = [
    "내가 만든 AI 모델이 정말 마음에 들어!",
    "오늘은 정말 행복한 하루야.",
    "서비스가 너무 형편없어서 실망했어.",
    "모든 게 잘 안 풀려서 우울해."
]

for text in test_sentences:
    r = classifier(text)
    print(f'문장: {text}')
    print(r)
    print("-"*80)