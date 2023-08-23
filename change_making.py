

def make_change_greedy(goal_amount=0):
    # list of available coins, sorted largest -> smallest (order matters)
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    coin_count = 0
    values = []
    for coin in denominations:
        # keep using the largest coin until there are no more coins
        while goal_amount >= coin:
            # decrement the amount by the coin used
            goal_amount -= coin
            # store the coin used
            values.append(coin)
            # increment the coin count
            coin_count += 1
    return coin_count, values


print(make_change_greedy(24))
print(make_change_greedy(163))
