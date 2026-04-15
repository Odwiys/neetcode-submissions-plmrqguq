# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node to avoid edge case of return empty list
        dummy = ListNode()
        # Initiate tail to start list
        tail = dummy

        # Iterate through list1 and list2
        while list1 and list2:
            # Check which has a lower value, assign to tail
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # update tail
            tail = tail.next

        # Append remainder of list to tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        # Return start of list from dummy
        return dummy.next












        # # Create dummy node to avoid edge case of return empty list
        # dummy = ListNode()
        # # Initiate tail to start list
        # tail = dummy

        # # Iterate through list1 and list2
        # while list1 and list2:
        #     # Check which has a lower value, assign to tail
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     # update tail
        #     tail = tail.next

        # # Append remainder of list to tail
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2

        # # Return start of list from dummy
        # return dummy.next
