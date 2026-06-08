# NSMC = Naver Sentiment Movie corpus

import numpy as np
from transformers import (
    AutoModelForSequenceClassification, AutoTokenizer,
    Trainer, TrainingArguments
)
from datasets import load_dataset

MODEL = "beomi/kcbert-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

ds = load_dataset("nsmc", trust_remote_code=True)
# ds = load_dataset("e9t/nsmc")

train_ds = ds["train"].filter(lambda x: bool(x["document"])).shuffle(seed=42).select(range(2000))
eval_ds = ds["test"].filter(lambda x: bool(x["document"])).shuffle(seed=42).select(range(500))

print(f"학습 데이터 수: {len(train_ds)}, 평가 데이터 수 {len(eval_ds)}")
print(f"예시: {train_ds[0]['document'][:30]}, {eval_ds[0]['document'][:30]}")
