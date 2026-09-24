class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def lowerBound(nums):
            lb, low, high = -1, 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return lb

        def upperBound(nums):
            ub, low, high = len(nums), 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ub

        lb = lowerBound(nums)

        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = upperBound(nums)

        return [lb, ub - 1]