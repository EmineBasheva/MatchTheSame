from ball import TypeBall, Ball
import random


class Board:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.all_positions = list()
        # print("width, height: ", self.__width, self.__height)
        for i in range(0, self.__height):
            self.all_positions.append([])
            for j in range(0, self.__width):
                self.all_positions[i].append(None)

    def _is_not_valid_coords(self, x, y):
        return ((0 > x or x >= self.__height) 
                or (0 > y  or y >= self.__width))

    def __get_random_ball(self):
        colors = ["red", "blue", "green", "yellow", "orange", "pink"]
        rand_color = random.choice(colors)
        return Ball(TypeBall.simple, rand_color)

    def neighbours_for(self, position_x, position_y):
        neighbours = []
        neighbours_dx = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        for dx in neighbours_dx:
            coord_x = position_x + dx[0]
            coord_y = position_y + dx[1]
            if self._is_not_valid_coords(coord_x, coord_y):
                continue
            neighbours.append((coord_x, coord_y))

        return set(neighbours)

    def has_group(self):
        pass

    def _is_same(self, x_1, y_1, x_2, y_2):
        # try:
        if (self._is_not_valid_coords(x_1, y_1) or
            self._is_not_valid_coords(x_2, y_2)):
            return False
        return self.all_positions[x_1][y_1] == self.all_positions[x_2][y_2]
        # except Exception:
        #     print(self.all_positions)
        #     print("width, height: ", self.__width, self.__height)
        #     print(x_1, y_1, "---", x_2, y_2)

    def has_same_in_neighbours(self, current, neighbours):
        curr_x = current[0]
        curr_y = current[1]

        for neighbour in neighbours:
            neigh_x = neighbour[0]
            neigh_y = neighbour[1]
            if self._is_same(curr_x, curr_y, neigh_x, neigh_y): #all_positions[curr_x][curr_y] == self.all_positions[neigh_x][neigh_y]:
                return True

        return False

    def group_for(self, pos_x, pos_y):
        if self._is_not_valid_coords(pos_x, pos_y):
            return False
        group = set()
        group.add((pos_x, pos_y))
        passed = set()
        passed.add((pos_x, pos_y))
        neighbours = self.neighbours_for(pos_x, pos_y)
        all_coords = {
            (x, y) for x in range(0, self.__height) for y in range(0, self. __width)
        }
        # print("all_coords:", all_coords)
        while set(all_coords) != passed:

            if not self.has_same_in_neighbours((pos_x, pos_y), neighbours):
                break

            for neighbour in neighbours:
                x = neighbour[0]
                y = neighbour[1]

                if self._is_not_valid_coords(x, y):
                    continue

                if neighbour in passed:
                    continue
                # print("x, y: ", x, y, " --- pos_x, pos_y: ", pos_x, pos_y)
                if self._is_same(x, y, pos_x, pos_y): 
                        group.add((x, y))

                passed.add(neighbour)

            # old_neighbours = neighbours
            new_neighbours = set()
            same_neighbours = neighbours & group
            for neighbour in same_neighbours:
                x = neighbour[0]
                y = neighbour[1]

                if self._is_not_valid_coords(x, y):
                    continue

                neighbour_neighbours = self.neighbours_for(x, y)

                for neigh in neighbour_neighbours:
                    n_x, n_y = neigh
                    
                    if self._is_not_valid_coords(n_x, n_y):
                        continue
                    new_neighbours.add(neigh)

            # print("neighbours: ", neighbours)
            neighbours = new_neighbours.difference(passed)

        return group


    def fill(self):
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                # self.all_positions[i][j] = Ball(TypeBall.simple, 'red')
                self.all_positions[i][j] = self.__get_random_ball()
        # for position in self.all_positions:
        #     self.all_positions[position] = self.__get_random_ball(position)
        # if not self.has_group():
        #     rand_x = random.randint(0, self.__width - 1)
        #     rand_y = random.randint(0, self.__height - 1)
        #     rand_ball_position = rand_x, rand_y
        #     # part of neighbours to be same type if not special ball
