# Create a list and get 5 elements from the user
my_list = [input(f"Enter element {i+1}: ") for i in range(5)]

# Display the list
print("\nYour list:", my_list)

# Insert a new element
element = input("\nEnter the element to insert: ")
position = int(input("Enter the position to insert at: "))
my_list.insert(position, element)
print("Updated list after insertion:", my_list)

# Delete an element
element_to_delete = input("\nEnter the element to delete: ")
if element_to_delete in my_list:
    my_list.remove(element_to_delete)
    print("Updated list after deletion:", my_list)
else:
    print("Element not found!")

# Final list
print("\nFinal list:", my_list)
