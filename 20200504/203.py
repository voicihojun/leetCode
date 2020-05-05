# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while (head != None and head.val == val):
            head = head.next

        current_node = head

        while (current_node != None and current_node.next != None):
            if (current_node.next.val == val):
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return head

# my comment:
# when seeing the below example, if the next one of a current node equal to the value,
# current_node.next = current_node.next.next. if not  current_node = current_node.next.
# but there is exceptional one. if the current node is that value, we need to remove it.
# So, at first, we need to put head to head.next if the current node is that value.


# 203. Remove Linked List Elements
# Remove all elements from a linked list of integers that have value val.
#
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5