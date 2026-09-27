class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        small = 0
        big = 0

        while small < len(s) and big < len(t):
            if s[small] == t[big]:
                small+=1
            big+=1
        
        if small == len(s):
            return True
        return False