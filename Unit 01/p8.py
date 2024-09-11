# p8 :  Find out pass-percenage of a class.
#       A teacher is entering the mark of student.
#       A student passes a course if the mark are it least 40(out of 100).the teacher
#       - wants to know the percetage of student passed.
# 

java=int(input("Enter JAVA mark :"))
dbms=int(input("Enter DBMS mark :"))
py=int(input("Enter PYTHON mark :"))
ds=int(input("Enter DS mark :"))

if java >=40 and java<=100:
    print("pass in java")
    print("------------")
if dbms >=40 and dbms <=100:
    print("pass in dbms")
    print("------------")
if py >=40 and py <=100:
    print("pass in python")
    print("------------")
if ds >=40 and ds <=100:
    print("pass in ds")
    print("------------")
else:
    print("fail in all subject")
    print("-------------------")

t_mark=java+dbms+py+ds
pre=t_mark/4
print("--------------------")
print("TOTAL MARK :",t_mark)
print("PERCENTAGE :",pre)  
print("--------------------")

if pre>=40.00 and pre<=100.00 :
    print("---------------------------")
    print("You Are Pass In The Exam...")
else :
    print("----------------------------------")
    print("Sorry,You are Fail In The Exam...!")
