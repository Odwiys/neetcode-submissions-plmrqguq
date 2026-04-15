# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init dummy/ tail , previous and current pointers
        previous = None
        current = head

        # iterate through
        while current:
            # store next as tmp
            tmp = current.next
            # reverse pointer
            current.next = previous
            # move pointers forward
            previous = current
            current = tmp
        
        return previous