from ball import TypeBall, Ball
import random
from settings import COLORS, MAX_TIME, DB_NAME, MULTICOLORED_FREQUENCY
from settings import BLACK_BALL_FREQUENCY, STAR_FREQUENCY, NUMBERED_BALL_FREQUENCY
import sqlite3


class Board:

    NAME = ''
    POINTS = 0
    TIME = MAX_TIME
    MULTICOLORED_INDEX = MULTICOLORED_FREQUENCY
    BLACK_BALL_INDEX = BLACK_BALL_FREQUENCY
    STAR_INDEX = STAR_FREQUENCY
    NUMBERED_BALL_INDEX = NUMBERED_BALL_FREQUENCY

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.all_positions = list()
        for i in range(0, self.__height):
            self.all_positions.append([])
            for j in range(0, self.__width):
                self.all_positions[i].append(None)

    def _is_not_valid_coords(self, x, y):
        return ((0 > x or x >= self.__height) 
                or (0 > y  or y >= self.__width))

    def __get_random_ball(self):
        rand_color = random.choice(COLORS)
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

    def has_group_for(self, x, y):
        return len(self.group_for(x, y)) > 2

    def has_group(self):
        all_coords = {
            (x, y) for x in range(0, self.__height) for y in range(0, self. __width)
        }
        for coord in all_coords:
            x, y = coord
            if self.has_group_for(x, y):
                return True
        return False

    def _is_same(self, x_1, y_1, x_2, y_2):
        if (self._is_not_valid_coords(x_1, y_1) or
            self._is_not_valid_coords(x_2, y_2)):
            return False
        return self.all_positions[x_1][y_1] == self.all_positions[x_2][y_2]

    def has_same_in_neighbours(self, current, neighbours):
        curr_x = current[0]
        curr_y = current[1]

        for neighbour in neighbours:
            neigh_x = neighbour[0]
            neigh_y = neighbour[1]
            if self._is_same(curr_x, curr_y, neigh_x, neigh_y): 
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

                if self._is_same(x, y, pos_x, pos_y): 
                        group.add((x, y))

                passed.add(neighbour)

            new_neighbours = set()
            same_neighbours = neighbours & group
            for neighbour in same_neighbours:
                x, y = neighbour

                if self._is_not_valid_coords(x, y):
                    continue

                neighbour_neighbours = self.neighbours_for(x, y)

                for neigh in neighbour_neighbours:
                    n_x, n_y = neigh
                    
                    if self._is_not_valid_coords(n_x, n_y):
                        continue
                    new_neighbours.add(neigh)

            neighbours = new_neighbours.difference(passed)

        return group

    def set_table_with_group(self):
        rand_x = random.randint(0, self.__height - 1)
        rand_y = random.randint(0, self.__width - 1)
        if self.all_positions[rand_x][rand_y].type_b() == TypeBall.simple:

            neighbours = self.neighbours_for(rand_x, rand_y)
            neighbours_number = random.randint(2, 4)

            for i in range(0, 3):
                if len(neighbours) > 0:
                    to_be_changed = neighbours.pop()
                    x, y = to_be_changed
                    if self.all_positions[x][y].type_b() == TypeBall.simple:
                        self.all_positions[x][y] = self.all_positions[rand_x][rand_y]
        else:
            return

    def fill(self):
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                self.all_positions[i][j] = self.__get_random_ball()

        if not self.has_group():
            self.set_table_with_group()

    def put_multicolored_ball(self):
        rand_x = random.randint(0, self.__height - 1)
        rand_y = random.randint(0, self.__width - 1)

        if self.all_positions[rand_x][rand_y].type_b() == TypeBall.simple:
            self.all_positions[rand_x][rand_y] = Ball(TypeBall.multicolored, "multicolored")
        else:
            return

        print('POINTS:', self.POINTS, "multicolored")

        if not self.has_group():
            self.set_table_with_group()

    def put_black_ball(self):
        rand_x = random.randint(0, self.__height - 1)
        rand_y = random.randint(0, self.__width - 1)

        if self.all_positions[rand_x][rand_y].type_b() == TypeBall.simple:
            self.all_positions[rand_x][rand_y] = Ball(TypeBall.black, "black")
        else:
            return

        print('POINTS:', self.POINTS, "black")

        if not self.has_group():
            self.set_table_with_group()

    def put_star(self):
        rand_x = random.randint(0, self.__height - 1)
        rand_y = random.randint(0, self.__width - 1)
        rand_color = random.choice(COLORS)

        if self.all_positions[rand_x][rand_y].type_b() == TypeBall.simple:
            self.all_positions[rand_x][rand_y] = Ball(TypeBall.star, rand_color)
        else:
            return

        print('POINTS:', self.POINTS, "star")

        if not self.has_group():
            self.set_table_with_group()

    def put_numbered_ball(self):
        rand_x = random.randint(0, self.__height - 1)
        rand_y = random.randint(0, self.__width - 1)
        rand_number = random.randint(1, MAX_TIME)

        if self.all_positions[rand_x][rand_y].type_b() == TypeBall.simple:
            self.all_positions[rand_x][rand_y] = Ball(TypeBall.numbered, str(rand_number))
        else:
            return

        print('POINTS:', self.POINTS, "star")

        if not self.has_group():
            self.set_table_with_group()

    def kill_group(self, group):
        self.POINTS += len(group)
        self.TIME = min(self.TIME + 2, MAX_TIME)

        for elem in group:
            x_elem, y_elem = elem
            self.all_positions[x_elem][y_elem] = None

        for i in range(self.__height - 1, -1, -1):
            for j in range(self.__width - 1, -1, -1):
                if self.all_positions[i][j] is None and i > 0:
                    k = 1
                    while self.all_positions[i][j] is None and (i - k > -1):
                        self.all_positions[i][j] = self.all_positions[i - k][j]
                        k += 1
                        if i - k <= -1:
                            break

                    self.all_positions[i - k + 1][j] = None

        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if self.all_positions[i][j] is None:
                    self.all_positions[i][j] = self.__get_random_ball()

        if not self.has_group():
            self.set_table_with_group()

    def kill_group_sample_balls_for(self, x, y):
        if self._is_not_valid_coords(x, y):
            return False

        if len(self.group_for(x, y)) < 3:
            self.TIME -= 1
            return

        group = self.group_for(x, y)

        self.kill_group(group)

        # add multicolored ball
        if self.POINTS > self.MULTICOLORED_INDEX:
            self.put_multicolored_ball()
            print("MULTICOLORED_INDEX:", self.MULTICOLORED_INDEX)
            self.MULTICOLORED_INDEX += MULTICOLORED_FREQUENCY

        # add black ball
        if self.POINTS > self.BLACK_BALL_INDEX:
            self.put_black_ball()
            print("BLACK_BALL_INDEX:", self.BLACK_BALL_INDEX)
            self.BLACK_BALL_INDEX += BLACK_BALL_FREQUENCY

        # add star
        if self.POINTS > self.STAR_INDEX:
            self.put_star()
            print("STAR_INDEX:", self.STAR_INDEX)
            self.STAR_INDEX += STAR_FREQUENCY

        # add numbered ball
        if self.POINTS > self.NUMBERED_BALL_INDEX:
            self.put_numbered_ball()
            print("NUMBERED_BALL_INDEX:", self.NUMBERED_BALL_INDEX)
            self.NUMBERED_BALL_INDEX += NUMBERED_BALL_FREQUENCY

    def kill_group_for_multicolored_for(self, x, y):
        if self._is_not_valid_coords(x, y):
            return False

        neighbours = self.neighbours_for(x, y)

        group = neighbours
        group.add((x, y))

        self.kill_group(group)

    def kill_group_for_black_ball_for(self, x, y):
        if self._is_not_valid_coords(x, y):
            return False

        neighbours = self.neighbours_for(x, y)

        group = neighbours
        group.add((x, y))

        self.POINTS -= len(group)

        self.kill_group(group)

    def kill_group_for_star_for(self, x, y):
        if self._is_not_valid_coords(x, y):
            return False

        group = {(x, y)}

        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if (self.all_positions[i][j].color() == 
                    self.all_positions[x][y].color()):
                    group.add((i, j))

        self.kill_group(group)

    def kill_numbered_ball_for(self, x, y):
        if self._is_not_valid_coords(x, y):
            return False

        group = {(x, y)}
        bonus = int(self.all_positions[x][y].color())
        self.TIME = min(self.TIME + bonus, MAX_TIME)

        self.kill_group(group)

    def kill_the_group_for(self, x, y):
        if self.all_positions[x][y].type_b() == TypeBall.simple:
            self.kill_group_sample_balls_for(x, y)

        elif self.all_positions[x][y].type_b() == TypeBall.multicolored:
            self.kill_group_for_multicolored_for(x, y)

        elif self.all_positions[x][y].type_b() == TypeBall.black:
            self.kill_group_for_black_ball_for(x, y)

        elif self.all_positions[x][y].type_b() == TypeBall.star:
            self.kill_group_for_star_for(x, y)

        elif self.all_positions[x][y].type_b() == TypeBall.numbered:
            self.kill_numbered_ball_for(x, y)

    def save_classification(self):
        insert_sql = """
            INSERT INTO Classification(name, points, board_width, board_height)
            VALUES (?, ?, ?, ?)
        """
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(insert_sql, (
            self.NAME, self.POINTS, self.__width, self.__height))
        conn.commit()

    def classification(self):
        get_classification_by_width_height = """
            SELECT id, name, points
            FROM Classification
            WHERE board_width = ?
                AND board_height = ?
            ORDER BY points DESC
            LIMIT 5;
        """
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        result = cursor.execute(get_classification_by_width_height, (
            self.__width, self.__height))
        
        return result.fetchall()
