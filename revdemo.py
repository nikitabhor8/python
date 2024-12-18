#Q.1)Write a function to reverse a list without using
#the built-in reverse() method.
def rev_lst(l):
    return l[::-1]

l=[98,87,45,78]

print("The reverse is",rev_lst(l))

#Q.2)WAP to find second largest number in a list

l2=[89,67,54,65,89,78]

remove_dup=(list(set(l2)))
print("The final list is",remove_dup)

sorted_list=sorted(remove_dup)

print("The sorted list is :",sorted_list)

print("The second largest element is",sorted_list[-2])

#Q.3)WAP to do intersection of two list

def intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection(list1, list2)
print("Intersection:", result)

#Q.4)find maximum and minimum from the list
#Q.5)WAP to add and remove the elements from the list
#Q.6)WAP to check whether the list is palindrome or not
