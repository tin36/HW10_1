order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]

order_converted = []

for i in order:
    i['count'] = round(i.pop('skolko'))
    i['specie'] = i.pop('poroda').title()
    i['avg_size'] = round(i.pop('sred_razmer')/10)
    order_converted.append(i)


# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
  for key, value in item.items():
      print(key, value)