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
        list1=self.copy_list(head)
        list3=self.copy_list(head)

        list2=self.reverse(list3)
        index=0
        final_list=ListNode()
        cur=final_list
        for i in range(self.length(head)):
            if i % 2 == 0:
                temp_node=ListNode(list1.val)
                temp_node.next=final_list
                final_list=temp_node
                list1=list1.next
            elif i%2==1:
                temp_node=ListNode(list2.val)
                temp_node.next=final_list
                final_list=temp_node
                list2=list2.next
        final_list=self.reverse(final_list)
        cur=final_list.next
        head=cur
       
    def reverse(self, x):
        cur = x
        prev = None 
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def copy_list(self, y):
        if not y:
            return None

        new_head = ListNode(0)  # Create a dummy node to simplify the code.
        original = y
        new_tail = new_head  # Initialize new_tail to the dummy node.

        while original:
            new_node = ListNode(original.val)
            new_tail.next = new_node
            new_tail = new_node
            original = original.next

        return new_head.next  # Return the actual head of the copied list.
    def length(self,z):
        cur=z
        leng=0
        while cur:
            cur=cur.next
            leng+=1
        return leng
