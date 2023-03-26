class LinkNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def print(self):
        curr = self.next
        print(f"{self.val} -> ",end='')
        while curr:
            print(f"{curr.val} -> ",end='')
            curr = curr.next 
        print("None")

class Solution:
    def remove_nth_node_from_end(self, head, n):
        if not head or not head.next:
            head = None
            return head
        
        fast = head
        slow = head

        len = 1
        slow_pos = 0

        while fast.next:
            if not fast.next.next:
                len += 1
                break

            len += 2
            fast = fast.next.next

        dead_index = len - n

        while slow_pos < dead_index-1:
            slow = slow.next
            slow_pos += 1

        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return head


"""
Idea:
use fast point to find len of array
then slow point to move to that location and reroute
"""

list1 = LinkNode(1,LinkNode(2,LinkNode(3,LinkNode(4,LinkNode(5)))))
list2 = LinkNode(1)
list3 = LinkNode(1,LinkNode(2))

s1 = Solution()
s1.remove_nth_node_from_end(list1,2)
list1.print()
list2 = s1.remove_nth_node_from_end(list2,1)
list2.print()
s1.remove_nth_node_from_end(list3,1)
list3.print()
