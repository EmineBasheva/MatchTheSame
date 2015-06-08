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

    def has_group(self):
        pass

    def neighbours_of(self, ball):
        pass

    def has_group_for(self, ball):
        pass

    def group_for(self, ball):
        if self.has_group_for(ball):
            pass

        return False

    def fill(self):
        while not self.has_group():
            for position in self.all_positions:
                self.all_positions[position] = self.__get_random_ball(position)

