# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head, list2 = list1, ListNode(next=list2)
        while list1.next is not None:
            if list2.next is not None and list2.next.val < list1.next.val:
                list2.next.next, list1.next, list2.next = list1.next, list2.next, list2.next.next
            list1 = list1.next
        list1.next = list2.next
        return head
