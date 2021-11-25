class Solution:

    def solve(self, s):
        ans = ''
        for i in range(len(s) - 1):
            c = s[i]
            if s[i:i+2] == 'xz':
                i += 1
                continue
            if c == 'y':
                continue
            print(c)
            ans += c
        print(ans)
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.solve("xyxyxz") == 'xx'
    assert solution.solve("xyz") == 'xz'
