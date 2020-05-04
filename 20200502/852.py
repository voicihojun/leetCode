class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        prev = 0
        if(A[0] < A[len(A)-1]):
            for i in range(len(A)):
                if(i == 0):
                    prev = A[i]
                else:
                    if(prev <= A[i]):
                        prev = A[i]
                    else:
                        return False
        elif(A[0] > A[len(A)-1]):
            for i in range(len(A)):
                if(i == 0):
                    prev = A[i]
                else:
                    if(prev >= A[i]):
                        prev = A[i]
                    else:
                        return False
        else:
            for i in range(len(A)):
                if(i == 0):
                    prev = A[i]
                else:
                    if(prev == A[i]):
                        prev = A[i]
                    else:
                        return False
        return True


test = Solution()
print(test.peakIndexInMountainArray([0,1,0]))  #1
print(test.peakIndexInMountainArray([0,2,1,0]))  #1
print(test.peakIndexInMountainArray([0,2,4,5,1,0]))  #3


# 852. Peak Index in a Mountain Array
# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
# Example 1:
#
# Input: [0,1,0]
# Output: 1
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1