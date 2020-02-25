s = input().strip()


class Solution:
    def getCenter(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (i+1, j-i-1)

    def longestPalindrome(self, s: str) -> str:
        n, start, maxLen = len(s), 0, 0
        for i in range(n):
            p1 = self.getCenter(s, i, i)
            p2 = self.getCenter(s, i, i+1)
            p = max([p1, p2], key=lambda i: i[1])
            if maxLen < p[1]:
                start = p[0]
                maxLen = p[1]
        return s[start:start+maxLen]


print(Solution().longestPalindrome(s))
