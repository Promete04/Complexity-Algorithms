# Knapsack Problem
def kanpsack_2_saddles(weight1,weight2,treasure_profit, treasure_weight):

    def knapsack(treasure_profit, treasure_weight, max_weight_saddles):
        n = len(treasure_profit)

        # K[i][w] will hold the maximum value of the first i items with a maximum weight w
        K = [[0 for _ in range(max_weight_saddles + 1)] for _ in range(n + 1)]

        # Build the K array
        for i in range(1, n + 1): # Iterate through each item
            for w in range(max_weight_saddles + 1): # Iterate through each weight
                # If the weight of the current item is less than or equal to the current weight w
                # we have two options: include the item or not
                if treasure_weight[i - 1] <= w: # We check if the current item could be included in the knapsack if it were empty
                     K[i][w] = max(K[i - 1][w], K[i - 1][w - treasure_weight[i - 1]] + treasure_profit[i - 1]) 
                else: # If the weight of the current item is greater than the current weight w, we cannot include it
                    K[i][w] = K[i - 1][w]

        # Remove from treasure_profit and treasure_weight the items that were included in the knapsack
        itemsLeftProfit = []
        itemsLeftWeight = []
        w = max_weight_saddles
        for i in range(n, 0, -1): # Iterate through the items in reverse order
            # If the current item was included in the knapsack
            if K[i][w] != K[i - 1][w]: # If the value is different, it means the item was included
                itemsLeftProfit.append(treasure_profit[i - 1])
                itemsLeftWeight.append(treasure_weight[i - 1])
                w -= treasure_weight[i - 1] # Decrease the weight by the weight of the included item
            else: # If the value is the same, it means the item was not included
                itemsLeftProfit.append(0)
                itemsLeftWeight.append(0)
        itemsLeftProfit.reverse() # Reverse to get the correct order
        itemsLeftWeight.reverse()
        # Return the maximum profit and the remaining items
        return K[n][max_weight_saddles], itemsLeftProfit, itemsLeftWeight
    
    
    

    # Call the knapsack function for both saddles in both orders
    max_profit11, itemsLeftProfit, itemsLeftWeight = knapsack(treasure_profit, treasure_weight, weight1)
    max_profit12, itemsLeftProfit, itemsLeftWeight = knapsack(itemsLeftProfit, itemsLeftWeight, weight2)

    max_profit21, itemsLeftProfit, itemsLeftWeight = knapsack(treasure_profit, treasure_weight, weight2)
    max_profit22, itemsLeftProfit, itemsLeftWeight = knapsack(itemsLeftProfit, itemsLeftWeight, weight1)

    max_profit = max(max_profit11 + max_profit12, max_profit21 + max_profit22)
    print("Maximum profit:", max_profit)

# Example data
treasure_profit = [1,6,4,6,2,4,6,7,4,8,9,5,3,2,1,5,4,3,2,1]
treasure_weight = [2,5,7,4,3,1,4,5,7,9,6,2,5,7,9,5,3,2,5,7]

weightSaddle1 = 2
weightSaddle2 = 8

# Call the knapsack function
kanpsack_2_saddles(weightSaddle1, weightSaddle2, treasure_profit, treasure_weight)


 




