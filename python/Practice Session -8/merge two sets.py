# 9.	Merge Two Sets and Add Their Elements as Keys in a Dictionary

set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}

merged_set = set1 | set2  # or set1.union(set2)

my_dict = dict.fromkeys(merged_set,10)
print(my_dict)
