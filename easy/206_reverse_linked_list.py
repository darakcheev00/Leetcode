# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        return self.crawl(None,head)

    def crawl(self,prev,curr):
        next = curr.next
        
        if not next:
            curr.next = prev
            return curr

        # flip
        curr.next = prev
        prev = curr
        curr = next

        return self.crawl(prev, curr)
    

"""
Idea
crawl through the linked list using prev, 
curr pointers to rearrange the next pointer.
Make sure to reverse the last arrow before returning
"""