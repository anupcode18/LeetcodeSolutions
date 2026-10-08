# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None

        slow, fast, prev = head, head, None
        # fast moves doulbe speed of slow, one fast reaches end slow will reach to the middle
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # skip slow ptr connect the link to next node of slow 
        prev.next = prev.next.next ## slow.next also works  

        return head

        
