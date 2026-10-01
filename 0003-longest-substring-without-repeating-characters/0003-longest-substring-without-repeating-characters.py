class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = max_len = 0
        
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
                
            my_set.add(s[right])    
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
