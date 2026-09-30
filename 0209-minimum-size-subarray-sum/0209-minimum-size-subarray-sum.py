class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left, right, count = 0, 0, 0
        run_sum = 0
        min_len = float("inf")

        while right < len(nums):
            run_sum += nums[right]
            count += 1

            while run_sum >= target:
                # current window is valid
                min_len = min(min_len, count)

                # shrik from left
                run_sum -= nums[left]
                left += 1
                count -= 1

            right += 1

        return 0 if min_len == float("inf") else min_len
