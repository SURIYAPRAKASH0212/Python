temperature=int(input("Enter temperature: "))
if temperature<0:
    print("Cold fever")
elif temperature>=38:
    print("Fever Detected")
else:
    print("Normal")