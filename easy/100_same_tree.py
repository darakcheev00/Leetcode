class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sameTree(self,node1,node2):
        if (not node1 and node2) or (not node2 and node1):
            return False
        if not node1 and not node2:
            return True
        
        def setMaxMin(node):
            max,min= None,None
            if node.left:
                if node.right:
                    if node.left.val > node.right.val:
                        max = node.left
                        min = node.right
                    else:
                        max = node.right
                        min = node.left
                else:
                    max = node.left
            else:
                if node.right:
                    max = node.right
            return max,min

        maxA,minA= setMaxMin(node1)
        maxB,minB= setMaxMin(node2)
        # print(maxA.val,minA.val)
        # print(maxB.val,minB.val)
        # print("----")

        return node1.val == node2.val and self.sameTree(maxA, maxB) and self.sameTree(minA,minB)


tree1a = Node(3,Node(20,Node(13),Node(7)),Node(9))
tree1b = Node(3,Node(9),Node(20,Node(15),Node(7)))

tree2 = Node(1,
            Node(2),
            Node(3,
                    Node(4),
                    Node(5,
                        Node(6),
                        Node(7))))

tree3a = Node(1,Node(2,Node(1)),Node(3))
tree3b = Node(1,Node(3),Node(2,Node(1)))

res = Solution().sameTree(tree3a,tree3b)
print(res)


# this is the isotope solution where each node is flippable ^^^^

# but here is the simple stiff tree solutionm

def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    
    if p and q:
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    elif p and not q or q and not p:
        return False
    else:
        return True
