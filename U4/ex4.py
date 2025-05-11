
def knapsack(treasure_profit, treasure_weight, max_weight_saddles):
    n = len(treasure_profit)

    # Create a 2D array to store the maximum value at each i (number of items) and w (max weight)
    # Initialize the K array with 0s
    # K[i][w] will hold the maximum value of the first i items with a maximum weight w
    K = [[0 for _ in range(max_weight_saddles + 1)] for _ in range(n + 1)]

    # Build the K array
    for i in range(1, n + 1): # Iterate through each item
        for w in range(max_weight_saddles + 1): # Iterate through each weight
            # If the weight of the current item is less than or equal to the current weight w
            # we have two options: include the item or not
            if treasure_weight[i - 1] <= w: # We check if the current item could be included in the knapsack if it were empty
                # We take the maximum of including the item or not including it
                # K[i - 1][w] is the max value without including the current item, so the previous value
                # K[i - 1][w - treasure_weight[i - 1]] + treasure_profit[i - 1] is the max value including the current item
                K[i][w] = max(K[i - 1][w], K[i - 1][w - treasure_weight[i - 1]] + treasure_profit[i - 1]) 

            else: # If the weight of the current item is greater than the current weight w, we cannot include it
                K[i][w] = K[i - 1][w]

    return K[n][max_weight_saddles], K

# Example data
treasure_profit = [1,6,4,6,2,4,6,7,4,8,9,5,3,2,1,5,4,3,2,1]
treasure_weight = [2,5,7,4,3,1,4,5,7,9,6,2,5,7,9,5,3,2,5,7]

max_weight_saddles = 10

# Call the knapsack function
max_profit, K = knapsack(treasure_profit, treasure_weight, max_weight_saddles)
print("Maximum profit:", max_profit)
# Print the matrix K in a nice format
print("K matrix:")
for i in range(len(K)):
    for j in range(len(K[i])):
        print(f"{K[i][j]:3}", end=" ")
    print()




