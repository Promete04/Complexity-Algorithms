n = int(input("Enter a number: "))

def fact_sum(n):
    sum = 0 # Initialize sum to 0
    if n==0: # Base case: if n is 0, return 0
        return sum
    else: # Recursive case: add n to the sum of the fac_sum(n-1)
        sum=n+fact_sum(n-1) 
    return sum

print(fact_sum(n))

