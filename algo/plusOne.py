
# 66. Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # apres avoir changé tous les integers dans digits en String, 
        # concatenez les elements en String. 
        # apres avoir changé le type de String à Integer, ajouter 1. 
        # Ensuite, changez le type de Integer à String. mettre les dans une liste. 
        # changez le type des elements dans la liste de STring à Integer.
        result = ""
        for element in digits:
            result += str(element)
        
        num = int(result) + 1
        
        result = list(str(num))
        for i in range(len(result)):
            result[i] = int(result[i])
        return result





# Success
# Details 
# Runtime: 12 ms, faster than 96.80% of Python online submissions for Plus One.
# Memory Usage: 11.8 MB, less than 29.17% of Python online submissions for Plus One.