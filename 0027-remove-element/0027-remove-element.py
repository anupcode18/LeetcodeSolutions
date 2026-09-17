class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  ## tells us where to put next valid element
        i = 0  ## scans every element
    
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]  ## if cond true then change values
                k += 1
            i += 1
        return k
        