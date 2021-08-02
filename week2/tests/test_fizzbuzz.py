# Source where I learned how to implement unittest libraries
# https://www.blog.pythonlibrary.org/2019/09/18/python-code-kata-fizzbuzz/

import fizzbuzz
import unittest

# Setting up Test Class
class TestFizzBuzz(unittest.TestCase):

    # For input of 1
    def test_get_one(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(1), 'Get 1')

    # For input of 2
    def test_get_two(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(2), 'Get 2')

    # For input of 3
    def test_num_is_three(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(3), 'Fizz')

    # For input of 5
    def test_num_is_five(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(5), 'Buzz')

    # For input that is a multiple of 3
    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(6), 'Fizz')

    # For input that is a multiple of 5
    def test_multiple_of_5(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(10), 'Buzz')

    # For input that is a multiple of 3 and 5
    def test_multiple_of_three_and_five(self):
        self.assertEqual(fizzbuzz.test_fizzbuzz(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()