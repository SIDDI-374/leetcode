from typing import Optional
class Solution:
    def addTwoNumbers(self, l1:[ListNode],l2:[ListNode]) ->[ListNode]:
        view = ListNode(0)  
        curr = view
        carry = 0
        while l1 or l2 or carry:
            # Get values (0 if node is None)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10          # carry for next iteration
            curr.next = ListNode(total % 10)  # store single digit

            # Advance pointers
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return view.next 


            
    
        
