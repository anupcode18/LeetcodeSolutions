class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # for i in range(0, rotations):
        nums[:] = nums[n-k:] + nums[:n - k]
            
           
