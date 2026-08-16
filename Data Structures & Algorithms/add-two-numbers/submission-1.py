# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # make l1 the longer
        cur = l1
        l1_len = 0
        while cur:
            l1_len += 1
            cur = cur.next
        cur = l2
        l2_len = 0
        while cur:
            l2_len+=1
            cur = cur.next
        
        if l1_len < l2_len:
            l1, l2 = l2, l1

        s = 0
        c = 0
        l1_cur = l1
        l2_cur = l2
        prev = None

        while l2_cur:
            l1_val = l1_cur.val
            l2_val = l2_cur.val
            s = (l1_val + l2_val) % 10
            l1_cur.val = (s + c) % 10
            c = (l1_val + l2_val + c) // 10
            prev = l1_cur
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next
        while l1_cur:
            l1_val = l1_cur.val
            l1_cur.val = (l1_val + c) % 10
            c = (l1_val + c) // 10
            prev = l1_cur
            l1_cur = l1_cur.next
        if c != 0:
            prev.next = ListNode(1)
        return l1
            
            
            
