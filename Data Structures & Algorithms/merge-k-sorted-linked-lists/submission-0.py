# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            cur = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else: 
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 if list1 else list2
            return dummy.next
        
        for i in range(len(lists)-1, 0, -1):
            lists[i-1] = mergeTwoLists(lists[i], lists[i-1])
        return lists[0]