import pandas as pd

from dataset import dataset_info

df = pd.DataFrame(dataset_info)

df.to_csv("dataset.csv", index=False, encoding="utf-8")

print("Датасет успешно сохранен в файл dataset.csv!")
