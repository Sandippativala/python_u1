lst1=()
lst1 = (int(item) for item in input("Enter the list items : ").split())

# sort a list.
lst1.sort()

#print a sorted list.
print("\nYour Sorted List :",lst1)

num=int(input("\nWhich Element Are You Search : "))

low=0
high=len(lst1)-1
found=False

while(low <= high):
    #mid=low+(high-low)//2 
    mid=high//2
    if lst1[mid]==num:
        print("----------------------------------------")
        print("{} Is Found At {} Index.".format(num,mid))
        print("----------------------------------------")
        found=True
        break
    elif lst1[mid]<num:
        low=mid+1
    else:
        high=mid-1
if found==False:
    print("Element Is Not Found In The List.....!")

