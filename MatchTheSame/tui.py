from board import Board
from ball import TypeBall, Ball
from termcolor import colored


symbol_for_color = {
    "red": 'X',
    "blue": 'O',
    "green": '@',
    "yellow": '#',
    "cyan": 'Ж',
    "magenta": 'Ф',
    "multicolored": '©',
    "black": 'ᚍ',
    "star": '♦'
    # "numbered": ''
}


def print_board(board):
    if not isinstance(board, Board):
        return False

    for i in range(0, len(board.all_positions)):
        row = []
        for j in range(0, len(board.all_positions[0])):
            if board.all_positions[i][j].type_b() == TypeBall.simple:
                symbol = symbol_for_color[board.all_positions[i][j].color()]
                color = board.all_positions[i][j].color()
                row.append(colored(symbol, color))

            elif board.all_positions[i][j].type_b() == TypeBall.multicolored:
                symbol = symbol_for_color["multicolored"]
                row.append(colored(symbol, "white"))

            elif board.all_positions[i][j].type_b() == TypeBall.black:
                symbol = symbol_for_color["black"]
                row.append(colored(symbol, "white", "on_white"))

            elif board.all_positions[i][j].type_b() == TypeBall.star:
                symbol = symbol_for_color["star"]
                color = board.all_positions[i][j].color()
                row.append(colored(symbol, color))

            elif board.all_positions[i][j].type_b() == TypeBall.numbered:
                symbol = board.all_positions[i][j].color()
                row.append(colored(symbol, "white"))
        print(' '*20, ' '.join(row))


def main():
    width = input("Enter WIDTH for your board >> ")
    height = input("Enter HEIGHT for your board >> ")
    boarD = Board(int(width), int(height))
    boarD.NAME = input("Enter your name >> ")
    boarD.fill()

    while boarD.TIME > 0:
        print_board(boarD)
        x = input("enter X > ")
        y = input("enter Y > ")
        if "exit" in (x, y):
            break
        boarD.kill_the_group_for(int(x), int(y))
        boarD.TIME -= 1
        print(boarD.NAME + ": ", boarD.POINTS, "[ time:", boarD.TIME, "]")

    boarD.save_classification()
    print(' '*10, "END OF GAME!!!")
    print("Points:", boarD.POINTS)
    classification = boarD.classification()
    count = 1
    for elem in classification:
        id, name, points = elem
        print(count, "|", name, "|", points)
        count += 1

    # boarD = Board(7, 4)
    # boarD.fill()
    # # boarD.all_positions = [
    # #         [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green'),
    # #          Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'orange'),
    # #          Ball(TypeBall.simple, 'yellow')], 
    # #         [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'blue'),
    # #          Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'pink'),
    # #          Ball(TypeBall.simple, 'yellow')],
    # #         [Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'blue'),
    # #          Ball(TypeBall.simple, 'blue'), Ball(TypeBall.simple, 'yellow'),
    # #          Ball(TypeBall.simple, 'yellow')],
    # #         [Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'red'),
    # #          Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'yellow'),
    # #          Ball(TypeBall.simple, 'yellow')]
    # #     ]
    # print_board(boarD)

    # x = input("enter X > ")
    # y = input("enter Y > ")

    # print(boarD.group_for(int(x), int(y)))
    # print(boarD.has_group_for(int(x), int(y)))
    # print(symbol_for_color[boarD.all_positions[int(x)][int(y)].color()])


if __name__ == '__main__':
    main()
