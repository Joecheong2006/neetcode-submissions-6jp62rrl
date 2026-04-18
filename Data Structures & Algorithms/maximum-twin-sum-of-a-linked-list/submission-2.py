# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find mid node
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = None

        prev, curr = None, slow
        # Reverse second half
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        res = 0
        first, second = head, prev
        while first:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res