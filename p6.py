#  p6 : find the student from CS department where the roll number may be in 
#       capital or smallcase letter.

rollno = input("Enter Roll Number :")
branch=rollno[0:2]
if branch == "CS" or branch == "Cs" or branch == "cS" or branch == "cs" :
    print("-----------------------------------------------------")
    print(rollno," roll number is a computer science department.")
    print("-----------------------------------------------------")
else :
    print("-----------------------------------------------------------")
    print(rollno,"roll number is not a computer science department...!")
    print("-----------------------------------------------------------")

