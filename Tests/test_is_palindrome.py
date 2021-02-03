from unittest import TestCase
from palindrome import is_palindrome


class TestIs_palindrome(TestCase):
  def test_is_palindrome(self):
    self.assertEqual(is_palindrome("racecar"), True)
  def test_is_palindrome_2(self):
    self.assertEqual(is_palindrome("Never odd or even"), True)
  def test_is_palindrome_Adding_Characters(self):
    self.assertEqual(is_palindrome("GNever odd or eveng"), True)
  def test_is_palindrome_End_Must_be_Lowercase(self):
    self.assertEqual(is_palindrome("GNever odd or evenG"), False)
