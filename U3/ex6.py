def find_fake_coin(coins, start_index=0):
    n = len(coins)
    #####BASE_CASES#####
    if n == 1:
        return start_index, "unknown"  # Only one coin, it must be the fake one, but we don't know if it weighs more or less
    elif n == 2:
        return "We can't know, add real coin to find the fake coin"  # Two coins, one is fake but we can't determine which
    elif n == 3:  # Three coins, one is fake, we can determine which one
        if coins[0] == coins[1]:
            if coins[2] > coins[0]:
                return start_index + 2, "more"
            else:
                return start_index + 2, "less"
        elif coins[0] == coins[2]:
            if coins[1] > coins[0]:
                return start_index + 1, "more"
            else:
                return start_index + 1, "less"
        else:
            if coins[0] > coins[1]:
                return start_index, "more"
            else:
                return start_index, "less"
    elif n == 4:  # Four coins, one is fake, we can determine which one
        if coins[0] == coins[1] == coins[2]:
            if coins[3] > coins[0]:
                return start_index + 3, "more"
            else:
                return start_index + 3, "less"
        elif coins[0] == coins[1] == coins[3]:
            if coins[2] > coins[0]:
                return start_index + 2, "more"
            else:
                return start_index + 2, "less"
        elif coins[0] == coins[2] == coins[3]:
            if coins[1] > coins[0]:
                return start_index + 1, "more"
            else:
                return start_index + 1, "less"
        elif coins[1] == coins[2] == coins[3]:
            if coins[0] > coins[1]:
                return start_index, "more"
            else:
                return start_index, "less"
    else:  # More than four coins, we can divide and conquer
        mid = n // 2
        left_coins = coins[:mid + 1]
        right_coins = coins[mid:]

        left_mid = len(left_coins) // 2

        left_left_coins_weight = left_coins[:left_mid]
        left_right_coins_weight = left_coins[left_mid:]

        if sum(left_left_coins_weight) == sum(left_right_coins_weight):
            return find_fake_coin(right_coins, start_index + mid)
        else:
            return find_fake_coin(left_coins, start_index)

# Example usage
coins = [1, 1, 1, 1, 1,.33, 1, 1, 1, 1]  # Example coins with one fake coin (0.33)
position, weight_comparison = find_fake_coin(coins)
print(f"The fake coin is at position {position} and it weighs {weight_comparison}")

