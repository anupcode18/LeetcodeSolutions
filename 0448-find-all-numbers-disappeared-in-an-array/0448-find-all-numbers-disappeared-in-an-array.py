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

# Frequency Map Approach:
# 1. Count frequency of every number present in nums.
# 2. Loop from 1 to n because these numbers should exist.
# 3. If freq.get(num, 0) == 0, num is missing.
# 4. Store missing numbers in missing_num and return it.
#
# .get(num, 0) returns 0 if num is not present in the dictionary.
# Time: O(n) | Space: O(n)

# TC: O(n)
# First loop runs n times to count frequencies.
# Second loop also runs n times to check numbers 1 to n.
# O(n) + O(n) = O(n).

# SC: O(n)
# freq dictionary can store up to n numbers.
# missing_num list can also store up to n numbers.
# O(n) + O(n) = O(n) extra space.
