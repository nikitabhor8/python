#program to calculate simple interest.

# Get user input for principal, rate, and time
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest (in %): "))
T = float(input("Enter the time (in years): "))

# Calculate simple interest
SI = (P * R * T) / 100

# Print the result
print("The simple interest is:", SI)
