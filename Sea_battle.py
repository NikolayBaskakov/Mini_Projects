import random as rnd
import time
import sys

class GameBoard:
    def __init__(self, name=None):
        self.curent_status = [[' |','1|','2|','3|','4|','5|','6|',''],
                                 ['1|','0|','0|','0|','0|','0|','0|',''],
                                 ['2|','0|','0|','0|','0|','0|','0|',''],
                                 ['3|','0|','0|','0|','0|','0|','0|',''],
                                 ['4|','0|','0|','0|','0|','0|','0|',''],
                                 ['5|','0|','0|','0|','0|','0|','0|',''],
                                 ['6|','0|','0|','0|','0|','0|','0|',''],
                                 ['  ','  ','  ','  ','  ','  ','  ','']]
        self.name = name
    
    def board_output(self): 
        for i in self.curent_status:
            print(*i)
    
    def ship_add(self, ship): 
        if self.curent_status[ship.row][ship.col] == '0|': 
            if (self.curent_status[ship.row - 1][ship.col] != '■|' and 
                    self.curent_status[ship.row + 1][ship.col] != '■|' and
                    self.curent_status[ship.row][ship.col - 1] != '■|' and
                    self.curent_status[ship.row][ship.col + 1] != '■|'):
                    if ship.size == 1:
                        self.curent_status[ship.row][ship.col] = '■|'
                    elif ship.size == 2:
                        if ship.direction == 'вверх':
                            if ship.row == 1:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row - 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row - 2][ship.col] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row - 1][ship.col] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        if ship.direction == 'вниз':
                            if ship.row == 6:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row + 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row + 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row + 2][ship.col] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row + 1][ship.col] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        if ship.direction == 'вправо':
                            if ship.col == 6:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row + 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row][ship.col + 2] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row][ship.col + 1] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        if ship.direction == 'влево':
                            if ship.col == 1:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row + 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row][ship.col - 2] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row][ship.col - 1] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                    elif ship.size == 3:
                        if ship.direction == 'вверх':
                            if ship.row == 1 or ship.row == 2:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row - 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row - 2][ship.col] != '■|' and
                                  self.curent_status[ship.row - 2][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row - 2][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row - 3][ship.col] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row - 1][ship.col] = '■|'
                                self.curent_status[ship.row - 2][ship.col] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        elif ship.direction == 'вниз':
                            if ship.row == 6 or ship.row == 5:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row + 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row + 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row + 2][ship.col] != '■|' and
                                  self.curent_status[ship.row + 2][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row + 2][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row + 3][ship.col] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row + 1][ship.col] = '■|'
                                self.curent_status[ship.row + 2][ship.col] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        elif ship.direction == 'вправо':
                            if ship.col == 6 or ship.col == 5:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row + 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col + 1] != '■|' and
                                  self.curent_status[ship.row][ship.col + 2] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col + 2] != '■|' and
                                  self.curent_status[ship.row + 1][ship.col + 2] != '■|' and
                                  self.curent_status[ship.row][ship.col + 3] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row][ship.col + 1] = '■|'
                                self.curent_status[ship.row][ship.col + 2] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        elif ship.direction == 'влево':
                            if ship.col == 1 or ship.col == 2:
                                raise ValueError('Невозможно поставить сюда корабль')
                            elif (self.curent_status[ship.row + 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col - 1] != '■|' and
                                  self.curent_status[ship.row][ship.col - 2] != '■|' and
                                  self.curent_status[ship.row - 1][ship.col - 2] != '■|' and
                                  self.curent_status[ship.row + 1][ship.col - 2] != '■|' and
                                  self.curent_status[ship.row][ship.col - 3] != '■|'):
                                self.curent_status[ship.row][ship.col] = '■|'
                                self.curent_status[ship.row][ship.col - 1] = '■|'
                                self.curent_status[ship.row][ship.col - 2] = '■|'
                            else:
                                raise ValueError('Невозможно поставить сюда корабль')
                        else:
                            raise ValueError('Такого направления нет')
                    else:
                        raise ValueError('Нельзя поставить корабль такого размера')
            else:
                raise ValueError('Невозможно поставить сюда корабль')
        else:
            raise ValueError('Невозможно поставить сюда корабль')
class Ship:
    def __init__(self, row, col, direction, size):
        self.__size = size
        self.__col = col
        self.__row = row
        self.__direction = direction
    
    @property
    def size(self):
        return self.__size
    
    @property
    def list_directions(self):
        return self.__list_directions
    
    @property
    def col(self):
        return self.__col
    @col.setter
    def col(self,value):
        if 0 < value < 7:
            self.__col = value
        else:
            raise ValueError('Недопустимое значение')
        
    @property
    def row(self):
        return self.__row
    @row.setter
    def row(self,value):
        if 0 < value < 7:
            self.__row = value
        else:
            raise ValueError('Недопустимое значение')
        
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self,value):
        if value in self.list_directions:
            self.__direction = value
        else:
            raise ValueError('Недопустимое значение')
    
        
    
