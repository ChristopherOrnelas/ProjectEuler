"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""


def prime_counter(number):
	count = 1
	n = 1
	while count < number:
		n += 2
		if prime_number(n):
			count += 1
	return n


def prime_number(number):
	for c in range(2, number):
		if number % c == 0:
			return False
	return True


print(prime_counter(10001))

