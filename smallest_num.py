#Q.3)WAP to find second smallest element in the list.
#number list
lst = [77, 23, 51, 36, 34, 29]
print("orginal list",lst)  #ouptut orginal list
print("-------------------------------------------")

# Remove duplicates and sort the list
sorted_list = sorted(set(lst)) #sorted method
print("The sorted list :",sorted_list) #After sorting

len(sorted_list) > 1

# Second smallest is at index 1
print("The second smallest element is :", sorted_list[1]) #second smallest element 
