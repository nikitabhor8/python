#WAP to reverse a given number for example n =123 rev = 321

n=int(input("Enter a number: "))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse of a given number is",rev)

#WAP to check whether the number is palindrome or not
#n=434  rev=424 palindrome

if rev==temp:
    print("The number is palindrome")
else:
    print("The number is not palindrome.")


