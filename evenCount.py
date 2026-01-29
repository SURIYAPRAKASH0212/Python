n=int(input("Enter n: "))
count=0
for i in range(0,n+1,2):
    count+=i
print("Even Sum: ",count)