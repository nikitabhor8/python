'''
wap to accept a number from user and check whether it is divisible by 3 and 5.
'''
num = int(input("Enter the number: "))
if num % 3 ==0 or num % 5 ==0:
    print("The number is divisible by 3 or 5.")
else:
    print("The number is not divisible by 3 or 5. ")
