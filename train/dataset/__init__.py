from .legend_info import legend_info_dataset
from .open_card import open_card_dataset
from .site_info import site_info_dataset

# Карта
open_card_dataset = {
    "Покажи карту": "open_card",
    "Открой карту": "open_card",
    "Карта": "open_card",
    "Хочу увидеть карту": "open_card",
    "Покажи местность на карте": "open_card",
    "Где карта?": "open_card",
    "Отобрази карту": "open_card",
    "Покажи план местности": "open_card",
    "Аткрой карту": "open_card",
    "Карата": "open_card",
    "Хочу увиеть карту": "open_card",
    "Покажи местнасть на карте": "open_card",
    "Где карата?": "open_card",
    "Отобрази карату": "open_card",
    "Покажи план местнасти": "open_card",
}

# Группа инвалидности
disability_group_dataset = {
    "Расскажи про группу инвалидности": "disability_group",
    "Какая это группа": "disability_group",
    "Расскажи об инвалидности": "disability_group",
    "Что это за группа инвалидности": "disability_group",
    "Объясни про инвалидность": "disability_group",
    "Какие бывают группы инвалидности?": "disability_group",
    "Объясни группы инвалидности": "disability_group",
    "Какая ето группа": "disability_group",
    "Раскажи об инвалидности": "disability_group",
    "Што ето за группа инвалидности": "disability_group",
    "Объесни про инвалидность": "disability_group",
    "Какие быывают группы инвалидности?": "disability_group",
    "Объесни группы инвалидности": "disability_group",
}

# Построение маршрута
path_dataset = {
    "Как добраться от до": "path",
    "Построй маршрут до": "path",
    "Как дойти до": "path",
    "Как пройти к": "path",
    "Покажи маршрут от до": "path",
    "Как мне попасть в": "path",
    "Как доехать до": "path",
    "Маршрут до": "path",
    "Как дабраться от до": "path",
    "Пастрой маршрут до": "path",
    "Как дойти до": "path",
    "Как прайти к": "path",
    "Покажи маршут от до": "path",
    "Как мне патрапить в": "path",
    "Как доехат до": "path",
    "Маршрут до": "path",
}

# Легенда для объекта
legend_place_dataset = {
    "Покажи легенду для": "legend_place",
    "Расскажи легенду для": "legend_place",
    "Легенда для объекта": "legend_place",
    "Какая легенда у": "legend_place",
    "Объясни легенду объекта": "legend_place",
    "Что за легенда у": "legend_place",
    "Расскажи историю объекта": "legend_place",
    "Покажи легенду для": "legend_place",
    "Раскажи легенду для": "legend_place",
    "Легенда для абьекта": "legend_place",
    "Какая легенда у": "legend_place",
    "Объесни легенду абьекта": "legend_place",
    "Што за легенда у": "legend_place",
    "Раскажи историю абьекта": "legend_place",
}

# Поиск объектов в радиусе
search_radius_dataset = {
    "Найди все адреса в радиусе": "search_radius",
    "Какие адреса есть в радиусе": "search_radius",
    "Поиск адресов в радиусе": "search_radius",
    "Адреса поблизости": "search_radius",
    "Найди объекты рядом": "search_radius",
    "Что есть поблизости?": "search_radius",
    "Поиск вокруг": "search_radius",
    "Какие адреса ест в радиусе": "search_radius",
    "Поиcк адреcов в радиусе": "search_radius",
    "Адреcа поблизи": "search_radius",
    "Найди абьекты рядом": "search_radius",
    "Што ест поблизи?": "search_radius",
    "Поиcк вакруг": "search_radius",
}

# Подробная информация
detailed_info_dataset = {
    "Расскажи подробнее о": "detailed_info",
    "Покажи подробности о": "detailed_info",
    "Подробная информация о": "detailed_info",
    "Что ты знаешь о": "detailed_info",
    "Дай больше информации о": "detailed_info",
    "Объясни подробнее про": "detailed_info",
    "Хочу знать больше о": "detailed_info",
    "Покажи падробности о": "detailed_info",
    "Падробная информация о": "detailed_info",
    "Што ты знаеш о": "detailed_info",
    "Дай болше информации о": "detailed_info",
    "Объесни падробнее про": "detailed_info",
    "Хочу знаеть болше о": "detailed_info",
}

# Поиск в указанной местности
search_place_dataset = {
    "Найти мне в поселке/городе": "search_place",
    "Найди в городе": "search_place",
    "Что есть в поселке": "search_place",
    "Поиск в местности": "search_place",
    "Что находится в городе?": "search_place",
    "Найди в этом районе": "search_place",
    "Поиск в поселении": "search_place",
    "Найди в гароде": "search_place",
    "Што ест в паселке": "search_place",
    "Поиcк в местнасти": "search_place",
    "Што нахадится в гароде?": "search_place",
    "Найди в етом районе": "search_place",
    "Поиcк в паселении": "search_place",
}

# Объединяем все словари в один
dataset = {
    **site_info_dataset,
    **legend_info_dataset,
    **open_card_dataset,
    **disability_group_dataset,
    **path_dataset,
    **legend_place_dataset,
    **search_radius_dataset,
    **detailed_info_dataset,
    **search_place_dataset,
}
