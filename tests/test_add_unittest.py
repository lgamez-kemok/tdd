import unittest

from my_app import add
from unittest.mock import patch


class TestAdd(unittest.TestCase):
    @patch('my_app.add', return_value=6)
    def test_add_integer_list(self, add):
        """
        Probar que la función suma números enteros
        """
        data = [1, 2, 3]
        result = add(data)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
