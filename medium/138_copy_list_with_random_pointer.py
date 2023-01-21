"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        mapping = {}

        # Create new unlinked nodes
        curr = head
        while curr:
            mapping[id(curr)] = Node(curr.val)
            curr = curr.next

        # Link nodes based on original linked list
        curr = head
        while curr:
            mapping[id(curr)].next = mapping[id(curr.next)] if curr.next else None 
            mapping[id(curr)].random = mapping[id(curr.random)] if curr.random else None 
            curr = curr.next

        return mapping[id(head)]


"""
Time: O(2n)
Space: O(n)

Solution:
First copy the nodes and save references to them in a hashmap: key is id of original node, value is a pointer to the new node. Then loop through the list again and link new linked list nodes based on the original linked list.
Note: when relinking check if curr.next or curr.random is null because id of an object is used as the key in the hashmap but null has no id.
"""
