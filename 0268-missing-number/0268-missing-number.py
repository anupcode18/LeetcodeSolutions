class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return sum(range(len(nums)+1)) - sum(nums)

        nums.sort()

        for ind, num in enumerate(nums):
            if ind != num:
                return num - 1
            if num == len(nums) - 1:
                return num + 1

        
        