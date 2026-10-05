# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # if head == none return directly head 
        if not head:
            return head 

        odd = head
        # evenHead will be used at the end to connect odd and even nodes
        even_head = even = head.next

        # This condition makes sure odd can never be None, since the odd node will always be the one before the even node.
       # If even is not None, then odd is not None. (odd before even)
        while even and even.next:
            # connect the current odd node to the next odd node
            odd.next = odd.next.next
            # update the odd node to the next odd node
            odd = odd.next
            
            # same with even
            even.next = even.next.next
            even = even.next

        # connect the 1st node of even node to the last node of odd node
        odd.next = even_head
        # head never change, just return it
        return head
        
        
        