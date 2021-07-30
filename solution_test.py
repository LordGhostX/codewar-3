import unittest
import solution


class MyTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual((0, 1), solution.solution([1, 2, 3, 4, 5], 3))


if __name__ == '__main__':
    unittest.main()
