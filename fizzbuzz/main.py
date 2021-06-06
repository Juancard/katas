"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print “Fizz” instead of the number and for the multiples of five print
“Buzz”. For numbers which are multiples of both three and five print “FizzBuzz
“.
"""


class FizzBuzz:
    __fizz = "Fizz"
    __buzz = "Buzz"

    def get_string_for(self, numero: int) -> str:
        out = ""
        if self.__es_fizz(numero):
            out += self.__fizz
        if self.__es_buzz(numero):
            out += self.__buzz
        return out or str(numero)

    def __es_fizz(self, numero: int):
        return self.__es_multiplo_de(
            numero, 3) or self.__contiene_un(numero, "3")

    def __es_buzz(self, numero: int):
        return self.__es_multiplo_de(numero, 5) or self.__contiene_un(numero, "5")

    def __es_multiplo_de(self, numero: int, n: int):
        if numero == 0:
            return 0
        return numero % n == 0

    def __contiene_un(self, numero: int, n: str):
        return n in str(numero)


class FizzBuzzPrinter:
    separator = "\n"

    def __init__(self, fizzBuzz: FizzBuzz):
        self.fizzBuzz = fizzBuzz

    def get_string(self, from_: int, to: int) -> str:
        out = ""
        for i in range(from_, to+1):
            out += self.fizzBuzz.get_string_for(i)
            if i < to:
                out += self.separator
        return out
