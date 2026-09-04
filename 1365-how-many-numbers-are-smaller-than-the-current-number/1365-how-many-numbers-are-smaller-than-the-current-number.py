class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        # count = 0     ## reminder because of this you struggled 20 min extra
        # nums.sort()

        for i in range(n):
            count=0
            for j in range(n):
                if nums[j] < nums[i]:
                    count+=1
            res.append(count)
        return res
        