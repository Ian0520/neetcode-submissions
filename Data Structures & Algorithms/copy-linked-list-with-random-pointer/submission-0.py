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
            return None
        orig_to_new_nodes = dict()

        # Pass 1: create every node
        cur = head
        while cur:
            orig_to_new_nodes[cur] = Node(cur.val)
            cur = cur.next


        # Pass 2: connect next and random
        cur = head
        while cur:
            copy = orig_to_new_nodes[cur]

            if cur.next:
                copy.next = orig_to_new_nodes[cur.next]

            if cur.random:
                copy.random = orig_to_new_nodes[cur.random]

            cur = cur.next

        return orig_to_new_nodes[head]
            
        

            