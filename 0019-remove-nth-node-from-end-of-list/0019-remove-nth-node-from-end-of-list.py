# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        ## the loop is for updating fast postion from head
        # to head + n
        for _ in range(n):
            fast = fast.next
            # If fast is at the last node, it means we need to remove the first node.
        if fast.next == None:
            return head.next

        # Because fast is n nodes ahead, slow will be exactly before the node we need to delete.
        # Move both pointers together until fast reaches the last node
        while fast.next != None:
            slow = slow.next 
            fast = fast.next
            # skip the unwanted node
        slow.next = slow.next.next
        return dummy.next


        