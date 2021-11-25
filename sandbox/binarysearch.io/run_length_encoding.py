class Solution:
    def solve(self, s):
        # Write your code here
        ct = 0
        pc = ''
        r = ''
        for c in s.strip():
            if c == pc:
                ct += 1
            elif c != pc:
                if not ct:
                    ct = ''
                print(ct)
                if ct == 9:
                    __import__('pdb').set_trace()
                r += str(ct) + pc
                pc = c
                ct = 1
        return r + str(ct) + pc


if __name__ == "__main__":
    solution = Solution()
    assert solution.solve("AAAABBBCCDAA") == "4A3B2C1D2A"
    assert solution.solve("ABCDE") == "1A1B1C1D1E"
    assert solution.solve("AABBA") == "2A2B1A"
    assert solution.solve("AAAAAAAAAAAAABBCDDDD") == "9A4A2BC4D"
