x=int(input("Enter The Value:"))
print("Factors of:",x,"Are")
for i in range(1,x+1):
    if (x%i==0):
        print(i)