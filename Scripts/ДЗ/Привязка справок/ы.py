order = [
    {"ооо": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]

order_converted = []



for i in order:
    my_keys = ['count', 'specie', 'avg_size']
    f = []
    while len(f) < len(i):
        for k, v in i.items():
            f.append(k)
    i[my_keys[0]] = round(i.pop(f[0]))
    i[my_keys[1]] = i.pop(f[1]).title()
    i[my_keys[2]] = round(i.pop(f[2]) / 10)
    order_converted.append(i)


# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)