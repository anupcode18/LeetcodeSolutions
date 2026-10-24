class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(index, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if index >= len(candidates) or total > target:
                return 
            
            subset.append(candidates[index])
            # adding the same no. again 
            dfs(index, subset, total + candidates[index]) 
            subset.pop()
            # after poping the num moving to the next index
            dfs(index + 1, subset, total)

        dfs(0,[],0)
        return res



        