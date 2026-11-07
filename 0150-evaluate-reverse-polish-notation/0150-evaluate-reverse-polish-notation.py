class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for ch in tokens:
            if ch == '+':
                st.append(st.pop() + st.pop())
            elif ch == '-':
                a, b = st.pop(), st.pop()
                st.append(b - a)
            elif ch == '*':
                st.append(st.pop() * st.pop())
            elif ch == '/':
                a, b = st.pop(), st.pop()
                st.append(int(b / a))
                
            else:
                st.append(int(ch))
        
        return st[-1]