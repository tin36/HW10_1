class Hero():

  def __init__(self, name, posessions):
    self.name = name
    self.posessions = posessions
    print(f'Герой {self.name} взял с собой {", ".join(self.posessions)}')



hero = Hero("Питомир", ["меч", "плащ", "шляпа"])