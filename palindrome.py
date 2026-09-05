number=int(input("Enter the number:"))
string=str(number)
rev_str=string[::-1]
print("Reversed String:",rev_str)
if string==rev_str:
    print("It is an Palindrome")
else:
    print("It is Not a Palindrome")
