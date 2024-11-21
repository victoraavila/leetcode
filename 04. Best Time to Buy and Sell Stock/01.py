class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 10001
        max = 0
        for i, elem_i in enumerate(prices):
            if elem_i < min:
                min = elem_i
                continue
            else:
                # The current element is greater or equal than the minimum (it is an opportunity to sell)
                if elem_i - min > max:
                    # This opportunity to sell is better than the best opportunity seen before
                    max = elem_i - min

        return max
