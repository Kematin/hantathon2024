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

# Объединяем все словари в один
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
    {"text": "расскажи подробнее о", "label": "detailed_info"},
    {"text": "какая это группа", "label": "disability_group"},
    {"text": "покажи легенду", "label": "legend_info"},
    {"text": "открой карту", "label": "open_card"},
    {"text": "покажи маршрут от до", "label": "path"},
    {"text": "какая легенда у", "label": "legend_place"},
    {"text": "что есть поблизости", "label": "search_radius"},
    {"text": "информация о сайте", "label": "site_info"},
    {"text": "что на карте", "label": "search_place"},
]
