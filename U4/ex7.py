"""
A sequence of bits A is defined as a sequence A={a1, a2,..., an} where each ai can take the
value 0 or the value 1, and n is the length of the sequence A. From a sequence it is defined
a subsequence X of A as X = {x1, x2,..., xk}, where kn, so that X can be obtained by
eliminating some element of A but respecting the order in which the bits appear; for
example, if A={1,0,1,1,0,0,1} we could obtain as subsequences {1,1,1,0,1}, {1,0,1} or
{1,1,0,0} among others, but you could never get the subsequence {1,0,0,1,1}.
Given two sequences A and B, X is called a common subsequence of A and B when X is
a subsequence of A and is also a subsequence of B. (although they may have been
obtained by removing different elements in A than B, and even different quantities of
elements). Assuming the sequences A = {0,1,1,0,1,0,1,0} and B = {1,0,1,0,0,1,0,0,1}, a
common subsequence would be X = {1,1,0,1}, but it could not be X = {0,1,1,1,0}.
We want to determine the common subsequence of two sequences A and B that have the
maximum length, for which it is requested
• explain in detail how to solve the problem, and
• make a Dynamic Programming algorithm that obtains the maximum possible
length and a common sequence of that length."""

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
