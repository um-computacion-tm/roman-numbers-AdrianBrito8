import unittest
from Romano_Decimal import roman_decimal
from Num_Romanos import decimal_roman

class MyTest(unittest.TestCase):
    
    def test_simple(self):
        self.assertEqual(roman_decimal("I"), 1)
        self.assertEqual(roman_decimal("V"), 5)
        self.assertEqual(roman_decimal("X"), 10)
        self.assertEqual(roman_decimal("L"), 50)
        self.assertEqual(roman_decimal("C"), 100)
       
        self.assertEqual(roman_decimal("D"), 500)
        self.assertEqual(roman_decimal("M"), 1000)

    def test_suma(self):
        self.assertEqual(roman_decimal("II"), 2)
        self.assertEqual(roman_decimal("VI"), 6)
        self.assertEqual(roman_decimal("XIII"), 13)
        self.assertEqual(roman_decimal("LX"), 60)
        self.assertEqual(roman_decimal("MMXXI"), 2021)

    def test_1(self):

        resultado = decimal_roman(1)

        self.assertEqual(resultado,"I")

    def test_5(self):

        resultado = decimal_roman(5)

        self.assertEqual(resultado,"V")

    def test_10(self):

        resultado = decimal_roman(10)

        self.assertEqual(resultado,"X")


    def test_2(self):

        resultado = decimal_roman(2)

        self.assertEqual(resultado,"II")

    def test_3(self):

        resultado = decimal_roman(3)

        self.assertEqual(resultado,"III")

    def test_4(self):

        resultado = decimal_roman(4)

        self.assertEqual(resultado,"IV")

    def test_6(self):

        resultado = decimal_roman(6)

        self.assertEqual(resultado,"VI")

    def test_7(self):

        resultado = decimal_roman(7)

        self.assertEqual(resultado,"VII")

    def test_8(self):

        resultado = decimal_roman(8)

        self.assertEqual(resultado,"VIII")

    def test_34(self):

        resultado = decimal_roman(34)

        self.assertEqual(resultado,"XXXIV")

    def test_79(self):

        resultado = decimal_roman(79)

        self.assertEqual(resultado,"LXXIX")
    
    def test_559(self):

        resultado = decimal_roman(569)

        self.assertEqual(resultado,"DLXIX")

    def test_800(self):

        resultado = decimal_roman(800)

        self.assertEqual(resultado,"DCCC")

    def test_1000(self):

        resultado = decimal_roman(1000)

        self.assertEqual(resultado,"M")
    
if __name__ == '__main__':
    unittest.main()