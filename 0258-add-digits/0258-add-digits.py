class Solution:
    def addDigits(self, num: int) -> int:
        n = num
       
        
        while n >= 10:
            cur_sum = 0
            while n > 0:
                ld = n % 10
                cur_sum = ld + cur_sum
                n //= 10

            n = cur_sum


        return n



            

        