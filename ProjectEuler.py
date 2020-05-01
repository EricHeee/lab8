# Finds the multiples of 3 and 5 under 1000
def multiples():
    
    li = []

    # If num mod 3 or mod 5 equals 0, it must be a multiple of either 3 or 5 or both.
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            li.append(num)
    
    return li


   
