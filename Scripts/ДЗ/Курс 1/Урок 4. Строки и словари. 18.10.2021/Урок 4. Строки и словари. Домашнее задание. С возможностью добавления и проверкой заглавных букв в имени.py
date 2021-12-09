#Словарь
dictionary = {
"mouse": 2,
"difficult": 7,
"surprise": 7,
}

#Булевый словарь
bul = {}

#Список с ответами (Угадано/Не угадано)
answer = []

#Заменяющий символл
symbol = '*'
index = 0

#Приветсвие и проверка имени на наличие пробелов и чисел
while True:
  name = str(input("""Привет, введите, пожалуйста, имя!
Оно должно быть без пробелов и цифр\n"""))
  
  if name == "admin":
    while True:
      
      new_key = str(input('Введи слово. Для сохраниения, набери - save\n'))
      if new_key == "save":
        print()
        print("Слова добавлены!")
        print()
        break
      new_value = int(input('Введи номер буквы:\n'))
      dictionary[new_key] = new_value
      
  if name.isalpha() == False and name != "admin":
    print('В имени присутсвуют пробелы')
  elif " ".join(i for i in name if i.istitle()):
    print('В имени есть заглавные буквы')
  else:
    print(f'Отлично, {name}, давай начнем тренировку!')
    break
  
    

#Цикл перебора ключей, проверка ответов пользователя, добавление значения в булевый словарь и список 
for key, value in dictionary.items():
  if value > 0:
    print(f"Вставьте пропущенную букву в слове: {key[:value-1] + symbol + key[value:]}\n")
    string = input()
    if string == key[value-1:value]:
      index += 1
      bul[index] = True
      if bul[index] == True:
        answer.append(f"{index} - {key} - угадано!")
      print("Ответ верный")
      print()      
    else:
      print(f"Ответ неверный. Верный ответ – {key[value-1:value]}")
      index += 1
      bul[index] = False
      if bul[index] == False:
        answer.append(f"{index} - {key} - не угадано!")
      
#Подсчет итогов
print(f"Вот и все, {name}")
for i in answer:
  print(i)