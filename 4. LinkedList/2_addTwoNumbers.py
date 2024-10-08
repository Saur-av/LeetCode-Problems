'''You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity : Linear | O(N)
        Spacee Complexity : Linear | O(N)'''
        head = ListNode()
        dummy = head
        carry = 0

        while (l1 or l2 or carry != 0):
            if not l1:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next

            if not l2:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next

            s = val1 + val2 + carry

            carry = s // 10
            s = s % 10

            dummy.next = ListNode(s)
            dummy = dummy.next
        
        return head.next
        