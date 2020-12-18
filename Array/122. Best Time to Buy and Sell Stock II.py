'''
122. Best Time to Buy and Sell Stock II
Array, Greedy

Description:
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Similar Questions:
Best Time to Buy and Sell Stock - Easy
Best Time to Buy and Sell Stock III - Hard
Best Time to Buy and Sell Stock IV - Hard
Best Time to Buy and Sell Stock with Cooldown - Medium
Best Time to Buy and Sell Stock with Transaction Fee - Medium
'''

# Solution:
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        '''
        Method 1: Search for the number of vertices.
                  If there is only one vertex and it is at the beginning of the array, then the profit is 0.
                  If there is only one vertex and it is at the end of the array, then the profit is vertex - min(prices).
                  If there are multiple vertices, for each vertex, we save vertex - previous number. And sum up all the transactions at the end.
        '''
        profit = 0
        if len(prices) < 2:
            return profit
        
        buy = prices[0]
        for i in range(1, len(prices)):
            buy = min(prices[i], buy)
            if i == len(prices) - 1 and prices[i] >= prices[i - 1]:
                profit += prices[i] - buy
            elif i == len(prices) - 1 and prices[i] < prices[i - 1]:
                profit = profit
            elif prices[i] > prices[i + 1]:
                profit += prices[i] - buy
                print(profit, prices[i], buy)
                buy = prices[i]
                print(buy)
        
        if profit == 0 and prices[0] == max(prices):
            return profit
        if profit == 0 and prices[-1] == max(prices):
            return max(prices) - min(prices)
        return profit
    
    
        '''
        Method 2: Simply search for buy and sell value (i.e., valley and peak).
                  The total profit is the summation of all possible difference between peak and valley.
        '''
        profit = 0
        buy = prices[0]
        sell = prices[0]
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell = prices[i]
            profit += sell - buy
        return profit
        
        
        '''
        Method 3: Simply add the increasement at each step if the value is increasing.
        '''
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit
    

