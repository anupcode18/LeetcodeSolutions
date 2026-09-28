class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1

        # for i in range(n-1, -1, -1):
        i = len(res) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
                i-=1
            else:
                res[i] = nums[right] ** 2
                right -= 1
                i-=1
        return res

