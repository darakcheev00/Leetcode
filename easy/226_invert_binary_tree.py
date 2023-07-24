class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_binary_tree(self,tree):
        def invert(node):
            if not node:
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp

            invert(node.left)
            invert(node.right)

        invert(tree)

        return tree


def printTree(tree):
    def dive(node):
        if node:
            print(f"{node.val}, ",end="")
            print("L: ",end="")
            dive(node.left)
            print("R: ",end="")
            dive(node.right)
    dive(tree)
    print("\n----")

    
tree1 = Node(3,Node(20,Node(13),Node(7)),Node(9))
printTree(tree1)

res = Solution().invert_binary_tree(tree1)


printTree(res)