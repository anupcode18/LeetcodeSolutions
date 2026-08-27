class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # count = 0
        
        even_num_count = 0

        for elements in nums:
            no_of_digits = 0

            while elements > 0:
                no_of_digits+=1
                elements =  elements // 10
            if no_of_digits % 2 == 0:
                even_num_count+=1
   

        return even_num_count

  

        