import unittest
import string


def convert_to_title(n):
    match = {}
    for i, l in enumerate(string.ascii_uppercase):
        match[i] = l
    ans = []

    while n:
        p = (n - 1) % 26
        ans.append(match[p])
        n = (n - 1) // 26

    return "".join(ans[::-1])


class ExcelSheetColumnTitle(unittest.TestCase):

    def test_convert_to_title(self):
        self.assertEqual(convert_to_title(1), "A")
        self.assertEqual(convert_to_title(28), "AB")
        self.assertEqual(convert_to_title(701), "ZY")


if __name__ == "__main__":
    unittest.main()
