class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] % 2 == 0:  ## if true even no. spotted
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
            
        return nums
        
        