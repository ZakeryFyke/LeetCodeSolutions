# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        full_list = []

        for L in lists:

            while L:
                full_list.append(L.val)
                L = L.next

        full_list.sort()
        return full_list