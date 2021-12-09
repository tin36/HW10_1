class Hero:
   def __init__(self, name, things):
     self.name = name
     self.things = things
     print("Я", self.name, "у меня есть", self.things)

   def iteratate_things(self):
     for thing in self.things:
       print(thing)

   def tralala(self):
       print(self.name)

hero_1 = Hero("Кусантий", ["hfg", "Лапки", "Пуговичка", "Масочка"])
hero_1.iteratate_things()
hero_1.tralala()

# Я Кусантий у меня есть ['Голова', 'Лапки', 'Пуговичка', 'Масочка']
# Голова
# Лапки
# Пуговичка
# Масочка