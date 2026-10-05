# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = head
        length = 0
        while temp != None:
            length+=1
            temp = temp.next
        # edge case
        if length == n:
            new_head = head.next
            return new_head

        pos = length - n #position_to_stop
        temp = head
        count = 1 ## 1st node counted
        while count < pos:
            temp = temp.next
            count += 1
        # connect prev node of target to the next node of target 
        # it means deleting the target node
        temp.next = temp.next.next
        return head
        
            



        