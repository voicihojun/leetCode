# 67. Add Binary

# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # on peut creer integer en utilisant la fonction int(string en binaire, 2)
        intA = int(a, 2)
        intB = int(b, 2)
        result = intA + intB
        # bin(integer) crée le string en binaire avec "0b"
        # par exemble, bin(2) => "0b10", donc par [2::], 
        # on utilise ce dont on besoin.
        return bin(result)[2::]




# Success
# Details 
# Runtime: 12 ms, faster than 98.45% of Python online submissions for Add Binary.
# Memory Usage: 11.7 MB, less than 65.79% of Python online submissions for Add Binary.