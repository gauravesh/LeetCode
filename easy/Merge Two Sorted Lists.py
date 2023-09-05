# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = list1
        head2 = list2
        list3 = []

        while head1:
            list3.append(int(head1.val))
            head1 = head1.next 

        while head2:
            list3.append(int(head2.val))
            head2 = head2.next
        list3.sort()

        # Create a new linked list.
        head_new = ListNode()
        current = head_new 

        for i in list3:
            current.next = ListNode(i)
            current = current.next
        head_new = head_new.next

        return head_new
