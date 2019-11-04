# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.



class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x > 0):
            x = str(x)
            x = int(x[::-1])
            if(x < -2**31 or x > 2**31 - 1):
                return 0
            return x
        elif(x < 0):
            x = -x
            x = str(x)
            x = "-" + x[::-1]
            x = int(x)
            if(x < -2**31 or x > 2**31 - 1):
                return 0
            return x    
        else:
            return 0
        

# Success
# Details 
# Runtime: 20 ms, faster than 61.24% of Python online submissions for Reverse Integer.
# Memory Usage: 11.8 MB, less than 25.81% of Python online submissions for Reverse Integer.



########## EXPLICATION ##########
# si x est positif,
# changer le type de x en String. 
# utilisant le propriété de String, reverser et change le type de x en Integer à nouveau. 
# si x est négatif, 
# avant change le type de x en String. 
# on change - en +. apres avoir reversé, on ajoute -. 

# avant de retourner, vérifier si x est dans le bon champ. 






