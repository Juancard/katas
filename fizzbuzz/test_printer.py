from unittest import TestCase, mock
from main import FizzBuzz, FizzBuzzPrinter


class TestFizzBuzzPrinterClassist(TestCase):
    separator = "\n"
    fizz = "Fizz"
    buzz = "Buzz"
    fizz_buzz = fizz + buzz

    def setUp(self) -> None:
        self.fizzBuzzPrinter = FizzBuzzPrinter(FizzBuzz())

    def test_given_1_to_1_return_1(self):
        string = self.fizzBuzzPrinter.get_string(1, 1)
        self.assertEqual(string, "1")

    def test_given_1_to_2_return_1_and_2(self):
        string = self.fizzBuzzPrinter.get_string(1, 2)
        expected_string = "{}{}{}".format(1, self.separator, 2)
        self.assertEqual(string, expected_string)

    def test_given_0_to_2_return_0_1_and_2(self):
        string = self.fizzBuzzPrinter.get_string(0, 2)
        expected_string = "{}{}{}{}{}".format(
            0, self.separator, 1, self.separator, 2)
        self.assertEqual(string, expected_string)

    def test_given_1_to_3_return_1_2_and_fizz(self):
        string = self.fizzBuzzPrinter.get_string(1, 3)
        expected_string = "{}{}{}{}{}".format(
            1, self.separator, 2, self.separator, self.fizz)
        self.assertEqual(string, expected_string)

    def test_given_10_to_15_returns_numbers_fizz_buzz_and_fizzbuzz(self):
        string = self.fizzBuzzPrinter.get_string(10, 15)
        expected_string = "{}{}{}{}{}{}{}{}{}{}{}".format(self.buzz, self.separator, 11, self.separator,
                                                          self.fizz, self.separator, 13, self.separator,
                                                          14, self.separator, self.fizz_buzz)
        self.assertEqual(string, expected_string)
