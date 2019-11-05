
# 14.Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # s'il n'y a pas d'élément dans la liste 'strs', retourner "" comme l'énoncé.
        if(len(strs) == 0):
            return ""
        # sinon, mettre le premier élément dans la variable 'min'
        else:
            min = strs[0]

        # Dans cette for loop, on cherche le plus court élément dans la liste 'strs'
        for i in range(len(strs)):
            if(len(min) > len(strs[i])):
                min = strs[i]

        # Dans cette double for loop, on compare les éléments dans la liste. 
        # Je vais expliquer avec exemple 1 de l'énoncé.
        
        # Example 1:
        # Input: ["flower","flow","flight"] 
        # Output: "fl"

        # On a déjà cherché le plus court élément dans la liste, c'est 'flow'
        # Comparer 'flow' et le premier élément 'flower', mais ici, en utilisant splice de python, 
        # on juste comparer 'flow' et les premiers 4 lettres de 'flower', c-a-dire 'flow'.
        # si ce n'est pas le même, on n'a pas besoin de comparer les autres donc, break.
        # si le même, on compare les autres aussi. 
        # Apres avoir fini de for loop de k, si concord est true, on retourne min[0:len(min)-j]
        # si concord est False, on compare à nouveau avec 'flo' de 'flow.  
        # ...
        # on compare à nouveau avec 'fl' de 'flow.  
        # on compare à nouveau avec 'f' de 'flow.  
        # s'il n'y a pas de corcordance jusce qu'à la fin, retourner "" comme l'énoncé.

        for j in range(len(min)):
            concord = True
            for k in range(len(strs)):
                if(min[0:len(min)-j] != strs[k][0:len(min)-j]):
                    concord = False
                    break
            if(concord == True):
                return min[0:len(min)-j]
        return ""


# Success
# Details 
# Runtime: 16 ms, faster than 91.76% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.9 MB, less than 78.75% of Python online submissions for Longest Common Prefix.

