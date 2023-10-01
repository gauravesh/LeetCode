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
        
        list1=head
        
        new_list = self.reverse(head)
        
        length_of_lists=(self.find_length(new_list))
        temp=ListNode()
        cur=temp
        tt=list1
        while tt:
            print(tt.val)
            tt=tt.next


        

        for i in range(length_of_lists):
            if i%2==0:
                if list1:
                    print(list1.val)
                    list1 = list1.next

            elif i%2==1:
                print("odd",i)
            
            

        #while 

    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def print_list(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next
    def find_length(self,head):
        cur = head
        length=0
        while cur:
            length+=1
            cur=cur.next
        return length
        
    
    
