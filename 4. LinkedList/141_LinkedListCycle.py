'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        fast = head
        
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        
        return False