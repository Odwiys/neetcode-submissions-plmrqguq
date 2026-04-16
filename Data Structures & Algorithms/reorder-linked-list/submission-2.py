# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle (fast / slow)
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        # break of list
        second = slow.next
        prev = slow.next = None

        # reverse second half of list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge 2 lists
        first, second = head, prev # (since prev of second list is none)
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
