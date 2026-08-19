class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        running_sum = 0
        for i in range(len(nums)):
            running_sum = running_sum + nums[i]
            result.append(running_sum) 
        return result
            
        
        
       