class Ship1(Ship):
    def __init__(self, row, col, direction, size=1):
        super().__init__(row, col, direction, size)
    
class Ship2(Ship):
    def __init__(self, row, col, direction, size=2):
        super().__init__(row, col, direction, size)

class Ship3(Ship):
    def __init__(self, row, col, direction, size=3):
        super().__init__(row, col, direction, size)

class ShipFactory:

    @staticmethod
    def create_ship(size, row, col, direction):
        if size == 1:
            return Ship1(row, col, direction)
        if size == 2:
            return Ship2(row, col, direction)
        if size == 3:
            return Ship3(row, col, direction)

class GameLogic:
    def __init__(self):
        self.__rules = 'Приветствуем вас в игре "морской бой"! \n \
                        Правила игры: у вас в распоряжении личный флот в следующем составе: \n \
                        1 трёхпалубный корабль, 2 двухпалубных корабля, 4 однопалубных корабля. \n \
                        Флот такого же размера присутствует и у противника. Игровое поле составляет сетку 6 на 6 клеток.\n \
                        В начале игры Вам будет предложено расставить корабли на своем игровом поле, \n \
                        корабли на полепротивника расставлены в случайном порядке. \n \
                        При расстановке кораблей они не должны соприкасаться сторонами, но могут соприкасаться углами. \n \
                        Чтобы поставить корабль на игровое поле, следуйте подсказкам на экране. \n \
                        При неправильном размещении корабля будут высвечиваться соответсвующие предупреждения. \n \
                        После расстановки кораблей начнётся "фаза боя". В этой фазе ни вы, ни ваш противник \n \
                        не видите корабли друг друга. Ходы заключаются в стрельбе по клеткам с целью попасть в корабль противника. \n \
                        Ходы производятся по очереди. Чтобы походить введите соответствующее клетке значение строки, \n \
                        и столбца, куда хотите выстрелить в соответствии со всплывающими подсказками. \n \
                        Побеждает игрок, который первый уничтожит флот противника.Удачной игры!'
        self.__available_ships = [3, 2, 2, 1, 1, 1, 1]
        self.__list_directions = ['вверх', 'вниз', 'вправо', 'влево']
    
    @property
    def rules(self):
        return self.__rules
    
    @property
    def available_ships(self):
        return self.__available_ships
    
    @property
    def list_directions(self):
        return self.__list_directions
    
    def shot(self, row, col, defense_board, atack_board):
        if defense_board.curent_status[row][col] == '■|':
            atack_board.curent_status[row][col] = 'X|'
            defense_board.curent_status[row][col] = 'X|'
            print(f'Цель поражена в клетке {row, col} ')
        elif defense_board.curent_status[row][col] == 'X|' or defense_board.curent_status[row][col] == 'T|':
            raise Warning('Вы уже стреляли сюда')
        else:
            atack_board.curent_status[row][col] = 'T|'
            defense_board.curent_status[row][col] = 'T|'
            print(f'Промах в клетке {row, col}')

    def user_motion(self, defense_board, atack_board):
        print('Ваш ход')
        not_available = True
        while not_available:
            try:
               user_row = int(input('Введите номер строки, соответствующей клетке для выстрела \n'))
               user_col = int(input('Введите номер столбца, соответствующего клетке для выстрела \n'))
            except ValueError:
                print('Недопустимое значение.Значение должно быть целым числом от 1 до 6')
                continue
            if not (0 < user_row < 7 and 0 < user_col < 7) :
                print('Недопустимые значения.Значения должны быть целым числом от 1 до 6')
                continue
            try:
                self.shot(user_row, user_col, defense_board, atack_board)
            except Warning:
                print('Вы уже стреляли сюда')
                time.sleep(1)
                continue
            time.sleep(1)
            not_available = False
        
    def computer_motion(self, defense_board, atack_board):
        print('Ход противника')
        time.sleep(1)
        not_available = True
        while not_available:
            computer_row = rnd.randint(1,6)
            computer_col = rnd.randint(1,6)
            try:
                self.shot(computer_row, computer_col, defense_board, atack_board)
            except Warning:
                continue
            time.sleep(1)
            not_available = False
    
    def random_board_filler(self,size, board):
        try:
            board.ship_add(ShipFactory.create_ship(size, rnd.randint(1,6),rnd.randint(1,6), rnd.choice(self.list_directions)))
        except  ValueError:
            self.random_board_filler(size, board)

    def hand_board_filler(self,size, board, row, col, direction):
            board.ship_add(ShipFactory.create_ship(size, row, col, direction))

    def row_input(self):
        while True:
            try:
                row = int(input('Введите номер строки, соответствующей точке, в которую хотите поставить корабль \n '))
            except ValueError:
                print('Недопустимое значение. Значение должно быть целым числом от 1 до 6')
                continue
            break
        if not(0 < row < 7):
            raise IndexError('нет такой строки')
        else:
            return row
        
    def col_input(self):
        while True:
            try:
                col = int(input('Введите номер столбца, соответствующего точке, в которую хотите поставить корабль \n '))
            except ValueError:
                print('Недопустимое значение. Значение должно быть целым числом от 1 до 6')
                continue
            break
        if not(0 < col < 7):
            raise IndexError('нет такого столбца')
        else:
            return col
    
    def direction_input(self):
        direction = input('Введите строчными буквами направление, куда будет направлен корабль: "вниз", "вверх", "вправо", "влево" \n')
        if not(direction in self.list_directions ):
            raise IndexError('нет такого направления')
        else:
            return direction
        
    def data_input(self):
        while True:
            try:
                row = self.row_input()
            except IndexError:
                print('Нет строки с таким номером')
                continue
            break
        while True:
            try:
                col = self.col_input()
            except IndexError:
                print('Нет столбца с таким номером')
                continue
            break
        while True:
            try:
                direction = self.direction_input()
            except IndexError:
                print('Нет такого направления')
                continue
            break
        return (row, col, direction)
    
    def output(self, board1, board2):
        print(board1.name + 13*' ', board2.name)
        for i in range(8):
            print(*board1.curent_status[i], '  ', *board2.curent_status[i])
    
    def win_test(self, board):
        count = 0
        for i in board.curent_status:
            for j in i:
                if j == 'X|':
                    count += 1
        if count == sum(self.available_ships):
            return True
        else:
            return False
                
    

    
    def game_start(self):
        print(self.rules)
        time.sleep(1)
        computer_defence_board = GameBoard()
        computer_atack_board = GameBoard()
        user_defence_board = GameBoard('Ваша доска')
        user_atack_board = GameBoard('Доска противника')
        for i in self.available_ships:
            self.random_board_filler(i,computer_defence_board)
        while True:
            board_filling_choice = input('Хотите ли вы расставить корабли автоматически? Введите "да" или "нет" \n')
            if board_filling_choice == "да":
                for i in self.available_ships:
                    self.random_board_filler(i,user_defence_board)
                break
            elif board_filling_choice == "нет":
                print('Приступим к расстановке кораблей')
                time.sleep(1)
                ship_size_index = 0
                while ship_size_index <= 6:
                    time.sleep(1)
                    user_defence_board.board_output()
                    print(f'Разместите {self.available_ships[ship_size_index]}-палубный корабль')
                    time.sleep(1)
                    data = self.data_input()
                    try:
                        self.hand_board_filler(self.available_ships[ship_size_index], user_defence_board, data[0], data[1], data[2])
                    except ValueError:
                        print('невозможно поставить сюда корабль')
                        time.sleep(1)
                        continue
                    ship_size_index += 1
                break
            else:
                print('Неправильный ответ! Ответьте "да" или "нет"')
                continue
        print('Корабли расставлены!')
        time.sleep(1)
        game_loop = True
        while game_loop:
            self.output(user_defence_board, user_atack_board)
            self.user_motion(computer_defence_board, user_atack_board)
            marker = None
            if self.win_test(user_atack_board):
                while True:
                    test_reset =  input('Вы победили! Поздравляем, вы уничтожили флот противника! \n \
                                    Хотите начать заново? (Введите "да" или "нет") \n')
                    game_loop = False
                    if test_reset == "да":
                        self.game_start()
                        break
                    elif test_reset == "нет":
                        print('GAME OVER')
                        sys.exit(0)
                    else:
                        'Ответ не распознан! Введите "да" или "нет"'
                        continue
            if marker:
                break
            self.computer_motion(user_defence_board, computer_atack_board)
            if self.win_test(computer_atack_board):
                while True:
                    test_reset =  input('К сожалению, Вы проиграли! Ваш флот уничтожен противником! В следующий раз повезёт! \n \
                                    Хотите начать заново? (Введите "да" или "нет") \n')
                    game_loop = False
                    if test_reset == "да":
                        self.game_start()
                    elif test_reset == "нет":
                        print('GAME OVER')
                        sys.exit(0)
                    else:
                        'Ответ не распознан! Введите "да" или "нет"'
                        continue

Game = GameLogic()
Game.game_start()
