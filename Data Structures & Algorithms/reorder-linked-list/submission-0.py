# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        # reverse second half
        prev = None
        cur = slow.next

        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # reorder
        list2 = prev
        list1 = head
        while list1 and list2:
            next = list1.next
            list1.next = list2
            list1 = next

            next = list2.next
            list2.next = list1
            list2 = next
