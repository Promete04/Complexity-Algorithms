n = int(input("Enter a number: "))

def fact_sum(n):
    sum = 0
    if n==0:
        return sum
    else:
        sum=n+fact_sum(n-1)
    return sum

print(fact_sum(n))

