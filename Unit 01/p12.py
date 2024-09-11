birthdays = {"Krunal": "10/08/04","Darshan": "03/12/04","Dharuvraj": "24/04/04","Aswin": "07/03/03",
             "Tushar": "23/05/04","Meet": "15/06/04","Pradip": "07/07/03","Jatin": "06/08/04",
             "Chetan": "15/10/04","Chirag": "07/11/03"}
print("\n")
month = int(input("Enter the month:"))

print("Birthdays in",month," month")

count=0
if(month<=12):
    for name, birthday in birthdays.items():
        day, month1, year = birthday.split("/")
        if int(month1) == month:
            print(name, ":", birthday)
            count= 1
    else : 
        if count == 0:
            print("This Month in Birthday Are Not Available..!")
else:
    print("Your Enterd Month Is Wrong.....!")
    print("\n")