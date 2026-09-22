class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0   ## points to the last unique element
        j = i + 1 ## scans through the array and find next unique elem
        
        while j < len(nums):  
            if nums[j] != nums[i]:  ## duplicate value get ignored
                i+=1
                nums[i]= nums[j]
            j += 1  ## for next unique element

        return i + 1  
""" if i = 2 (index) there will be total three elements 0,1,2 
return i + 1 => 2 + 1 => 3  """       
         




        