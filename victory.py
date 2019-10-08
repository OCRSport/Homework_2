# Год рождения современных писателей Росии
while True:
    # Пелевин - 1962
    year_1 = int(input('Год рождения Пелевина? '))
    if year_1 == 1962:
        year_1 = 1
    else:
        year_1 = 0
    # Сорокин - 1955
    year_2 = int(input('Год рождения Сорокина? '))
    if year_2 == 1955:
        year_2 = 1
    else:
        year_2 = 0
    # Акунин - 1956
    year_3 = int(input('Год рождения Акунина? '))
    if year_3 == 1956:
        year_3 = 1
    else:
        year_3 = 0
    # Глуховский - 1979
    year_4 = int(input('Год рождения Глуховского? '))
    if year_4 == 1979:
        year_4 = 1
    else:
        year_4 = 0
    # Быков - 1967
    year_5 = int(input('Год рождения Быкова? '))
    if year_5 == 1967:
        year_5 = 1
    else:
        year_5 = 0
    summ = year_1 + year_2 + year_3 + year_4 + year_5
    print('Количество правильных ответов: ', summ)
    print('Количество ошибок: ', 5 - summ)
    print('Процент правильных ответов: ', summ * 100 / 5)
    print('Процент неправильных ответов: ', (5 - summ) * 100 / 5)
    answer = input('Начать викторину сначала? Да/Нет ')
    if answer == 'Нет':
        break
