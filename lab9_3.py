planets_names = ('Меркурій', 'Венера', 'Земля', 'Марс', 'Юпітер', 'Сатурн', 'Уран', 'Нептун')

planets = {}

while True:
    print('1 — Додати планету')
    print('2 — Знайти радіус орбіти')
    print('0 — Вийти')

    choice = input('Оберіть дію: ')

    if choice == '1':
        planet = input('Введіть назву планети: ')
        R = float(input('Введіть радіус орбіт: '))
        
        if planet in planets_names:
            planets[planet] = R
        else:
            print('Планети не знайдено в словнику!')

    elif choice == '2':
        search_planet = input('Введіть назву планети для пошуку: ')
        
        if search_planet in planets:
            print(planets[search_planet])
        
        else:
            print('Планети не знайдено в словнику!')
            
        
    elif choice == '0':
        print('До побачення!')
        break
        
    else:
        print('Такої команди немає!')
        
    





    


