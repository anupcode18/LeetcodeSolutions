class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        lb = n
        low, high = 0, n-1
        while low <= high:  ## why low <= high?
            mid = (low+high)//2
            if nums[mid] >= target:
                lb = mid ## updating lb mid's index from n 
                high = mid - 1
            else:
                low = mid + 1
        return lb
        