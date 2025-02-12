from math import sqrt

# Input and validation
n = int(input("Enter a number: "))  # Get user input
Prime_n = 0  # Counter for prime numbers
Perfect_n = 0  # Counter for perfect numbers

# Ensure the number is positive
while n < 0:
    print("Please enter a positive number")
    n = int(input("Enter a number: "))

# Loop from 1 to N
for i in range(1, n+1):
    # ------ Prime Number Check ------
    is_prime = True  # Assume number is prime
    for num in range(2, int(sqrt(i)) + 1):  # Check divisibility up to sqrt(i)
        if i % num == 0:
            is_prime = False  # Not a prime
            break  # Stop checking further
    if is_prime and i > 1:  # If number is prime, increment count
        Prime_n += 1

    # ------ Perfect Number Check ------
    sum_divisors = 1  # 1 is always a divisor (excluding itself)
    for div in range(2, int(sqrt(i)) + 1):  # Check divisibility up to sqrt(i)
        if i % div == 0:
            sum_divisors += div  # Add divisor
            if div != i // div:  # Check if the paired divisor is not the same as div
                sum_divisors += i // div
    if sum_divisors == i and i != 1:  # Check if sum of divisors equals the number
        Perfect_n += 1

# Output results
print("Number of prime numbers: ", Prime_n)
print("Number of perfect numbers: ", Perfect_n)
