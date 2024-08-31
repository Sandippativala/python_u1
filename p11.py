# p11 : given a positive integer,check if the number is prime or not.

no=int(input("Enter any positive number :"))
for i in range(2,int(no/2+1)):
    if(no%i==0):
        break
if(i==int(no/2)):
    print(no," number is Prime")
else:
    print(no," number is not Prime")
            