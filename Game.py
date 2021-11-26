from AI_User import *
from Board import Board
from MyException import *
from Ship import Ship


class Game:
    def __init__(self):
        self.size = 6
        player_board = self.handle_board()
        ai_board = self.handle_board()

        self.ai = AI(ai_board, player_board)
        self.ai.add_targets(self.size)
        ai_board.hid = True
        self.player = User(player_board, ai_board)

    def initial_board(self):
        ships_length = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        quantity = 0
        for length in ships_length:
            while True:
                quantity += 1
                if quantity > 1000:
                    return None
                ship = Ship(Dot(randint(0, self.size - 1), randint(0, self.size - 1)), length,
                            'H' if randint(0, 1) else 'V')
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def handle_board(self):
        board = None
        while board is None:
            board = self.initial_board()
        return board

    def loop(self):
        self.render_field()
        while True:
            repeat = True
            while repeat:
                print('Ваш ход')
                repeat = self.player.move()
                self.render_field()
            if self.player.enemy.count == 7:
                print("Вы победили!!!")
                break
            repeat = True
            while repeat:
                print('Ход компьютера')
                repeat = self.ai.move()
                self.render_field()
            if self.ai.enemy.count == 7:
                print("Вы проиграли(((")
                break

    def render_field(self):
        print('Ваша гавань')
        print(self.player.board)
        print('Залив противника')
        print(self.ai.board)

    def greet(self):
        greet = """
            (*************************************)
            (**    Приветствую тебя на игре     **)
            (**          'Морской Бой'          **)
            (!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
            (** Стреляй по короблям противника, **)
            (**     вводя координаты точки.     **)
            (**     Первая это номер скоки      **)
            (**     Вторая - номер столбца      **)
            (**          У Д А Ч И !!!          **)
            (*************************************)
            """
        print(greet)

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
