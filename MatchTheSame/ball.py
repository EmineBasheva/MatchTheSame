from enum import Enum


class TypeBall(Enum):
    simple = "simple"
    multicolored = "multicolored"
    black = "black"
    star = "star"
    numbered = "numbered"


class Ball:
    def __init__(self, type_ball, color, position):
        self.__color = color
        self.__position = position
        self.__type = type_ball

    def type_b(self):
        return self.__type

    def color(self):
        return self.__color

    def position(self):
        return self.__position

    def move_to(self, new_position):
        self.__position = new_position

    def __str__(self):
        return "{} ball".format(self.__color)
