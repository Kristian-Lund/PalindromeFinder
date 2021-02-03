from unittest import TestCase
from palindrome import is_palindrome


class TestIs_palindrome(TestCase):
  def test_is_palindrome(self):
    self.assertEqual(is_palindrome("racecar"), True)
  def test_is_palindrome_2(self):
    self.assertEqual(is_palindrome("Never odd or even"), True)
  def test_is_palindrome_3(self):
    self.assertEqual(is_palindrome("GGNever odd or even"), True)

