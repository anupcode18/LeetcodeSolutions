class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        total_sum = 0
        result = []
        for i in nums:
            total_sum += i
            result.append(total_sum)
        return result

        