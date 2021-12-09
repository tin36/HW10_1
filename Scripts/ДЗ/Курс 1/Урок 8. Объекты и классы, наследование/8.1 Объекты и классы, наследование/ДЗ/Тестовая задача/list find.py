
class Auto:
    def __init__(self, marka, fiff):
        self.marka = marka
        self.fiff = fiff


    def __str__(self):
        return self.marka

s = Auto('2', '1')

print(s)