import requests
import json

class Auto:
    def __init__(self, marka, years,price,customs,name, vozrast, sex):
        self.marka = marka
        self.years = years
        self.price = price
        self.customs = customs
        self.name = name
        self.vozrast = vozrast
        self.sex = sex

    def __repr__(self):
        return self.marka

list = []
questions_dict = json.loads(requests.get('https://jsonkeeper.com/b/B23G').text)

for i in questions_dict:
    list.append(Auto(
        marka=i,
        years=questions_dict[i]['years'],
        price=questions_dict[i]['price'],
        customs=questions_dict[i]['customs'],
        name=questions_dict[i]['owner']['name'],
        vozrast=questions_dict[i]['owner']['vozrast'],
        sex=questions_dict[i]['owner']['sex'],
        ))


s = input('Марку')
for i in list:


    if s != i.marka:
        continue
    else:

        print(f"""Марка: {i}
Цена: {i.price}
Ремонты в {', '.join(i.customs)}
Владелец: {i.name}
Возвраст: {i.years}
Пол: {i.sex}
""")

