def fullname_split(fullname_str):
    namr_parts = fullname_str.split(' ')
    return namr_parts[1], namr_parts[0], namr_parts[2]

surname, namr, patronymic = fullname_split('Тарасов Иван Николанвич')

print((namr))