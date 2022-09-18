import unittest


def increasing_mono_stack(nums):
    stack = []

    for i in range(len(nums)):
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        stack.append(nums[i])
    return stack


def decreasing_mono_stack(nums):
    stack = []
    for i in range(len(nums)):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        stack.append(nums[i])
    return stack


class MonoStackTest(unittest.TestCase):

    def test_increasing_mono_stack(self):
        self.assertEqual(increasing_mono_stack([5, 3, 1, 2, 4]), [1, 2, 4])

    def test_decreasing_mono_stack(self):
        self.assertEqual(decreasing_mono_stack([5, 3, 1, 2, 4]), [5, 4])


if __name__ == "__main__":
    unittest.main()
