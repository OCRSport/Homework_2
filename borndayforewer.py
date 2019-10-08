year = int(input('Введите год рождения Пушкина: '))
while year != 1799:
    print('Неверно')
    year = int(input('Введите год рождения Пушкина: '))
else:
    day = float(input('Введите его день рождения: '))
    # формат ввода - дд.мм
    while day != 26.09:
        print('Неверно')
        day = float(input('Введите его день рождения: '))
    else:
        print('Верно')
