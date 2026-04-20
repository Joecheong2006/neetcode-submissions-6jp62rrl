# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1

        n = l - n + 1
        curr, prev = head, None
        while n != 1:
            prev = curr
            curr = curr.next
            n -= 1

        next = curr.next
        del curr
        if prev:
            prev.next = next
        else:
            head = next
        return head
