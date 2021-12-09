def get_errors():
    errors = {
        'out': 'Вы вышли из системы',
        'noAccess': 'У вас нет доступа в этот раздел',
        'unknown': 'Неизвестная ошибка',
        'timeout': 'Система долго не отвечает',
        'robot': 'Ваши действия похожи на робота',
    }
    error = input()
    e = errors[error]

    print(e)


get_errors()
