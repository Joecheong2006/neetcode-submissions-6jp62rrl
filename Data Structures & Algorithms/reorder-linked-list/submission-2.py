# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr != None:
            curr.next = self.reverseList(curr.next)
            curr = curr.next
