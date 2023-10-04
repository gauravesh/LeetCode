# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l1=head
        prev=l1
        length_ptr = head
        #find length
        length=0
        while length_ptr:
            length_ptr=length_ptr.next
            length+=1

        ter=0
        if abs(n-length)==0:
            if head.next == None:
                head = None
            else:
                head=head.next
            return head
        while ter < abs(n-length):
            ter+=1
            if not l1:
                return
            prev=l1
            l1=l1.next

        

        prev.next=l1.next
        return head

         
