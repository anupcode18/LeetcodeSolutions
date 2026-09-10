class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = [], []

        for i in range(0,n):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        result = [0] * n
        pos_idx = 0
        neg_idx = 1

        for i in range(len(pos)):  ## len(pos) = len(neg) == 3
            result[pos_idx] = pos[i]
            result[neg_idx] = neg[i]

            pos_idx += 2
            neg_idx += 2
        
        return result
        