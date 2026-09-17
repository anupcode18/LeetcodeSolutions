class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):  ## len of 1st string
            for word in strs:
                ch = strs[0][i]
                if i == len(word) or word[i] != ch:
                    return res
            res += ch
        return res
    
""" 
inner loop : this goes thorugh every word(string) of strs
line 6 : 1st char of word at index 0 """


        
        