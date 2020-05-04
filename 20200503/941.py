class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if (len(A) < 3):
            return False

        max = 0

        for i in range(len(A)):
            if (A[i] > max):
                max = A[i]

        max_index = A.index(max)

        if max_index == 0 or max_index == len(A)-1:
            return False

        for i in range(max_index):
            if (A[i] >= A[i + 1]):
                return False

        for i in range(max_index, len(A) - 1):
            if (A[i] <= A[i + 1]):
                return False

        return True

test = Solution()
print(test.validMountainArray([2,0,2])) #false
print(test.validMountainArray([0,1,2,3,4,5,6,7,8,9])) #false
print(test.validMountainArray([0,1,2,1,2])) #false

# in my code, for the mountain array, the data need to have more than 2 elements.
# and I found the max. max does not have to be first index or last index.
# I use max index as a criteria for increasing elements having index from 0 to max,
# and for decreasing elements having index from max to last index.

# 941. Valid Mountain Array
# Given an array A of integers, return true if and only if it is a valid mountain array.
#
# Recall that A is a mountain array if and only if:
#
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
#
# Example 1:
# Input: [2, 1]
# Output: false
#
# Example 2:
# Input: [3, 5, 5]
# Output: false
#
# Example 3:
# Input: [0, 3, 2, 1]
# Output: true
#
# Note:
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000