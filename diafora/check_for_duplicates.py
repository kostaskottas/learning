#mou bgazei oti emfanizetai kai stis 2 listes
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,4,6,8,0]
duplicates = set(list1) & set(list2)
print(duplicates)

#mou bgazei oti dn emfanizetai kai stis 2 listes
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,4,6,8,0]
duplicates = set(list1) ^ set(list2)
print(duplicates)