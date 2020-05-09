# Assertions
# accepts an expression and returns None if truthy or AssertionError if fasley
# A Python file run with a -O flag it will ignroe all the assertion statements

def add_positive_numbers(x,y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

# Doctests
# can write tests for functions inside of the docstring
# write code that looks like it's inside of a REPL
# To run: python -m doctest -v <filename>.py
def add(x,y):
    """ add together x and y

    >>> add(1,2)
    3

    >>> add(8, "hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y

# Unit Testing
# unittest
import unittest
# import functions to test (tests should be in seperate file.)

class ActivityTests(unittest.TestCase):
    def setUp(self):
        #do setup here
        pass
    
    def test_add(self):
        """Test function for add() method"""
        self.assertEqual(add(1, 1), 2, "Wrong answer")
        self.assertEqual(add(10, 1), 11, "Wrong answer")
        self.assertEqual(add(15, 15), 30, "Wrong answer")
    
    def tearDown(self):
        #do tear down here
        pass

#BEFORE and AFTER hooks
"""
setUp - runs before each test method
tearDown - runs after each test method
"""


if __name__ == "__main__":
    unittest.main()
