n = int(input("Enter the number: "))
i=2
def pri(i):
    j=2
    prime= True;
    while(j<i):
        if(i%j == 0):
            prime= False
        j+=1
    return prime
while(i<=n):
    if(pri(i)):
        print(i)
    i+=1

