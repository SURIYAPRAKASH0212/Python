salary=int(input("Enter Salary: "))
if salary<250000:
    tax=0
    print("No Tax")
elif salary>=250000 and salary<=500000:
    tax=salary*0.05
    print("Tax 5%")
else:
    tax=salary*0.1
    print("Tax 10%")
print("Tax Amount: ",tax)
print("Salary After Tax: ",salary-tax)