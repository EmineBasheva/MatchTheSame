import unittest
from board import Board
from ball import TypeBall, Ball


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.boarD = Board(8, 3)

    def test_start_all_positions(self):
        answer = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
        self.assertEqual(self.boarD.all_positions, answer)

    def test_fill(self):
        self.boarD.fill()
        answer = len([[Ball(TypeBall.simple, 'red')] * 8] * 3)
        self.assertEqual(len(self.boarD.all_positions), answer)

    def test_fill_in(self):
        self.boarD.fill()
        answer = len(([[Ball(TypeBall.simple, 'red')] * 8] * 3)[1])
        self.assertEqual(len(self.boarD.all_positions[0]), answer)

    def test_is_not_valid_coords_False(self):
        self.assertFalse(self.boarD._is_not_valid_coords(2, 7))

    def test_is_not_valid_coords_True(self):
        self.assertTrue(self.boarD._is_not_valid_coords(7, 2))

    def test_neighbours_for(self):
        self.boarD.fill()
        neighbours = self.boarD.neighbours_for(2, 5)
        answer = [ (1, 5), (2, 4), (2, 6)]
        self.assertEqual(neighbours, set(answer))

    def test_neighbours_for_1_1(self):
        b = Board(5, 5)
        b.fill()
        neighbours = b.neighbours_for(1, 1)
        answer = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertEqual(neighbours, set(answer))

    def test_neighbours_for_2_2(self):
        b = Board(4, 3)
        b.fill()
        neighbours = b.neighbours_for(2, 2)
        answer = {(1, 2), (2, 1), (2, 3)}
        self.assertEqual(neighbours, answer)


class BoardTestGroupFor(unittest.TestCase):

    def setUp(self):
        self.b = Board(5, 4)
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

    def test_type_of_same_balls(self):
        self.assertEqual(self.b.all_positions[0][0].type_b(), 
                        self.b.all_positions[0][1].type_b())

    def test_type_for_sample(self):
        print(self.b.all_positions[0][0].type_b())
        self.assertEqual(self.b.all_positions[0][0].type_b(),
                        TypeBall.simple)

    def test_is_same_3_3_and_2_3(self):
        self.assertTrue(self.b._is_same(3, 3, 2, 3))

    def test_has_same_in_neighbours_3_0(self):
        neighbours = self.b.neighbours_for(3, 0)
        self.assertTrue(self.b.has_same_in_neighbours((3, 0), neighbours))

    def test_has_same_in_neighbours_3_0_False(self):
        neighbours = {(1, 0), (2, 1), (2, 2), (2, 3), (3, 3)}
        self.assertFalse(self.b.has_same_in_neighbours((3, 0), neighbours))

    def test_has_same_in_neighbours_2_1(self):
        neighbours = self.b.neighbours_for(2, 1)
        self.assertTrue(self.b.has_same_in_neighbours((2, 1), neighbours))

    def test_has_same_in_neighbours_2_1_False(self):
        neighbours = {(1, 0), (0, 1), (1, 2), (2, 3)}
        self.assertFalse(self.b.has_same_in_neighbours((2, 1), neighbours))

    def test_has_same_in_neighbours_1_2(self):
        neighbours = self.b.neighbours_for(1, 2)
        self.assertFalse(self.b.has_same_in_neighbours((1, 2), neighbours))

    def test_has_same_in_neighbours_1_2_True(self):
        neighbours = {(0, 1), (0, 2), (1, 3), (2, 2)}
        self.assertTrue(self.b.has_same_in_neighbours((1, 2), neighbours))

    def test_group_for_3_0(self):
        group = self.b.group_for(3, 0)
        answer = {(3, 0), (2, 0), (3, 2), (3, 1)}
        self.assertEqual(group, answer)

    def test_gorup_for_3_3(self):
        group = self.b.group_for(3, 3)
        answer = {(3, 3), (3, 4), (2, 3), (2, 4), (1, 4), (0, 4)}
        self.assertEqual(group, answer)

    def test_gorup_for_2_2(self):
        group = self.b.group_for(2, 2)
        answer = {(2, 2), (2, 1), (1, 1)}
        self.assertEqual(group, answer)

    def test_gorup_for_1_2(self):
        group = self.b.group_for(1, 2)
        answer = {(1, 2)}
        self.assertEqual(group, answer)

    def test_gorup_for_1_3(self):
        group = self.b.group_for(1, 3)
        answer = {(1, 3)}
        self.assertEqual(group, answer)

    def test_gorup_for_0_0(self):
        group = self.b.group_for(0, 0)
        answer = {(0, 0), (0, 1), (1, 0)}
        self.assertEqual(group, answer)

    def test_gorup_for_0_2(self):
        group = self.b.group_for(0, 2)
        answer = {(0, 2), (0, 3)}
        self.assertEqual(group, answer)

    def test_has_group_for_2_0_True(self):
        self.assertTrue(self.b.has_group_for(2, 0))

    def test_has_group_for_1_2_False(self):
        self.assertFalse(self.b.has_group_for(1, 2))

    def test_has_group_big(self):
        self.assertTrue(self.b.has_group())


class BoardTestAlone(unittest.TestCase):

    def test_for_board_2_3(self):
        b = Board(2, 3)
        b.all_positions = [
            [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green')],
            [Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'orange')],
            [Ball(TypeBall.simple, 'yellow'), Ball(TypeBall.simple, 'green')]
        ]
        group = b.group_for(0, 0)
        answer = {(0, 0), (0, 1)}
        self.assertEqual(group, answer)

    def test_has_group_False(self):
        b = Board(2, 3)
        b.all_positions = [
            [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green')],
            [Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'orange')],
            [Ball(TypeBall.simple, 'yellow'), Ball(TypeBall.simple, 'green')]
        ]
        self.assertFalse(b.has_group())

    def test_set_table_with_group(self):
        b = Board(2, 3)
        b.all_positions = [
            [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green')],
            [Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'orange')],
            [Ball(TypeBall.simple, 'yellow'), Ball(TypeBall.simple, 'green')]
        ]
        b.set_table_with_group()
        self.assertTrue(b.has_group())

    def test_kill_the_group_for_without_None(self):
        b = Board(2, 3)
        b.all_positions = [
            [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green')],
            [Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'green')],
            [Ball(TypeBall.simple, 'yellow'), Ball(TypeBall.simple, 'green')]
        ]
        b.kill_the_group_for(0, 1)
        count_None = 0
        for row in b.all_positions:
            for elem in row:
                if elem is None:
                    count_None += 1

        self.assertEqual(count_None, 0)

    # def test_kill_the_group_for(self):
    #     b = Board(2, 3)
    #     b.all_positions = [
    #         [Ball(TypeBall.simple, 'green'), Ball(TypeBall.simple, 'green')],
    #         [Ball(TypeBall.simple, 'orange'), Ball(TypeBall.simple, 'green')],
    #         [Ball(TypeBall.simple, 'yellow'), Ball(TypeBall.simple, 'green')]
    #     ]
    #     b.kill_the_group_for(0, 1)
    #     self.assertTrue(b.all_positions[1][0] == Ball(TypeBall.simple, 'orange') and
    #         b.all_positions[2][0] == Ball(TypeBall.simple, 'yellow'))


if __name__ == '__main__':
    unittest.main()
