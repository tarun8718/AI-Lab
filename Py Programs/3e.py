N = int(input("Enter the number: "))
temp = N
sum = 0
while temp>0 :
    digit=temp%10
    sum += digit**3
    temp //= 10
if sum == N :
    print("It is an Amrstrong number")
else: 
    print("Nope")