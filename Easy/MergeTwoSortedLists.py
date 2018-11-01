'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = []

        while (l1 is not None or l2 is not None):

            # Check if L1 or L2 is empty
            if (l1 is None):
                while (l2 is not None):
                    new_list.append(l2.val)
                    l2 = l2.next
                break
            elif (l2 is None):
                while (l1 is not None):
                    new_list.append(l1.val)
                    l1 = l1.next
                break

            if (l1.val <= l2.val):
                new_list.append(l1.val)
                l1 = l1.next
            else:
                new_list.append(l2.val)
                l2 = l2.next

        return new_list