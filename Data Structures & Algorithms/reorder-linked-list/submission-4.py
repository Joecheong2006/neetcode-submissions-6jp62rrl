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
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        list1 = head
        list2 = self.reverseList(slow.next)
        slow.next = None

        while list2 != None:
            next1, next2 = list1.next, list2.next
            list1.next = list2
            list2.next = next1
            list1, list2 = next1, next2