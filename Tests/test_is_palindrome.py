import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1,currentdir)
sys.path.insert(0,parentdir)

from unittest import TestCase
from palindrome import is_palindrome
from Helpers import MakeSpreadSheet




class TestIs_palindrome(TestCase):
  #Positive Tests
  def test_Simple_palindrome(self):
    self.assertEqual(is_palindrome("racecar"), True)
  def test_Sentence_palindrome(self):
    self.assertEqual(is_palindrome("Never odd or even"), True)
  def test_is_palindrome_Adding_Characters(self):#Equivalent partition
    self.assertEqual(is_palindrome("GNever odd or eveng"), True)
  def test_Remove_Spes_Characters_End(self):
    self.assertEqual(is_palindrome("Never odd or even."), True)
  def test_Spes_Character_Early(self):
    self.assertEqual(is_palindrome("Agnes, i senga"), True)
  def test_Spes_Character_Late(self):
    self.assertEqual(is_palindrome("Agnes i ,senga"), True)

  #The following should be true
  def test_End_Must_be_Lowercase(self):
    self.assertEqual(is_palindrome("NEVER ODD OR EVEN"), False)
  def test_Numbers(self):
    self.assertEqual(is_palindrome("11223eLe32211"), False)
  def test_Remove_Spes_Characters_Front(self):
    self.assertEqual(is_palindrome(" Never odd or even"), False)

  #Negative Tests
  def test_Non_Palindrome(self):
    self.assertEqual(is_palindrome("Never Even or odd"), False)
  # The following should be false
  def test_Some_Strange_Behaviour(self):
    self.assertEqual(is_palindrome("N123ever odd or even"), True)


  #Adding an example with testcases from a file, increasing abstraction layer for adding test

  def test_Test_Cases_From_File(self):
    print('Hei')
    print(currentdir)
    print(os.listdir())
    f = open('PalindromesToTest.txt', 'r')
    TestCasesForPalindromes = MakeSpreadSheet(f.read())
    f.close()
    for TestCaseForPalindrome in TestCasesForPalindromes:
      with self.subTest():
        self.assertEqual(is_palindrome(TestCaseForPalindrome[0]), TestCaseForPalindrome[1].lower() == "true", '---' + TestCaseForPalindrome[0] + '--- does not test: ---' + TestCaseForPalindrome[1]+'---')
