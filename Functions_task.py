from datetime import datetime

def calculate_age(year,month,day):
    today = datetime.now()
    DOB=datetime(year, month, day)
    age= today-DOB 
    age_in_days= age.days
    age_in_years=int(age_in_days/365) 
    age_in_days= age_in_days%365
    age_in_months= int(age_in_days/30)


    print("Your are %d years, %d months, and %d days old" %(age_in_years,age_in_months,age_in_days))

def check_birthdate(year, month, day):
    today = datetime.now()
    DOB=datetime(year,month,day)
    if today > DOB:
        return True 
    else:
        return False 

year=int(input("Enter year of birth: "))
month=int(input("Enter month of birth"))
day=int(input("Enter day of birth"))
check_birthdate(year,month,day)        

if check_birthdate(year, month, day) == True:
    calculate_age(year, month, day)


   


else:
    print("Birthdate is invalid")

