# 58. Length of Last Word

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word in the string.
# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # lorsqu'il y a " " à l'extremité, ca causera le problème pour mon algo, 
        # donc, supprimez l'espace à l'extremité de 's'
        # exemple "a ", on doit supprimer l'espace pour utiliser l'algo suivant.
        s = s.strip()
        # s'il n'y a pas de mots, c-a-d, s="", retourne 0
        if(len(s) == 0):
            return 0
        
        #reversez 's' et apres, on cherche premiere espace et retournez l'index de l'espace. 
        reversedS = s[::-1] 
        
        # mais, s'il n'y a pas d'espace de 's', il faut verifier s'il y a du mot sans espace
        if((reversedS.find(" ") == -1) and (len(reversedS) != 0)):
            return len(reversedS)
        
        length = reversedS.find(" ")
        return length;


# Success
# Details 
# Runtime: 12 ms, faster than 90.89% of Python online submissions for Length of Last Word.
# Memory Usage: 12.1 MB, less than 7.14% of Python online submissions for Length of Last Word.        