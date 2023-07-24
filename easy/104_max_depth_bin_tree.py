class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self,node):
        return 0 if not node else 1 + max(self.max_depth(node.left),self.max_depth(node.right))


tree = Node(3,Node(9),Node(20,Node(15),Node(7)))
tree2 = Node(1,
            Node(2),
            Node(3,
                    Node(4),
                    Node(5,
                        Node(6),
                        Node(7))))
res = Solution().max_depth(tree2)
print(res)