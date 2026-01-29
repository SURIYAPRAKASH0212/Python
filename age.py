age=int(input("Enter Age: "))
if age<0:
    print("Invalid Age")
elif age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
elif age>19 and age<=59:
    print("Adult")
else:
    print("Senior")