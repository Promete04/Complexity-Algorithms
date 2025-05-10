
def find_max_shared_substring(A, B):
    # Create a 2D array to store the lengths of longest common subsequences
    m = len(A)
    n = len(B)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the L array
    for i in range(1, m + 1): # Iterate through each element of A
        for j in range(1, n + 1): # Iterate through each element of B
            # If the current elements of A and B match, increment the length of the common subsequence
            if A[i - 1] == B[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1 # Increment the length of the common subsequence
            # If they do not match, take the maximum length from the previous elements
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1]) # The maximum length is the maximum of the two previous lengths (previous row or previous column)

    # Length of the longest common subsequence
    length = L[m][n]

    # Backtrack to find the common subsequence
    i, j = m, n
    common_subsequence = []
    while i > 0 and j > 0: # Backtrack through the L array
        if A[i - 1] == B[j - 1]: # If the current elements of A and B match, it is part of the common subsequence
            common_subsequence.append(A[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]: # If the value above is greater, move up
            i -= 1
        else: # If the value to the left is greater, move left
            j -= 1

    common_subsequence.reverse() # Reverse to get the correct order

    return length, common_subsequence


A = [0,1,1,0,1,0,1,0]
B = [1,0,1,0,0,1,0,0,1]

l, s= find_max_shared_substring(A, B)
print("Length of longest common subsequence:", l)
print("Longest common subsequence:", s)
