#WAP to get sum of digits present in a number.
#example n = 678    sum=21

n=int(input("Enter number:"))
temp=n
sum=0
while(n>0):
    rem=n%10
    #rev = rev*10+rem
    sum=sum+rem
    n=n//10
print("sum=",sum)

#WAP to check whether the number is armstrong number or not
#for Example n=153 , 371
#sum=(3)*3*3+5*5*5+1*1*1
#    =27+125+1=153

#27+343+1=371

