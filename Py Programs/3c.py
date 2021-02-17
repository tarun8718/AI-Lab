def fact(n):
    if(n<2):
        return n
    else:
        return n*fact(n-1)

n = int(input("Enter a num: "))
print("Factorial of that number is: ",fact(n))