# p3 : Extracting field of a roll number using string  indexing and slicing.

roll_number="MCA462024"
rollnumber='m','c','a','4','6','2','0','2','4'

# slicing on roll number.
RollNumber=roll_number[3:5]
DepartmentName=roll_number[0:3]
JoinYear=roll_number[5:]

# indexing on roll nmber.
DepartmentName1=rollnumber.index('m')
JoinYear1=rollnumber.index('2')

print("-----------------input string-----------------------")
print("First :",roll_number)
print("Second :",rollnumber)

print("-----------------slicing find-----------------------")
print("Roll Number :",RollNumber)
print("Department Name :",DepartmentName)
print("Joinnig Year Of Collage :",JoinYear)

print("-----------------index find-----------------------")
print("Department Name :",DepartmentName1)
print("Joinnig Year Of Collage :",JoinYear1)