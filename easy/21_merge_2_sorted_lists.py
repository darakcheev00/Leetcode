# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2: 
            return None
        
        dummy = ListNode(-1)
        self.merge(dummy,list1,list2)
        return dummy.next


    def merge(self, m, l1, l2):
        if l1.val < l2.val:
            m.next = l1
            l1 = l1.next
        else:
            m.next = l2
            l2 = l2.next

        m = m.next

        if not l1:
            m.next = l2
            return m
        elif not l2:
            m.next = l1
            return m

        return self.merge(m,l1,l2)


"""
idea:
create dummy node to point to merged list head
compare list pointers
add smaller list pointer to m.next
advance m to be this next element
check if either list is done:
    if so then just append the rest of the other list

call merge again with the resulting lists
"""
