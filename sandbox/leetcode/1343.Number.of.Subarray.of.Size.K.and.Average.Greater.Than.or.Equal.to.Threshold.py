import unittest


def numberOfSubarray(array, k, threshold):
    if not array:
        return 0

    curSum = sum(array[:k - 1])
    res = 0

    for i in range(k - 1, len(array)):
        curSum += array[i]
        if curSum / k >= threshold:
            res += 1
        curSum -= array[i - k + 1]

    return res


class NumberOfSubarrayOfSizeKAndAvgGTEThreshold(unittest.TestCase):

    def test_number_of_subarray(self):
        self.assertEqual(numberOfSubarray([2, 2, 2, 2, 5, 5, 5, 8], 3, 4), 3)
        self.assertEqual(
            numberOfSubarray([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5), 6)


if __name__ == "__main__":
    unittest.main()
