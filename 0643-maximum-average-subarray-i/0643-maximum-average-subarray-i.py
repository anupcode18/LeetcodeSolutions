class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        # sum of first window
        window_sum = sum(nums[:k])
        # set 1st window as max sum default 
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum -= nums[left]
            window_sum += nums[right]

            max_sum = max(max_sum, window_sum)
            left += 1
        return max_sum/k  