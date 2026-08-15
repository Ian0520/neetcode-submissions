# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        back = head
        front = back.next
        while front:
            if back == front:
                return True
            back = back.next
            front = front.next
            if front:
                front = front.next
        return False