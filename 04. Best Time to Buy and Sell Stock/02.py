class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        # Using ifs in Python is faster than using min() and max()
        for price_today in prices:
            if price_today < buy_price:
                buy_price = price_today
            else:
                if price_today - buy_price > profit:
                    profit = price_today - buy_price

        return profit