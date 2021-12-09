store = [
    {'name' : 'яблоки', 'price' : 100, 'ava': 40},
    {'name' : 'лимон', 'price' : 452, 'ava': 40},
    {'name' : 'киви', 'price' : 410, 'ava': 40},
    {'name' : 'апельсин', 'price' : 578, 'ava': 40},
]

for i in store:
    price = i['price'] / 2
    i['price'] = price
    print(i)