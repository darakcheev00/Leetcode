# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# import queue
import heapq as hq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        # make heap of max size k
        heap = []
        for i,list in enumerate(lists):
            if list:
                hq.heappush(heap,(list.val,i,list))

        dummy = ListNode(-1)
        self.merge(dummy,heap)
        return dummy.next

    def merge(self,m,heap):
        if len(heap) == 0:
            return

        _,i,node = hq.heappop(heap)
        m.next = node
        m = m.next
        
        if node.next:
            hq.heappush(heap,(node.next.val,i,node.next))

        self.merge(m,heap)

"""
idea:
make heap of tuples: (node.val, list_index, pointer)
make dummy node to point to head of merged
merge all lists recursively:
    pop heap to get smallest element
return merged
"""


    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     #q = queue.PriorityQueue()
    #     heap = []
        
    #     dummy = ListNode(None)
    #     curr = dummy
    #     count = 0
    #     for list in lists:
    #         if list:
    #             hq.heappush(heap,(list.val,count,list))
    #             count += 1
                
    #     while(heap):
    #         val, c, listHead = hq.heappop(heap)
    #         curr.next = listHead
    #         if listHead.next:
    #             hq.heappush(heap,(listHead.next.val,count,listHead.next))
    #             count += 1
            
    #         curr = curr.next
            
    #     return dummy.next