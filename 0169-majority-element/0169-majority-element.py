class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for key, value in freq.items():
            if freq[key] > n/2:
                return key

   

        