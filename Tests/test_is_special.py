from unittest import TestCase
from palindrome import is_special

class TestIs_special(TestCase):
    def test_is_not_special_A(self):
        self.assertEqual(is_special('A'), False)
    def test_is_not_special_Æ(self):
        self.assertEqual(is_special('Æ'), True)

