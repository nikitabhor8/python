#2)WAP to reverse the element in List.

def rev_lst(l):
    return l[::-1]    #Reverses the list using slicing

# Define the list
l=[93,89,48,65]
print("Original list:",l) #print the original list
print("---------------------------------------")

# Print the reversed list

print("The reverse list is:",rev_lst(l))
