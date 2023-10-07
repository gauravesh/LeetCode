class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur=ListNode()
        head=cur
        carry=0
        while l1 or l2 or carry!=0:
            if not l1:
                v1=0
            else:
                v1=l1.val
            if not l2:
                v2=0
            else:
                v2=l2.val
            
            total=v1+v2+carry
            
            carry=total//10
            
            digit=total%10

            print(total)
            
            cur.next=ListNode(digit)
            
            cur=cur.next

            if l1:
                l1=l1.next

            if l2:
                l2=l2.next

        return head.next
        
            
            



        
