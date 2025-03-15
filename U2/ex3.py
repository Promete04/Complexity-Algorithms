import random

def find_min_max(arr):
    # Step 1: Check for empty array
    if not arr:
        raise ValueError("The array should not be empty")

    n = len(arr)
    
    # Step 2: Initialize variables
    if n == 1:
        return arr[0], arr[0]

    # Step 3: Initial comparison
    if n % 2 == 0: # If even number of elements
        if arr[0] < arr[1]:  
            min_elem, max_elem = arr[0], arr[1]
        else:
            min_elem, max_elem = arr[1], arr[0]
        i = 2
    else: # If odd number of elements
        min_elem = max_elem = arr[0]
        i = 1

    # Step 4: Pairwise comparison
    while i < n - 1: 
        # Compare in pairs to reduce the number of comparisons
        # Compare the smaller element with the min_elem 
        # and the larger element with the max_elem
        if arr[i] < arr[i + 1]: 
            min_elem = min(min_elem, arr[i]) 
            max_elem = max(max_elem, arr[i + 1])
        else:
            min_elem = min(min_elem, arr[i + 1])
            max_elem = max(max_elem, arr[i])
        i += 2

    # Step 5: Return results
    return min_elem, max_elem

# Example usage
V = [3, 5, 1, 2, 4, 8]
min_val, max_val = find_min_max(V)
print(f"Minimum: {min_val}, Maximum: {max_val}")

# Generate a large array with 1,000,000 random integers
large_array = [random.randint(1, 100000000) for _ in range(1000000)]

# Find the minimum and maximum values in the large array
min_val, max_val = find_min_max(large_array)
print(f"Minimum: {min_val}, Maximum: {max_val}")