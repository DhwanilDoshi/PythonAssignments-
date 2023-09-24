def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


num = int(input("enter a number: "))

if num < 0:
	print("number is invalid")

i = 0

print("fibonacci series: ")

for i in range(0, num):
	print(fibonacci(i))