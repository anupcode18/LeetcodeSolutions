# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        ## brute force
        n = 0  ## counting nodes 
        temp = head
        ## after loop end we know nodes length
        while temp is not None:
            n+=1
            temp = temp.next
        temp = head
        ## 2nd loop to traverse and finding middle
        for i in range(0,n//2):
            temp = temp.next
        return temp
        


        