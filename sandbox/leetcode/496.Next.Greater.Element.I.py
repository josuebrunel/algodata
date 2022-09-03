import unittest


def next_greater_element(nums1, nums2):
    nums1idx = {n: i for i, n in enumerate(nums1)}
    stack = []
    ans = [-1] * len(nums1)

    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and stack[-1] < cur:
            val = stack.pop()
            idx = nums1idx[val]
            ans[idx] = cur
        if cur not in nums1idx:
            continue
        stack.append(cur)

    return ans


class NextGreaterElementTest(unittest.TestCase):

    def test_next_greater_element(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]),
                         [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])


if __name__ == "__main__":
    unittest.main()
