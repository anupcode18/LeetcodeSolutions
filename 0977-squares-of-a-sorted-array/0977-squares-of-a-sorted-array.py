class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        el = []

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
            el.append(nums[i])
        el.sort()
        return el

        