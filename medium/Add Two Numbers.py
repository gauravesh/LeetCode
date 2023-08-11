class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()  # Create a dummy head for the result linked list
        cur = head  # Initialize a pointer to traverse the result linked list
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10
            
            cur.next = ListNode(digit)
            cur = cur.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next  # Return the result linked list (skip the dummy head)


            
            



        
