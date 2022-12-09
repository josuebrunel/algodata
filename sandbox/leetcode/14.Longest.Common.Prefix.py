import unittest


def longest_common_prefix(strs):
    shortest = strs[0]
    for s in strs:
        if len(s) < len(shortest):
            shortest = s

    for i in range(len(shortest)):
        for j in range(len(strs)):
            if strs[j][i] != shortest[i]:
                return shortest[:i]
    return shortest


class LongestCommonPrefix(unittest.TestCase):

    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]),
                         "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")


if __name__ == "__main__":
    unittest.main()
