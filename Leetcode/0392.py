class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if s == "":
            return True
        elif t == "":
            return False
        for n in t:
            if n == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False