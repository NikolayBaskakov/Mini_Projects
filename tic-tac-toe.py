rules = """Выберите, кто будет играть крестиками, а кто - ноликами. 
После соответствующих подсказок, чтобы походить, введите две цифры подряд без пробелов: первая цифра - это номер строки, 
вторая цифра - это номер столбца, куда вы хотите походить! Хорошей игры!""" 
field= [[' ', 0, 1, 2],
         [0, '-', '-', '-'],
         [1, '-', '-', '-'],
         [2, '-', '-', '-']]
game = True
moves_list = ['00', '01','02', '10', '11', '12', '20', '21', '22']
check_list = []
move_number = 0

def win(field):
    if (field[1][1] == 'x' and field[1][2] == 'x' and field[1][3] == 'x') or \
    (field[2][1] == 'x' and field[2][2] == 'x' and field[2][3] == 'x') or \
    (field[3][1] == 'x' and field[3][2] == 'x' and field[3][3] == 'x') or \
    (field[1][1] == 'x' and field[2][1] == 'x' and field[3][1] == 'x') or \
    (field[1][2] == 'x' and field[2][2] == 'x' and field[3][2] == 'x') or \
    (field[1][3] == 'x' and field[2][3] == 'x' and field[3][3] == 'x') or \
    (field[1][1] == 'x' and field[2][2] == 'x' and field[3][3] == 'x'):
        print("Выиграли крестики, поздравляем!")
        return False
    elif (field[1][1] == 'o' and field[1][2] == 'o' and field[1][3] == 'o') or \
    (field[2][1] == 'o' and field[2][2] == 'o' and field[2][3] == 'o') or \
    (field[3][1] == 'o' and field[3][2] == 'o' and field[3][3] == 'o') or \
    (field[1][1] == 'o' and field[2][1] == 'o' and field[3][1] == 'o') or \
    (field[1][2] == 'o' and field[2][2] == 'o' and field[3][2] == 'o') or \
    (field[1][3] == 'o' and field[2][3] == 'o' and field[3][3] == 'o') or \
    (field[1][1] == 'o' and field[2][2] == 'o' and field[3][3] == 'o'):
        print("Выиграли нолики, поздравляем!")
        return False
    else:
        return True

def move_func(move, sign):
    row = int(move[0]) + 1
    col = int(move[1]) + 1
    field[row][col] = sign


print(rules)
while game:
    for i in field:
            print(*i)
    if move_number % 2 == 0:
       move = input('Походите крестиком ')
       sign = 'x'
    else:
        move = input('Походите ноликом ')
        sign = 'o'
    if move in moves_list:
        move_func(move, sign)
        moves_list.remove(move)
        check_list.append(move)
        move_number += 1
        game = win(field)
        if move_number == 9:
            game = False
            print('Ничья')
    elif move in check_list:
        print('Сюда уже был сделан ход')
    else:
        print('Неверно введены цифры для хода')
        

