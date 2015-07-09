from board import Board
from ball import TypeBall, Ball


symbol_for_color = {
    "red": 'X',
    "blue": 'O',
    "green": '@',
    "yellow": '#',
    "orange": 'Ж',
    "pink": 'Ф'
}


def print_board(board):
    if not isinstance(board, Board):
        return False

    for i in range(0, len(board.all_positions)):
        row = []
        for j in range(0, len(board.all_positions[0])):
            row.append(symbol_for_color[board.all_positions[i][j].color()])
        print(' '.join(row))


def main():
    
    boarD = Board(4, 5)
    boarD.fill()
    # boarD.all_positions = [
    #         [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green'),
    #          Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'orange'),
    #          Ball(TypeBall.simple, 'yellow')], 
    #         [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'blue'),
    #          Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'pink'),
    #          Ball(TypeBall.simple, 'yellow')],
    #         [Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'blue'),
    #          Ball(TypeBall.simple, 'blue'), Ball(TypeBall.simple, 'yellow'),
    #          Ball(TypeBall.simple, 'yellow')],
    #         [Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'red'),
    #          Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'yellow'),
    #          Ball(TypeBall.simple, 'yellow')]
    #     ]
    print_board(boarD)

    x = input("enter X > ")
    y = input("enter Y > ")

    print(boarD.group_for(int(x), int(y)))
    print(symbol_for_color[boarD.all_positions[int(x)][int(y)].color()])


if __name__ == '__main__':
    main()
