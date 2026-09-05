class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # min_suffix[i] = minimum value in nums[i:]
        min_suffix = [0] * n
        min_curr = float("inf")

        for i in range(n - 1, -1, -1):
            min_curr = min(min_curr, nums[i])
            min_suffix[i] = min_curr

        curr_max = float("-inf")

        for i in range(n):
            curr_max = max(curr_max, nums[i])

            if curr_max - min_suffix[i] <= k:
                return i

        return -1