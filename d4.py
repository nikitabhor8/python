def is_prime(num):
    if num < 2:
        return False
if num == 2:
    return True
if num % 2 == 0:
     return False
 sqrt_num = int(num ** 0.5)
for i in range(3, sqrt_num, 2):
    if num % i == 0:
        return False
    return True
num = int(input("Please enter a 3 digit number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
