# С рыбками хорошо работать — они ведут себя тихо и не кусаются. Главное — работникам не заболеть!
#
# Перенесите в подсписок vaccinated только сотрудников, которые прошли вакцинацию, а остальных отправьте в not_vaccinated! Затем распечатайте оба списка в таком формате.
#
# Вакцинированные:
# Киселёв Всеволод Эдуардович
# ...
# Остальные:
# Довлатова Эмилия Ефимовна

employees = [

    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семеновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнев Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for i in employees:
    index = 0
    if i["vaccinated"] == True:
        vaccinated.append(i["fio"])
    else:
        not_vaccinated.append(i["fio"])

print('Вакцинированные:')
for i in vaccinated:
    print(i)

print('Остальные:')
for i in not_vaccinated:
    print(i)