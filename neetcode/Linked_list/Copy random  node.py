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
        #first lets copy the linked list
        new_List=ListNode()
        ur=new_List
        cur=head
        while cur.next is not None:
            temp_val=cur.val
            ur.next=ListNode(temp_val)
            ur=ur.next
            cur=cur.next
        new_List=new_List.next


        





        
