fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(fish_name):
    for i in fish:
        if i["specie"] == fish_name:
            return  (i["specie"], i["water"])

print(type(get_fish('Белуга')))

