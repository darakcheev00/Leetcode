# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head
        slow = head

        while True:
            if not fast.next or not fast.next.next:
                return False

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            

"""
idea:
fast pointer jumps by 2, slow jumps by one.
if fast and slow ever meet there is a cycle
if fast.next or fast.next.next is ever None there is no cycle
"""