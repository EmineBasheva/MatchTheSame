from ball import TypeBall, Ball
import random


class Board:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.all_positions = {
            (x, y): None for x in self.__width for y in self.__height
        }

    def __get_random_ball(self, position):
        colors = ["red", "blue", "green", "yellow", "orange", "pink"]
        rand_color = random.Choice(colors)
        return Ball(TypeBall.simple, rand_color, position)

    def fill(self):
        for position in self.all_positions:
            self.all_positions[position] = self.__get_random_ball(position)
