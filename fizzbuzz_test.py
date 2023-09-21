import unittest

class TestCalc(unittest.TestCase):

    def test_is_FizzBuzz(self):
        for i in range(0, 101):
            print("Fizzbuzz")
            self.assertEqual(i % 5 and i % 3, 0)

if __name__ == "__main__":
    unittest.main()
