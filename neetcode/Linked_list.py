# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        reverse=[]
        

        while cur: 
           # print(cur.val)
            reverse.append(cur.val)
            cur=cur.next
            
        r=list ((reverse))
        curr=None

        for i in r:
            temp_node=ListNode(i)
            temp_node.next=curr
            curr=temp_node
        return curr
