class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        small = 0
        big = 0

        while small < len(s) and big < len(t):
            if s[small] == t[big]:
                small+=1
            big+=1
        
        if small == len(s): 
            return True
        return False
    
"""     easy way : return small == len(s)
    if true it will return True """
