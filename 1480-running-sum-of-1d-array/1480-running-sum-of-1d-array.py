class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total_sum = 0
        result = []
        for i in range(len(nums)):
            total_sum += nums[i]
            result.append(total_sum)
        return result

        