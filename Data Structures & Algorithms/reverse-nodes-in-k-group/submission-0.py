# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_next_k(start, k):
            prev = None
            cur = start

            for _ in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            # prev = new head of reversed group
            # start = new tail of reversed group
            # cur = start of next group
            start.next = cur
            return prev, start, cur
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        cur = head
        while n >= k:
            new_head, new_tail, next_group = reverse_next_k(cur, k)
            prev_group_tail.next = new_head

            prev_group_tail = new_tail
            cur = next_group

            n -= k
        return dummy.next
            