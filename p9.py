#p9 : print Fibonacci sequence.

n=int(input("Enter Value :"))
num1 = 0
num2 = 1
next_num = num1 
count = 0

while count <= n:
	print(next_num,end=" ")
	count += 1
	num1 = num2
	num2 = next_num
	next_num = num1 + num2
print()
