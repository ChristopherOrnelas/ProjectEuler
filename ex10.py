'''the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''


def sumPrimes(n):
    total = 0
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            total += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return total


print(sumPrimes(2000000))
