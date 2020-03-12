# 1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. 
# The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 3:
# Input: head = [1]
# Output: 1

# Example 4:
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880

# Example 5:
# Input: head = [0,0]
# Output: 0

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):        
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = ''
        
        while head.next != None:
            result = result + str(head.val)
            head = head.next
        result = result + str(head.val)
        
        return int(result, 2)


# Explication. 

# J'ai un peu de difficulté de ca même si c'est le niveau 'Easy'. 
# En faisant ca, j'ai réalisé que la concatenation int + str ne marche pas. 
# Donc, on doit utiliser cast pour la concatenation de int type + str type. 
# En plus, 
# int(str en integer, 2) veut dire que le str en int est binaire. et ca changera en decimal apres int(). 
# par exemple, int('110', 2) = 6 / int('21', 8) = 17. 


