class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s = sorted(s)
        t = sorted(t)
        n = len(s)

        for i in range(n):

            if s[i] != t[i]:
                return t[i]

        return t[n]
        