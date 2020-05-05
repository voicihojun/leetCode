

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if(k < 0):
            return 0

        from collections import Counter
        nums_dict = Counter(nums)

        count = 0

        for num in set(nums):
            if num+k in nums_dict:
                if k==0 and nums_dict[num] > 1:
                    count += 1
                if k!=0:
                    count += 1
        return count


test = Solution()
print(test.findPairs([3,1,4,1,5], 2)) #2
print(test.findPairs([1,3,1,5,4], 0)) #1
print(test.findPairs([1,2,3,4,5], -1)) #0


# my comment
# i used the below code for the first time. but for the huge of data, it causes time limit problem for 62nd test of 77.
# So, i used the above code to avoid the time limit problem. In using Counter, i learned the property of dict and Counter.

# class Solution(object):
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#
#         ensemble = set()
#         print(type(ensemble))
#         # print(ensemble)
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if abs(nums[i] - nums[j]) == k:
#                     ensemble.add(frozenset([nums[i], nums[j]]))
#
#         # print(ensemble)
#         return len(ensemble)


# 532. K-diff Pairs in an Array
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
#
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
#
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
#
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
#
# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].