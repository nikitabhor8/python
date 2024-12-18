def is_armstrong(num):
    str_num = str(num)
    num_digits = len(str_num)
total = sum(int(digit) ** num_digits for digit in str_num)
 
if total == num:
    return True
else:
    return False
num = int(input("Please enter a 3 digit number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
