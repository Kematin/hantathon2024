from transformers import pipeline

model = "hmao_model/checkpoint-364"

classifier = pipeline("text-classification", model)

while True:
    text = input("Команда: ")
    print(classifier(text))
