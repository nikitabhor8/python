'''
A Set in Python programming is an unordered collection data type
that is iterable and has no duplicate elements.While sets are mutable,
meaning you can add or remove elements after their creation.
'''


set_a={5,8,67,3,6}
print(set_a)

set_b={6,9,5,6}   #set does not allow duplicate elements.
print(set_b)

set_c={7,9,78,4}
print(set_c)

#set union operation
set_d=set_a.union(set_b)
print("The union of both the sets are:",set_d)

set_e=set_a.union(set_b,set_c)
print("The union of all the sets are",set_e)

#using union operator  |

result=set_a|set_b|set_c
print("The union of all is",result)

#WAP to find intersection of two sets using intesection() function
result=set_a & set_b
print("the interaction is",result)

#WAP to find intersection of two sets using intesection() function and & operator
set1 = set(input("Enter elements of the first set (comma-separated): ").split(","))
set2 = set(input("Enter elements of the second set (comma-separated): ").split(","))
intersection_set_method = set1.intersection(set2)
intersection_set_operator = set1 & set2

print("The intersection of the two sets using intersection() is:", intersection_set_method)
print("The intersection of the two sets using & operator is:", intersection_set_operator)

#set diffrence(-)
result=set_a-set_b
print("The difference is",result)

#set difference using difference()method
result=set_a.difference(set_b)

print("The difference is",result)

#WAP to get symmetric_difference  (elements not in both the sets)
result=set_a ^ set_b
print("The symmetric difference is",result)

















