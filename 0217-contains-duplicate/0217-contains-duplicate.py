class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) == len(nums):
        #     return False
        # return True


        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])
        return False          

        