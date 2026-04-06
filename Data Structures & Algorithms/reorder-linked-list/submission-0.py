# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Find middle (slow / fast method)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half (reverse linked list)
        # Init second list
        second_list = slow.next
        # Set prev, set slow.next to None to unlink
        prev = slow.next = None

        while second_list:
            tmp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = tmp

        # merge two halfs (alternate merging)
        first_list, second_list = head, prev
        while second_list:
            # Store next nodes
            tmp1, tmp2 = first_list.next, second_list.next
            # Re-assign first and second nodes
            first_list.next = second_list
            second_list.next = tmp1

            # Move pointers
            first_list, second_list = tmp1, tmp2
