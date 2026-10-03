# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res < 0:
                high = mid - 1
            else:
                low = mid + 1

""" 
Approach for this Problem:
Initialize first to 1 and last to n.
While first is less than or equal to last, do the following:
a. Compute mid as first + (last - first) / 2.
b. If guess(mid) returns 0, return mid, means the guess is correct
c. If guess(mid) returns -1, update last to mid - 1, means guess is higher
d. If guess(mid) returns 1, update first to mid + 1, means guess is lower.
Return -1.
 """