from transformers import pipeline

model = "hmao_model/checkpoint-522"

classifier = pipeline("text-classification", model)

while True:
    text = input("Команда: ")
    print(classifier(text))
