def get_errors(*args):
    errors = {
        'out': 'Вы вышли из системы',
        'noAccess': 'У вас нет доступа в этот раздел',
        'unknown': 'Неизвестная ошибка',
        'timeout': 'Система долго не отвечает',
        'robot': 'Ваши действия похожи на робота',
    }
    values = []
    for i in args:
        for k, v in errors.items():
            if i == k:
                values.append(v)

    print(values)


get_errors('out', 'noAccess')
