n=int(input("Enter Perfect Number :"))
sum1=0
for i in range(1,n):
    if n%i==0 :
        print(i,end="+")
        sum1=sum1+i

if n==sum1 :
    print("\n-----------------------------------")
    print("{0} Is A Prefect Number.".format(n))
    print("-----------------------------------")
else :
    print("\n-----------------------------------")
    print("{0} Is A Not Perfect Number....!".format(n))
    print("-----------------------------------")