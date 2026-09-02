class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        op = []

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                op.append(left + 1)
                op.append(right + 1)
                return op
            elif s < target:
                left +=1
                
            else:
                right -= 1
        

        