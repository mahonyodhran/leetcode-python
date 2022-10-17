"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
            else:
                left = right
            right += 1
        return max_profit
    
sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4])) #5
print(sol.maxProfit([7,6,4,3,1])) #0

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Runtime: 2900 ms, faster than 12.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 7.02% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""