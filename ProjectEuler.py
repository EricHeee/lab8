# Finds the multiples of 3 and 5 under 1000
def multiples():
    
    li = []

    # If num mod 3 or mod 5 equals 0, it must be a multiple of either 3 or 5 or both.
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            li.append(num)
    
    return li



# Checks if a number n is a prime or not
def isPrime(n):
    i = 2
    
    # If n equals 1 or 2 it is definately a prime number
    if n == 1 or n == 2:
        return True
    
    # Divide n with i to see if n mod i is 0 or not. If not, n is a prime.
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True
