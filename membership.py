bill=int(input("Enter Bill Amount: "))
if bill<0:
    print("Invalid Bill Amount")
else:
    membership = input("Enter Membership(y/n): ")
    if bill>=3000:
        if membership == "Yes":
            amount=bill*0.3
        else:
            amount=bill*0.2
    elif bill<3000 and bill>=1000:
        if membership=="Yes":
            amount=bill*0.15
        else:
            amount=bill*0.1
    else:
        amount=bill
    print("Amount: ",bill-amount)