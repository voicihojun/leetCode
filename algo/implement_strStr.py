# 28. Implement strStr()

# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2


# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().



class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        return haystack.find(needle)

print(Solution().strStr("heeello", "ll")) #réponse = 4


# Explication

# Dans le langage de python, il y a deux methodes internaux pour chercher l'index de certain string. 
# find et index. Dans ce problème-ci, on a à utiliser find, car si on utilise index, quand il n'y a pas d'occurence 
# dans haystack, il retourne Error. Mais, find retourne -1 comme l'énoncé. 



