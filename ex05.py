"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
"""import math

print(4 // math.gcd(4, 3))


def compute():
    ans = 1
    for i in range(1, 21):
        ans *= i // math.gcd(i, ans)
    return str(ans)


if __name__ == "__main__":
	print(compute())"""


def divisivelpor20(numero):
    for i in range(2, 21):
        if numero % i != 0: return False
    return True


numero = 20
while True:
    if divisivelpor20(numero): break
    numero += 20

print(numero)