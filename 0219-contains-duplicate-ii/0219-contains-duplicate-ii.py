class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        my_set = set()
        left = 0

        for right in range(len(nums)):

            # If the window becomes larger than k,
            # remove the element that is leaving the window.
            if right - left > k:
                my_set.remove(nums[left])
                left += 1

            # If nums[right] is already in the current window,
            # we found the same value within k indices.
            if nums[right] in my_set:
                return True

            # Add the current element to the window.
            my_set.add(nums[right])

        return False