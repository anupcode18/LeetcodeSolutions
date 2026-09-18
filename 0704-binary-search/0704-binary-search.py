class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0 ## 0th index
        high = n - 1 ## last index

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid  ## mid's index => target index
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1  ## if target element is not in nums return -1
        