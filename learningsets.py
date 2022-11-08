#how to create sets
# s1={"Ahmed",1,True,3.14,(5+4j)}
# print(s1)
#----------------------------------------
#duplicates are not allowed in sets
# s1={"Ahmed",1,True,3.14,(5+4j),"Ahmed"}
# print(s1)
#-------------------------------
#sets are mutable so we can modify it
#add/ update element in set
# s1={"Ahmed",1,True,3.14,(5+4j),"Ahmed"}
# s1.add("Hassan sheikh")
# print(s1)
#---------------------------------
#adding/updating multiple elements in set
# s1={1,2,3,4,5}
# s1.update([6,7,8,9])
# print(s1)
#-----------------------------------------
#removing any element from set
# s1={1,2,3,4,5}
# s1.remove(1)
# print(s1)
#-----------------------
#Sets functions
#taking union of two sets
# s1={1,2,3,4,5}
# s2={"a","b","c"}
# print(s1.union(s2))
#------------------------------------
#taking intersection of two sets 
s1={1,2,3,4,5}
s2={3,2,5}
print(s1.intersection(s2))
#------------------------------

