class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        missing_num = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in range(1, n+1):
            if freq.get(num,0) == 0:
                missing_num.append(num)

        return missing_num


                
