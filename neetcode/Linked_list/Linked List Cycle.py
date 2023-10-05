# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        i=0
        if not head:
            return False
        if head.next is None:
            return False

        while head and i < 10001:
            head=head.next
            if head.next is None:
                return False
            i+=1
        return True
        
