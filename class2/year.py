year=int(input("Enter number of years: "))
unit=input("""Pick a choice: 
1-Days 
2-Weeks 
3-Hours
What is your choice? """)

if unit == "1":
    print(f"in {year} years {year*365} days")
elif unit == "2":
    print(f"in {year} years {year*52} weeks")
elif unit == "3":
    print(f"in {year} years {year*365*24} hours")
else:
    print("Wrong choice.")
    