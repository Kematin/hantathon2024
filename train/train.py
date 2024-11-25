import pandas as pd
from dataset import dataset
from datasets import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

# Преобразуем данные в DataFrame
data = pd.DataFrame(list(dataset.items()), columns=["text", "label"])

# Преобразуем метки в числовые
label_mapping = {label: idx for idx, label in enumerate(data["label"].unique())}
data["label"] = data["label"].map(label_mapping)

# Пересоздаем Dataset
hf_dataset = Dataset.from_pandas(data)

# Разделение на тренировочный и тестовый наборы
train_test_split = hf_dataset.train_test_split(test_size=0.2)
train_dataset = train_test_split["train"]
test_dataset = train_test_split["test"]

# Выводим структуру данных для проверки
print(train_dataset)
print(test_dataset)

# Загружаем токенизатор и модель
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)


# Токенизация
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True)
tokenized_test_dataset = test_dataset.map(tokenize_function, batched=True)

# Создаем модель
num_labels = len(data["label"].unique())
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=num_labels
)

# Настройка параметров обучения
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
)

# Создание тренера
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_test_dataset,
)

# Обучение модели
trainer.train()

predictions = trainer.predict(tokenized_test_dataset)
print(predictions)
