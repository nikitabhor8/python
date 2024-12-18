#Q.4) Perform Intersection operation on list.

def intersection(list1, list2):  
    return list(set(list1) & set(list2)) # Perform intersection

# Given lists(list 1,list 2)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8,54]

# Get the intersection
result = intersection(list1, list2) #intersection of 2

# Print the result
print("list one:",list1)
print("list two:",list2)
print("-----------------------------------")
print("Intersection of the 2 list:", result)
