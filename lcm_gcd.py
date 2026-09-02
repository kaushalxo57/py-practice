def Compute_gcd(a,b):
    if b==0:
        return a
    else:
        return Compute_gcd(b,a%b)
a=int(input("Enter The Number :"))
b=int(input("Enter the Number :"))
LCM=(a*b)//Compute_gcd(a,b)
print(LCM)