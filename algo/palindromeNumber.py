# 9. Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if(x < 0):
        #     return False
        # x = str(x)
        # num = len(x) // 2
        # for i in range(num):
        #     if (x[i] != x[len(x) - 1 - i]):
        #         return False
        # return True
                
        return str(x) == str(x)[::-1]

# Success
# Details 
# Runtime: 40 ms, faster than 91.33% of Python online submissions for Palindrome Number.
# Memory Usage: 11.9 MB, less than 15.66% of Python online submissions for Palindrome Number.

############### EXPLICATION ###############
# 1)
# juste changer integer x en String x, et après, 
# comparer la valeur de l'indice i avec la valeur de l'indice longeur -1 -i de String tour à tour.  

# 2) 
# changer integer x en string. 
# reverser x en utilisant [::-1] de String. 
# comparer x et x[::-1] si cest le meme. 







