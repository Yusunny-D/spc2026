import numpy as np
from transformers import (
    AutoModelForSequenceClassification, AutoTokenizer,
    Trainer, TrainingArguments
)
from datasets import Dataset

train_data = {
    "text": [
        "이 제품이 정말 좋아요!",
        "정말 최악이에요.",
        "저는 행복해요.",
        "저는 슬퍼요.",
        "이 제품은 정말 훌륭해요.",
        "최악의 경험이었어요.",
        "정말 환상적이에요.",
        "정말 싫어요."
    ],
    "label": [1, 0, 1, 0, 1, 0, 1, 0]
}

eval_data = {
    "text": [
        "오늘 기분이 정말 좋아요!",
        "서비스가 형편없었어요.",
        "이 일 때문에 정말 신나요!",
        "기대한 것과 달랐어요."
    ],
    "label": [1, 0, 1, 0]
}

model_name = "beomi/kcbert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(batch['text'], padding="max_length", truncation=True)

train_ds = Dataset.from_dict(train_data).map(tokenize, batched=True)
eval_ds = Dataset.from_dict(eval_data).map(tokenize, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=2,
    id2label={0: "부정", 1: "긍정"},
    label2id={"부정": 0, "긍정": 1}
)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return {"accuracy": float((preds == labels).mean())}

args = TrainingArguments(
    output_dir="./results_kr",
    eval_strategy="epoch",
    save_strategy="epoch",
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=5,
    logging_steps=1
)

trainer = Trainer(
    model=model, args=args,
    train_dataset=train_ds, eval_dataset=eval_ds,
    compute_metrics=compute_metrics
)

trainer.train()
print("평가 결과: ", trainer.evaluate())

save_path="./my_local_model_kr"
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
print("내 모델 저장 완료: ", save_path)