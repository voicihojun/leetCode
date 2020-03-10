
# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         flag = True
#         for i in range(len(prices) - 1):
#             if(prices[i] > prices[i+1]):
#                 flag = True
#             else:
#                 flag = False
#                 break;
        
#         if(flag == True):
#             return 0
                
#         bestProfit = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if(prices[j] - prices[i] > 0):
#                     profit = prices[j] - prices[i]
#                     if(profit > bestProfit):
#                         bestProfit = profit
#         return bestProfit
##        ca ne marche pas à cause de 'Time limit exceeded'.
        
        minPrice = sys.maxint
        maxProfit = 0
        
        for i in range(len(prices)):
            if(prices[i] < minPrice):
                minPrice = prices[i]
            elif(prices[i] - minPrice > maxProfit):
                maxProfit = prices[i] - minPrice
        
        return maxProfit



# Success
# Details 
# Runtime: 36 ms, faster than 99.55% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 12.8 MB, less than 13.76% of Python online submissions for Best Time to Buy and Sell Stock.