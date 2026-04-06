# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
        
        # # get head, get next
        # next = head.next
        # # set prev as head
        # prev = head

        # # on next, get next of next
        # while head:
        #     next_of_next = next.next
        #     # set next to point to prev
        #     next.next = prev
        #     # set prev as next
        #     prev = next
        #     # set next as head
        #     next = head
            
        # return prev