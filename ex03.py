"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?"""

def largest_prime_factor(number):
    factor = 2
    while factor < number:
        if number % factor == 0:
            number /= factor
            factor = 1
        factor += 1
    print(number)

    """for c in range(2, number):
        if number % c == 0:
            if prime_number(c):
                print(c)"""



"""def prime_number(number):
    for c in range(2, number):
        if number % c == 0:
            return False
    return True"""

largest_prime_factor(600851475143)
