def merge_and_fuse(A, originalSize):
    # Check if this is the top-level call
    Father = len(A) == originalSize
    if len(A) < 2:
        return A, 0  # Base case: no inversions in a single-element array

    # Split the array and recursively count inversions
    mid = len(A) // 2
    B, left_inv = merge_and_fuse(A[:mid], originalSize)
    C, right_inv = merge_and_fuse(A[mid:], originalSize)
    merged, split_inv = fuse_count(B, C)
    
    # Calculate total inversions
    total_inv = left_inv + right_inv + split_inv
    if Father:
        total_inv += 1  # Increment for the top-level call
    
    return merged, total_inv

def fuse_count(B, C):
    # Merge two sorted arrays and count split inversions
    i, j = 0, 0
    merged = []
    inv_count = 0

    while i < len(B) and j < len(C): 
        if B[i] <= C[j]:
            merged.append(B[i])
            i += 1
        else:
            merged.append(C[j])
            j += 1
            inv_count += 1  # Count inversions

    # Add remaining elements
    merged.extend(B[i:])
    merged.extend(C[j:])
    
    return merged, inv_count

# Example usage
A = [1, 2, 7, 3, 4, 5, 6]
sorted_A, inversions = merge_and_fuse(A, len(A))
print(f"Number of inversions: {inversions}")

A = [1, 7, 2, 3, 4, 5, 6]
sorted_A, inversions = merge_and_fuse(A, len(A))
print(f"Number of inversions: {inversions}")

