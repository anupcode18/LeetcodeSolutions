# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        curr = dummy
        n = 0
        # loop for calc the length of LL or n
        while curr.next != None:
            curr = curr.next
            n+=1
        # for loop runs till middle of the loop exclude last element 
        curr = dummy ## reset curr to dummy 
        for _ in range(n//2):
            ## move slowPtr to middle node - 1
            curr = curr.next
        ## skip the middle node by direclty conneting it' next node
        curr.next = curr.next.next

        return dummy.next ## return head
        


        
