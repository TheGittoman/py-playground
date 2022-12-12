import unittest

# import main from the .src folder
from src import main


class test_func(unittest.TestCase):
    # test isEven function and assert if the answer is incorrect
    def test_isEven(self):
        self.assertEqual(main.isEven(1), 0)
        self.assertEqual(main.isEven(2), 1)
        self.assertEqual(main.isEven(66), 1)
        self.assertEqual(main.isEven(55), 0)


if __name__ == "__main__":
    # required for unittest to run the tests correctly
    unittest.main()
