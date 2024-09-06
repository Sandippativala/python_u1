n=int(input("Enter Perfect Number :"))
sum1=0
for i in range(1,n):
    if n%i==0 :
        print(i,end="+")
        sum1=sum1+i

if n==sum1 :
    print("\n-----------------------------------")
    print("Prefect Number : {1}".format(n))
    print("-----------------------------------")
else :
    print("\n-----------------------------------")
    print("This Is Not Perfect Number :{0}".format(n))
    print("-----------------------------------")