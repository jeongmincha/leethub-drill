# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        answer = None
        
        p = None
        c = head
        n = c.next
        
        while n:
            c.next = p
            
            p = c
            c = n
            n = n.next
        
        c.next = p

        return c