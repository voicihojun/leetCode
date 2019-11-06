# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

  #       s'il y a une parenthèse fermée, 
  #       il y a sûrement une parenthèse ouverte juste avant une parenthèse fermée.

  #       par exemple, 

  #       {[[[[(())]]]]}
  #              )	celle-ci est première parenthèse fermée, donc il y a une parenthèse ouverte juste avant.

		# pour les autres exemples, on pourra mettre la même règle. 
		

        openParentheses = ["(","[","{"]
        closeParentheses = [")","]","}"]
        stack = []

        # toujours, s sera pair. donc, sinon, on retourne False
        if(len(s) % 2 == 1):
            return False
        
        # en utilisant for loop, s'il y a des éléments dans 'openParentheses'
        # on va mettre cela dans stack, 
        # s'il y a des élément dans 'closeParentheses', 
        # premièrement, on va verifier la longeur de stack, car s'il y a pas de choses dans stack, 
        # ca veut dire, sans ouvrir la parenthèse, on ferme. Alors, c'est False. 
        # Ensuite, on va valider si les parentheses sont une paire.
        # A la fin, on va faire le pop pour 'stack'.
        # Après avoir fini for loop, si la longeur de stack est égale à 0, True. sinon, False. 

        for i in range(len(s)):
            if s[i] in openParentheses:
                stack.append(s[i])
            elif s[i] in closeParentheses:
                if(len(stack) == 0):
                    return False
                elif(openParentheses.index(stack[-1]) == closeParentheses.index(s[i])):
                    stack.pop()
                else:
                    return False
        if(len(stack) == 0):
            return True
        return False


# Success
# Details 
# Runtime: 24 ms, faster than 29.29% of Python online submissions for Valid Parentheses.
# Memory Usage: 12 MB, less than 5.04% of Python online submissions for Valid Parentheses.