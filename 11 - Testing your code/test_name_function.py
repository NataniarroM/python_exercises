import unittest
from name_function import get_formatted_number

class NameTestCase(unittest.TestCase):
    "Tests for name_function.py"

    def test_first_last_name(self):
        "Do names like 'Frank Miller' work?"
        formatted_number = get_formatted_number('frank', 'miller')
        self.assertEqual(formatted_number, "Frank Miller")

    def test_first_middle_last_name(self):
        "Do names like 'Thomas Stearns Eliot' work?"
        formmatted_number = get_formatted_number("thomas", "eliot", "stearns")
        self.assertEqual(formmatted_number, "Thomas Stearns Eliot")

unittest.main()