class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in A:
            result.append(i * i)

        result.sort()
        return result


test = Solution()

print(test.sortedSquares([-4,-1,0,3,10]))  #[0,1,9,16,100]
print(test.sortedSquares([-7,-3,2,3,11]))  #[4,9,9,49,121]


# 977. Squares of a Sorted Array
#
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#
# Example 1:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
# Example 2:
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
