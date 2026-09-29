class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        letter_window = s[:k]
        
        for vowel in letter_window:
            if vowel in "aieou":
                vowel_count += 1
        left = 0
        max_count = vowel_count
        for right in range(k, len(s)):
            if s[left] in "aieou":
                vowel_count -= 1
            if s[right] in "aieou":
                vowel_count += 1
            left += 1
            max_count = max(max_count, vowel_count)
        return max_count
            
        
            
        
        