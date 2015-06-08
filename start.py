import sys
from board import Board


def main():
    if len(sys.argv) <= 1:
        print("Write username :)")
        print("python3 start.py 'your_username'")
        sys.exit(1)

    username = sys.argv[1]
    the_board = Board(10, 10)
    the_board.fill()



if __name__ == '__main__':
    main()
