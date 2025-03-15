def merge_and_fuse(A):
    if len(A) < 2:
        return A, 0

    mid = len(A) // 2
    B, left_inv = merge_and_fuse(A[:mid])
    C, right_inv = merge_and_fuse(A[mid:])
    merged, split_inv = fuse_count(B, C)

    return merged, left_inv + right_inv + split_inv

def fuse_count(B, C):
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
            inv_count += 1

    # Add remaining elements of B (if any)
    merged.extend(B[i:])
    # Add remaining elements of C (if any)
    merged.extend(C[j:])
    
    return merged, inv_count

A = [1,2,7,3,4,5,6]
sorted_A, inversions = merge_and_fuse(A)
print(f"Number of inversions: {inversions}")
