import unittest


def roman_to_integer(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    length = len(s)
    for i in range(length):
        if i + 1 < length and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]

    return res


class RomanToIntegerTest(unittest.TestCase):
    def roman_to_integer(self):
        self.assertEqual(roman_to_integer("III"), 3)
        self.assertEqual(roman_to_integer("LVIII"), 58)
        self.assertEqual(roman_to_integer("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
