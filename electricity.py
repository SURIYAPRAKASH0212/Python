units = int(input("Enter Units: "))
if units<=100:
    bill=0
elif units>100 and units<=300:
    bill=(units-100)*2
    if bill>200:
        bill+=50
elif units>300:
    bill=(200*2)+((units-300)*5)
    bill+=100
print("Bill: ",bill)