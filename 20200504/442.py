class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        dic = Counter(nums)

        result = set()
        for num in nums:
            if dic[num] == 2:
                result.add(num)

        return list(result)


test = Solution()
print(test.findDuplicates([4,3,2,7,8,2,3,1]))  #[2,3]


# 442. Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]