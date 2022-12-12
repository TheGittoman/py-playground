import unittest

from src import main


class test_func(unittest.TestCase):
    def test_func(self):
        self.assertEqual(main.func(1), 0)
        self.assertEqual(main.func(2), 1)
        self.assertEqual(main.func(66), 1)

    def test_number(self):
        self.assertEqual(main.number(), 10)


if __name__ == "__main__":
    unittest.main()
