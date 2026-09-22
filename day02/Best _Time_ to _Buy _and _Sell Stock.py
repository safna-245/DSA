def maxProfit(prices):

        buy = prices[0]
        profit = 0

        for price in prices:

            if price < buy:

                buy = price

            else:

                curr_profit = price - buy

                if curr_profit > profit:

                    profit = curr_profit

        return profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))