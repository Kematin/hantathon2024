import csv

from .detailed_info import detailed_info_dataset
from .disabilty import disability_group_dataset
from .legend_info import legend_info_dataset
from .legend_place import legend_place_dataset
from .open_card import open_card_dataset
from .path import path_dataset
from .search_place import search_place_dataset
from .search_radius import search_radius_dataset
from .site_info import site_info_dataset

"""
labels:
- site_info
- legend_info
- open_card
- disability_group
- path
- legend_place
- search_radius
- detailed_info
- search_place
"""

# (Для примера) объединяем все словари в один
dataset_info = (
    site_info_dataset
    + legend_info_dataset
    + open_card_dataset
    + disability_group_dataset
    + path_dataset
    + legend_place_dataset
    + search_radius_dataset
    + detailed_info_dataset
    + search_place_dataset
)


test_dataset_info = [
    # Метка "site_info"
    {"text": "информация о сайте", "label": "site_info"},
    {"text": "что за сайт", "label": "site_info"},
    {"text": "расскажи об этом сайте", "label": "site_info"},
    {"text": "что ты знаешь о сайте", "label": "site_info"},
    {"text": "данные о сайте", "label": "site_info"},
    # Метка "legend_info"
    {"text": "покажи легенду", "label": "legend_info"},
    {"text": "что обозначают цвета на карте", "label": "legend_info"},
    {"text": "расскажи о значках на карте", "label": "legend_info"},
    {"text": "объясни легенду карты", "label": "legend_info"},
    {"text": "что означает эта метка", "label": "legend_info"},
    # Метка "open_card"
    {"text": "открой карту", "label": "open_card"},
    {"text": "покажи карту", "label": "open_card"},
    {"text": "запусти карту", "label": "open_card"},
    {"text": "отобрази карту", "label": "open_card"},
    {"text": "покажи карту местности", "label": "open_card"},
    # Метка "disability_group"
    {"text": "какая это группа", "label": "disability_group"},
    {"text": "к какому типу инвалидности относится", "label": "disability_group"},
    {"text": "что это за группа инвалидности", "label": "disability_group"},
    {"text": "определи группу инвалидности", "label": "disability_group"},
    {"text": "какая группа инвалидности у", "label": "disability_group"},
    # Метка "search_place"
    {"text": "покажи местоположение школы номер 1", "label": "search_place"},
    {"text": "где находится советская больница", "label": "search_place"},
    {"text": "покажи адрес детского сада теремок", "label": "search_place"},
    {"text": "найди на карте торговый центр", "label": "search_place"},
    # Метка "detailed_info"
    {"text": "расскажи подробнее о Сургут", "label": "detailed_info"},
    {"text": "подробная информация о Радужный", "label": "detailed_info"},
    {"text": "дай информацию о Нефтеюганск", "label": "detailed_info"},
    {"text": "что ты можешь рассказать о Белоярский район", "label": "detailed_info"},
    {"text": "объясни подробнее о Мегион", "label": "detailed_info"},
    {"text": "хочу больше узнать о Лангепас", "label": "detailed_info"},
    {"text": "что ты знаешь о Когалым", "label": "detailed_info"},
    {"text": "расскажи подробнее о Нижневартовск", "label": "detailed_info"},
    # Метка "search_radius"
    {"text": "найди все адреса в Белоярский район", "label": "search_radius"},
    {"text": "что рядом с Когалым", "label": "search_radius"},
    {"text": "что есть поблизости от Мегион", "label": "search_radius"},
    {"text": "какие объекты рядом с Нефтеюганск", "label": "search_radius"},
    # Метка "path"
    {"text": "как доехать от Сургут до Урай", "label": "path"},
    {"text": "покажи маршрут до Ханты-Мансийск", "label": "path"},
    {"text": "как добраться до Покачи", "label": "path"},
    {"text": "построить маршрут от Радужный до Белоярский", "label": "path"},
    # Метка "legend_place"
    {"text": "какая легенда у района Советский", "label": "legend_place"},
    {"text": "что за место на карте в Нижневартовск", "label": "legend_place"},
    {"text": "расскажи о местоположении по адресу Пыть-Ях", "label": "legend_place"},
]


def get_dataset_from_csv(filename):
    dataset = []

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dataset.append(row)

    return dataset
