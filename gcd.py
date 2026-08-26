def ComputeGCD(A, B):
    if B == 0:
        return A
    else:
        return ComputeGCD(B, A % B)


A = int(input("Enter the First Number: "))
B = int(input("Enter the Second Number: "))

print(ComputeGCD(A, B))