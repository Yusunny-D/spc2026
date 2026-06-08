from transformers import pipeline

model_name="gpt2"

text_generator = pipeline("text-generation", model=model_name)

result = text_generator("Once upon a time, ", max_length=50, truncation=True)[0]

print(result["generated_text"])

