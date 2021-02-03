#import os,sys,inspect
#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(1,currentdir)
#sys.path.insert(0,parentdir)

from unittest import TestCase
from palindrome import is_palindrome
from Helpers import MakeSpreadSheet




class TestIs_palindrome(TestCase):
  #Positive Tests
  def test_is_palindrome(self):
    self.assertEqual(is_palindrome("racecar"), True)
  def test_is_palindrome_2(self):
    self.assertEqual(is_palindrome("Never odd or even"), True)
  def test_is_palindrome_Adding_Characters(self):
    self.assertEqual(is_palindrome("GNever odd or eveng"), True)
  def test_Remove_Spes_Characters_End(self):
    self.assertEqual(is_palindrome("Never odd or even123"), True)




  #Negative Tests
  def test_Non_Palindrome(self):
    self.assertEqual(is_palindrome("Never Even or odd"), False)

  #Should fail
  def test_End_Must_be_Lowercase(self):
    self.assertEqual(is_palindrome("GNever odd or evenG"), False)
  def test_Numbers(self):
      self.assertEqual(is_palindrome("11223eLe32211"), False)
  def test_Remove_Spes_Characters_Front_Not_Removed_Before(self):
    self.assertEqual(is_palindrome("123Never odd or even"), False)
  def test_Some_Strange_Behaviour(self):
    self.assertEqual(is_palindrome("N123ever odd or even"), True)


  #Adding an example with testcases from a file, increasing abstraction layer for addign test
  def test_Test_Cases_From_File(self):

    f = open('PalindromesToTest.txt', 'r')
    TestCasesForPalindromes = MakeSpreadSheet(f.read())
    for TestCaseForPalindrome in TestCasesForPalindromes:
      with self.subTest():
        self.assertEqual(is_palindrome(TestCaseForPalindrome[0]), TestCaseForPalindrome[1] == "True",TestCaseForPalindrome[0] + 'does not test: ' + TestCaseForPalindrome[1])
