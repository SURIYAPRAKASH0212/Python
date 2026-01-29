n=int(input("Enter n: "))
count=0
for i in range(1,n+1,2):
    count+=i
print("Odd Sum: ",count)