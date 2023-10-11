# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s=f=head
        while f and f.next:
            f=f.next.next
            s=s.next
        second=s
        prev=s=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        f1=head
        f2=prev

        while f2:
            print(f1.val,f2.val)
            t1=f1.next
            t2=f2.next
            f1.next=f2
            f2.next=t1
            f1,f2=t1,t2
        t,h=head,head.next
        while h and h.next :
            h=h.next.next
            t=t.next
            if h == t:
                h.next.next=None
        
    
