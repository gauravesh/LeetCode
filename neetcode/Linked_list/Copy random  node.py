"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldtocopy={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            oldtocopy[cur]=copy
            cur=cur.next

        cur=head
        while cur:
            copy = oldtocopy[cur]
            copy.next=oldtocopy[cur.next]
            copy.random=oldtocopy[cur.random]
            cur=cur.next
        
        return oldtocopy[head]





        
