def a(list):
    if(list!=[]):
        print(list[0],end=" ")
        print(list)
        a(list[1:])

list=[1,2,3,4,5,6,7,8,9,10]
a(list)