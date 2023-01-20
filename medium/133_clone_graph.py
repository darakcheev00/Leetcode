"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        relinked_nodes = set()

        def copy_node(node):
            if id(node) in mapping:
                return

            mapping[id(node)] = Node(node.val, [])

            for n in node.neighbors:
                copy_node(n)

        def relink_node(node):
            if node in relinked_nodes:
                return

            for n in node.neighbors:
                mapping[id(node)].neighbors.append(mapping[id(n)])
            
            relinked_nodes.add(node)

            for n in node.neighbors:
                relink_node(n)

        if node:
            copy_node(node)
            relink_node(node)
            return mapping[id(node)]
        
        else:
            return node

"""
Time complexity: O(m*n) m = branching factor, n = depth
Space complexity: O(2n)

Solution:
First run dfs to create clones of nodes in graph and save in hashmap where the key is the id of the old node, and the value is the new node object. 
Then relink the nodes through another dfs, by appending all adjacent nodes to the neighbors list.
After running both functions just return the node in the map corresponding to the original starting node id.
"""