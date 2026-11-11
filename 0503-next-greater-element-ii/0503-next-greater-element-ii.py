class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #montonic stack like temperatures q
        stack = []
        l = len(nums)
        ans = [-1] * l
        for i,v in enumerate(nums):
            while stack and stack[-1][1] < v:
                x,y = stack.pop()
                ans[x] = v
            stack.append((i,v))
        if stack:
            for k in nums:
                while stack and stack[-1][1] < k:
                    x,y = stack.pop()
                    ans[x] = k
        return ans
