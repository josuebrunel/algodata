import unittest


# O(n) time | O(1) space
def jump_game(nums):
    """What if instead of starting from the first element
    we start by the last element. The idea is to set the
    last element as a goal and shift the goal as long as
    the index of current element (i) plus the value of the
    value of the current element (nums[i]) is superior or
    equal to the goal.
    """
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        # it's >= because the value
        # represents the **max** jump
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


class JumpGameTest(unittest.TestCase):
    def test_jump_game(self):
        self.assertEqual(jump_game([2, 3, 1, 1, 4]), True)
        self.assertEqual(jump_game([3, 2, 1, 0, 4]), False)


if __name__ == "__main__":
    unittest.main()
