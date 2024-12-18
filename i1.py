def second_smallest(lst):
    lst = list(set(lst))  # Remove duplicates
    lst.sort()  # Sort the list
    return lst[1] if len(lst) > 1 else None  # Return the second smallest element

# Example usage:
lst = [7, 2, 5, 3, 3, 2]
print(second_smallest(lst))  # Output: 3
