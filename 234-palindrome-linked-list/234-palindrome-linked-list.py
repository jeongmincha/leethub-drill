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
    
    # This solution - Time Complexity: O(n), Space Comlexity: O(n)
    # It solves the problem by using a stack
    def __isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
            
        answer = True
        curr = head
        while curr:
            if stack.pop() != curr.val:
                answer = False
                break
            curr = curr.next
        
        return answer
    
    # This solution - Time Complexity: O(n), Space Complexity: O(1)
    # It will work with the `reverseList()` which is implemented above
    def _isPalindrome(self, head: Optional[ListNode]) -> bool:
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
    
    # This solution - Time Complexity: O(n), Space Complexity: O(1)
    # This uses recursion to solve the problem.
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        
        def helper(right):
            nonlocal left
            
            if right is None:
                return True
            
            isSubPalindrome = helper(right.next)
            if not isSubPalindrome:
                return False
            
            _isPalindrome = left.val == right.val
            left = left.next
            return _isPalindrome
        
        return helper(head)