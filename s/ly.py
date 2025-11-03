year=int(input("Enter a number :"))
if (year%400 == 0 or (year%4 == 0 and year%100 != 0)):
    print(f"your given year {year} is leap year")
else:
    print(f"your given year {year} is not leap year")
