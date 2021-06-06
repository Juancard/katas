"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print “Fizz” instead of the number and for the multiples of five print
“Buzz”. For numbers which are multiples of both three and five print “FizzBuzz
“.
Stage 2 - new requirements
 * A number is fizz if it is divisible by 3 or if it has a 3 in it
 * A number is buzz if it is divisible by 5 or if it has a 5 in it
"""

from unittest import TestCase, mock
from main import FizzBuzz, FizzBuzzPrinter


class TestFizzBuzz(TestCase):
    fizz = "Fizz"
    buzz = "Buzz"
    fizz_buzz = fizz + buzz

    def setUp(self) -> None:
        self.fizzBuzz = FizzBuzz()

    def test_given_1_return_1(self):
        string = self.fizzBuzz.get_string_for("1")
        self.assertEqual(string, "1")

    def test_given_2_return_2(self):
        string = self.fizzBuzz.get_string_for("2")
        self.assertEqual(string, "2")

    def test_given_3_return_fizz(self):
        string = self.fizzBuzz.get_string_for("3")
        self.assertEqual(string, self.fizz)

    def test_given_5_return_fizz(self):
        string = self.fizzBuzz.get_string_for("5")
        self.assertEqual(string, self.buzz)

    def test_given_6_return_fizz(self):
        string = self.fizzBuzz.get_string_for("6")
        self.assertEqual(string, self.fizz)

    def test_given_10_return_buzz(self):
        string = self.fizzBuzz.get_string_for("10")
        self.assertEqual(string, self.buzz)

    def test_given_15_return_fizzbuzz(self):
        string = self.fizzBuzz.get_string_for("15")
        self.assertEqual(string, self.fizz_buzz)

    def test_given_13_return_fizz(self):
        string = self.fizzBuzz.get_string_for("13")
        self.assertEqual(string, self.fizz)

    def test_given_52_return_buzz(self):
        string = self.fizzBuzz.get_string_for("52")
        self.assertEqual(string, self.buzz)
