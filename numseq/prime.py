def primes(n):
    ''' returns list of primes less than n'''
    primes = []
    for num in range(2,n):
        if all(num%i!=0 for i in range(2,num)):
            primes.append(num)
    return primes

def is_prime(m):
    '''returns True if m is prime'''
    if (m <= 1) : 
        return False
    if (m <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (m % 2 == 0 or m % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= m) : 
        if (m % i == 0 or m % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
