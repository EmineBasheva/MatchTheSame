import unittest
from board import Board
from ball import TypeBall, Ball


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.boarD = Board(8, 3)

    def test_start_all_positions(self):
        answer = [[None] * 8] * 3
        self.assertEqual(self.boarD.all_positions, answer)

    # def test_fill(self):
    #     self.boarD.fill()
    #     answer = [[Ball(TypeBall.simple, 'red')] * 8] * 3
    #     self.assertEqual(self.boarD.all_positions, answer)

    def test_neighbours_for(self):
        self.boarD.fill()
        neighbours = self.boarD.neighbours_for(5, 2)
        answer = [ (5, 1), (4, 2), (6, 2)]
        self.assertEqual(neighbours, set(answer))

    def test_neighbours_for_1_1(self):
        b = Board(5, 5)
        b.fill()
        neighbours = b.neighbours_for(1, 1)
        answer = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertEqual(neighbours, set(answer))


class BoardTestGroupFor(unittest.TestCase):

    def setUp(self):
        self.b = Board(4, 5)
        self.b.all_positions = [
            [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green'),
             Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'orange'),
             Ball(TypeBall.simple, 'yellow')], 
            [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'blue'),
             Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'pink'),
             Ball(TypeBall.simple, 'yellow')],
            [Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'blue'),
             Ball(TypeBall.simple, 'blue'), Ball(TypeBall.simple, 'yellow'),
             Ball(TypeBall.simple, 'yellow')],
            [Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'red'),
             Ball(TypeBall.simple, 'red'), Ball(TypeBall.simple, 'yellow'),
             Ball(TypeBall.simple, 'yellow')]
        ]

    def test_group_for_(self):
        group = self.b.group_for(3, 0)
        answer = {(3, 0), (2, 0), (3, 2), (3, 1)}
        self.assertEqual(group, answer)

if __name__ == '__main__':
    unittest.main()
