# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sentinel = l3 = ListNode()
        rest = 0
        while l1 is not None and l2 is not None:
            l3.next = ListNode((rest + l1.val + l2.val) % 10)
            rest = (rest + l1.val + l2.val) // 10
            l1, l2 = l1.next, l2.next
            l3 = l3.next
        while l1 is not None:
            l3.next = ListNode((rest + l1.val) % 10)
            rest = (rest + l1.val) // 10
            l1, l3 = l1.next, l3.next
        while l2 is not None:
            l3.next = ListNode((rest + l2.val) % 10)
            rest = (rest + l2.val) // 10
            l2, l3 = l2.next, l3.next
        if rest == 1:
            l3.next = ListNode(1)
        return sentinel.next
