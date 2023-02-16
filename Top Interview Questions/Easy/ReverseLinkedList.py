# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        if head == None: return None
        temp, head.next = head.next, None
        while temp != None:
            temp.next, temp, head = head, temp.next, temp
        return head
