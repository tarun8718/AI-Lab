N = int(input("Enter a Number: "))
rN = str(N)[::-1]
if rN == str(N):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
