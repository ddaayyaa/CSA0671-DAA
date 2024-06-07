n=int(input("Enter a number:"))
sum=0
originalnum=n
while n>0:
    r=n%10
    sum+=r**3
    n //=10
if sum==originalnum:
    print("Armstrong number")
else:
    print("Not Armstrong number")