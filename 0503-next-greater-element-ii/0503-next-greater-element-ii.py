class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            for j in range(1, n):
                idx = (i + j) % n

                if nums[idx] > nums[i]:
                    ans[i] = nums[idx]
                    break

        return ans