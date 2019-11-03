
# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


	




class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for x in range(len(nums)):
            for y in range(nums.index(nums[x])+1, len(nums)):
                if(nums[x] + nums[y] == target):
                    return [x, y]

        return -1
        # Success
		# Details 
		# Runtime: 4976 ms, faster than 12.11% of Python online submissions for Two Sum.
		# Memory Usage: 12.4 MB, less than 98.97% of Python online submissions for Two Sum.

		############## EXPLICATION ##################
		# c'est simple de faire le coding comme celui-ci. 
		# c'est chercher le target de toutes les possibilités.

		# exemple)
		# [1,2,3] 
		# (1,2), (1,3), (2,3) =  toutes les possibilités pour 3 éléments, car 3C2 = 3. 
		# si list est [1,2,3,4], 4C2 = 6. 

		# si on cherche le target, retourner list de index, sinon -1.
