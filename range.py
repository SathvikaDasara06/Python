num=int(input("enter a number:"))
prime=True

for i in range(2,num):
    if num%i==0:
        prime=False

if prime==True:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")