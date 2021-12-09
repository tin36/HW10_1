store = {
    "apples": {"name": "Яблоки", "price": "100", "available": 40},
    "oranges": {"name": "Апельсины", "price": "200", "available": 20},
    "pomegranate": {"name": "Гранаты", "price": "400", "available": 5},
}

stocktaking = {}
for key, vaule in store.items():
    stocktaking[key] = vaule["available"]

print(stocktaking)
