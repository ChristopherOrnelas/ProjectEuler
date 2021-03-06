"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def palindrome():
	res = 0
	for c in range(100, 1000):
		for d in range(100, 1000):
			if str(c*d) == str(c*d)[::-1]:
				if c*d > res:
					res = c*d
	return res
print(palindrome())



"""
Outra possibilidade
def compute():
	ans = max(i * j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[ : : -1])
	return str(ans)


print(compute())"""