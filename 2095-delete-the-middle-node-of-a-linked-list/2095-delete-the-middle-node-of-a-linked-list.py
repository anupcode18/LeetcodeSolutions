# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        n = 0
        # loop for calc the length of LL or n
        while fast.next != None:
            fast = fast.next
            n+=1
        # for loop runs till middle of the loop exclude last element 
        for _ in range(n//2):
            ## move slowPtr to middle node - 1
            slow = slow.next
        ## skip the middle node by direclty conneting it' next node
        slow.next = slow.next.next

        return dummy.next ## return head
        


        
