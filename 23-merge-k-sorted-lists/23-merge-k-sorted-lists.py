class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return head.next
