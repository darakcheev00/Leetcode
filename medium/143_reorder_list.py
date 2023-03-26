# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head

        # find middle
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        # reverse second half of list
        curr = slow.next
        prev = slow
        prev.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr2 = prev

        # merge 2 lists
        curr1 = head

        while curr2:
            nxt = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1 = curr1.next
            curr1.next = nxt
            curr1 = curr1.next

        curr1.next = None

"""
idea:
- first find the middle of the list
- then reverse second half of the list
- then merge the 2 lists
"""




