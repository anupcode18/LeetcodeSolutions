class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []

## the wile loop run until word1 and word2 has words 
## if i or j beocme greater than len of i or j the loop stops
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:]) ## for remaining words in word1 
        res.append(word2[j:]) ## for remaining words in word2 

        return "".join(res)
        