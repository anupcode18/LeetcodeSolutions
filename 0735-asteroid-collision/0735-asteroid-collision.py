class Solution:
    def asteroidCollision(self, ast: list[int]) -> list[int]:
        st = []
        for i in ast:
            while st and i < 0 and st[-1] > 0:
                diff = i + st[-1]
                if diff < 0:
                    st.pop()
                elif diff > 0:
                    break
                else:
                    st.pop()
                    break
                    
            else:
                st.append(i)
        return st
        
                


        