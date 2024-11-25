import torch
from safetensors import safe_open
from transformers import AutoModelForSequenceClassification

# Загрузка модели из safetensors
model_path = "./results/checkpoint-12/model.safetensors"

# Загрузите параметры модели с использованием safetensors
with safe_open(model_path, framework="pt") as f:
    model_state_dict = f.get_tensor()

# Создайте модель
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased", state_dict=model_state_dict
)

# Сохраните модель в формате PyTorch
model.save_pretrained("./train/results/checkpoint-12/pytorch_model")
