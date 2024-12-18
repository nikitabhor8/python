#Q.1)Create dynamic list where you will ask user to enter 5 elements in it
# and perform insert new element and delete an element operationon it.

# Create an empty list and get 5 elements from the user
my_list = [input(f"Enter element {i+1}: ") for i in range(5)]

# Display the list
print("\nYour list:", my_list)

# Insert a new element at a specified position
element = input("\nEnter the element to insert: ")  # Element to insert
position = int(input("Enter the position to insert at (0-4): "))  # Position to insert at
my_list.insert(position, element)  # Insert element at the position
print("Updated list after insertion:", my_list)

# Delete an element
element_to_delete = input("\nEnter the element to delete: ")  # Element to delete
if element_to_delete in my_list:
    my_list.remove(element_to_delete)  # Remove the element if found
    print("Updated list after deletion:", my_list)
else:
    print("Element not found!")  # If the element is not in the list

# Final list
print("\nFinal list:", my_list)
