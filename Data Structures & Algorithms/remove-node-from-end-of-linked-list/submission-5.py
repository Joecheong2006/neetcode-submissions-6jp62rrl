# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            del head
            return None
            
        curr, prev = head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        new_head = prev
        curr, prev = new_head, None
        while n != 1:
            prev = curr
            curr = curr.next
            n -= 1

        next = curr.next
        del curr
        if prev:
            prev.next = next
        else:
            new_head = next

        curr, prev = new_head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
