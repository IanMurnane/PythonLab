import unittest


class MyClass:
    def __init__(self, value):
        self.value = value

    def add(self, other_value):
        return self.value + other_value


class TestMyClass(unittest.TestCase):
    def test_add(self):
        my_class = MyClass(10)
        result = my_class.add(20)
        self.assertEqual(result, 30)

    def test_add_negative(self):
        my_class = MyClass(-10)
        result = my_class.add(-20)
        self.assertEqual(result, -30)


if __name__ == '__main__':
    unittest.main()
