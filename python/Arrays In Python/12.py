# Intersection of two array

import array as arr

array1 = arr.array('i', [1, 2, 3, 4])
array2 = arr.array('i', [5, 2, 4, 8])

intersection_array = arr.array('i',[])
for i in array1:
    if i in array2:
        intersection_array.append(i)
print(intersection_array)
