from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# MNLI = Multi-Genre Natural Language Inference
# 문장/문장 연관성

text = "I just upgraded my computer's graphics card"

candidate_labels = ["technology", "sports", "cooking", "politics"]

result = classifier(text, candidate_labels=candidate_labels)

print(f"문장 : {text}")
for label, score in zip(result["labels"], result['scores']):
    print(f"{label:12} {score:.3f}")

print(f"최종 분류: {result['labels'][0]}")