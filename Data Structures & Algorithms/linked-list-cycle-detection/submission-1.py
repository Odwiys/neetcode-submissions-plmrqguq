# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False




        # # init fast and slow pointers
        # fast, slow = head, head

        # # iter through
        # while fast and fast.next:
        #     # Move fast and slow pointers
        #     fast = fast.next.next
        #     slow = slow.next

        #     # Check if they meet
        #     if fast == slow:
        #         return True

        # # Else return false
        # return False