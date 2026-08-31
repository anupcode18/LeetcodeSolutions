class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0    # k is var, we are declaring at oth index in nums
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
        