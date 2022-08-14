# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> None:
        prev = None
        curr = head
        
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # if fast is not None, the length will be odd.
        if fast:
            mid = slow
            slow = slow.next
            mid.next = None
        
        answer = True
        left = head
        right = self.reverseList(slow)
        while right:
            if left.val != right.val:
                answer = False
                break
            
            left = left.next
            right = right.next
        
        return answer