# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4
# 2.next = last
# last = 2
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev