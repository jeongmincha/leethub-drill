# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        answer = True
        curr = head
        while curr:
            elem = stack.pop()
            
            if curr.val != elem:
                answer = False
            
            curr = curr.next
        
        return answer