# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find mid node
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow
        # Reverse second half
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Iter with the second since the first has not disconnected yet
        res = 0
        first, second = head, prev
        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res