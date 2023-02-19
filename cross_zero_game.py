# Программа игры "крестики-нолики"

def greet():   # Функция начального приветсвия и объяснения правил игры:
    print('Приветствуем Вас в игре')
    print('  крестики - нолики')
    print('------------------------')
    print('Правила следующие:')
    print('Два игрока (Х и 0) ходят поочерёдно,')
    print('начиная с "Х"')
    print('выигрывает игрок, который')
    print('заполнил любую линию, столбец')
    print('или диагональ своим символом')
    print('----------------------------')
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():     # Функция распечатки текущего вида игрового поля
    print("   ", "0  ", "1  ", "2  ")
    print('--+---+---+---+')
    for i in range(3):
        print(f" {i}| {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("--+---+---+---+")


def ask():      # Функция ввода координат очередного хода и проверки этих координат
    while True:
        cords = input("Введите координаты: ").split()
        if len(cords) != 2:      # проверка на верное количество введённых координат
            print("Введите ДВЕ координаты")
            continue
        row, column = cords
        if not(cords[0].isdigit()) or not(cords[1].isdigit()):   # проверка верности типа введённых данных
            print("Введите ЧИСЛОВЫЕ координаты")
            continue
        else:
            row, column = int(row), int(column)
        if any([row > 2, row < 0, column > 2, column < 0]):    # проверка, попадают ли введенные координаты в поле
            print("Введённые координаты вне игрового поля")
            continue
        if field[row][column] != " ":    # проверка, занята ли ячейка введённых координат
            print("Ход невозможен, так как указанная ячейка занята")
            continue
        return row, column


def win_check():   # Функция проверки выигрышной комбинации
    result = bool(False)
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != " ":
            print(f"{field[i][0]} - одержал победу, заполнив строку  {i}")
            result = bool(True)
        elif field[0][i] == field[1][i] == field[2][i] != " ":
            print(f"{field[0][i]} - одержал победу, заполнив столбец {i}")
            result = bool(True)
    if field[0][0] == field[1][1] == field[2][2] != " ":
        print(f"{field[0][0]} - одержал победу, заполнив главную диагональ")
        result = bool(True)
    if field[0][2] == field[1][1] == field[2][0] != " ":
        print(f"{field[2][0]} - одержал победу, заполнив побочную диагональ")
        result = bool(True)
    return result


field = [[" "]*3 for i in range(3)]     # Обнуление игрового поля:

greet()
show()
for j in range(9):
    if j % 2 == 0:
        print('ходит "X"')
        x, y = ask()
        field[x][y] = "X"
    if j % 2 == 1:
        print('ходит "0"')
        x, y = ask()
        field[x][y] = "0"
    show()
    res = win_check()
    if res:
        break
    if j == 8 and (not res):
        print("Игра окончена: ничья")
