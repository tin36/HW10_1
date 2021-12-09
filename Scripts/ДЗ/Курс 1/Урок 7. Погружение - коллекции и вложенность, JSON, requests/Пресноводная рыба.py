fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for i in fish:
    if i['water'] == 'fresh':
        fresh_water.append(i['specie'])
    else:
        sea_water.append(i['specie'])
print(f'Морские: {", ".join(sea_water)}')
print(f'Пресноводные: {", ".join(fresh_water)}')