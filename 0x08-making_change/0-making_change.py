#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total) -> int:
    """determine the fewest number
    of coins needed to meet a
    given amount total
        coins: a list of the values of the
            coins in your possession
        total: the total to meet
    Return: fewest number of coins needed to meet total
    """
    # if total <= 0:
    #     return 0
    #
    # dp = [float('inf')] * (total + 1)
    # dp[0] = 0
    #
    # for coin in coins:
    #     for amount in range(coin, total + 1):
    #         dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    #
    # return dp[total] if dp[total] != float('inf') else -1
    if total <= 0:
        return 0

    current_total = total
    index = 0
    coins_count = 0
    sorted_coins = sorted(coins, reverse=True)
    coins_len = len(coins)

    while current_total > 0:
        if index >= coins_len:
            return -1

        if current_total - sorted_coins[index] >= 0:
            current_total -= sorted_coins[index]
            coins_count += 1
        else:
            index += 1

    return coins_count
