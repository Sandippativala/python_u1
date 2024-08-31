# 1.for even numbers, divide by 2 :

n=int(input("Enter Number For Even:"))
print("-----Even Number-----")
for i in range(n) :
    if i%2==0 :
      print(i,end=" ")
print("\n-------------------")

# 2. for odd numbers, multiply by 3 and add 1. :

n1=int(input("Enter Number For Odd:"))
print("-----Odd Number-----")
for i in range(n1) :
    if i%2!=0 : 
        print(i,end=" ")
print("\n-------------------")

# 3.repeat above steps,until it become 1.
# input 7

no=int(7)

print(no,end=" ")

while(no!=1):
    if(no%2==0):
        no=int(no/2)
        print(no,end=" ")
    else:
        no=(no*3)+1
        print(no,end=" ")
