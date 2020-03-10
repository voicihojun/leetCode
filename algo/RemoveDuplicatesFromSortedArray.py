# 26. Remove Duplicates from Sorted Array

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.


# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.


# Clarification:

# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        i = 0
        length = 1
        
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                length += 1
                 
        return length


# Explication

# La première condition est qu'il n'y pas d'élément dans la list de nums. Dans ce cas, ca doit retourner la length 0. 
# sinon, on pense que, au moins, un élément est dedans. alors, length sera 1 dans ce cas. Et puis, on doit mettre 
# un variable i = 0 pour utiliser cela tel qu'un pointer. 
# Dans la boucle de for, on compare nums[i] et nums[j]. 

# par exemple, 
# [1,1,2,3,3]

# on commence par, i = 0 et j = 1,

# i = 0, j = 1. Dans ce cas, pas de changement, car nums[i] et nums[j] sont le même.
# 			  mais j sera 2 à la prochaine boucle. 

# i = 0, j = 2  nums[i] = 1 et nums[j] = 2. Alors, i sera 1. Et la place de la list va changer aussi comme dessous.
# 			  on doit changer la place des nums[1] et nums[2]
# 			  [1,1,2,3,3] --> [1,2,1,3,3]
			  
# i = 1, j = 3  nums[i] = 2 et nums[j] = 3. Alors, i sera 2. on doit changer la place des nums[2] et nums[3]
# 			  [1,2,1,3,3] --> [1,2,3,1,3]
			  
# i = 2, j = 4  rien changer, car nums[i] == nums[j]


# on a du changer la place deux fois. Donc, la length va etre 3. 
# Et la list sera = [1,2,3,1,3]

# En utilisant for i in range(len(length)), il va imprimer [1,2,3]

