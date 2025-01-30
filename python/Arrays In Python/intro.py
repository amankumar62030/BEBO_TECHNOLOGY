# Collection of same data types

# ------------------------------array declaration----------------

# import array
# array.array(type,elements)

# import array as arr
# arr.array(type,element)

# import array import*
# {array(type,elements)}

#------------------------------ signed and unsigned data------------------------

# signed = +,-,12,-4,34                    #(i)
#unsigned = either positive,either negative     #(I)


import array as arr
ar= arr.array('b',[13,20,45,-23,-5])
#direct
# for i in ar:
#     print(i)
#using index
for i in range(5):
    print(ar[i])



import array as arr

# Integer array
int_array = arr.array('i', [1, -2, 3])
print("Integer array:", int_array)

# Float array
float_array = arr.array('f', [1.5, 2.7, -3.2])
print("Float array:", float_array)

# Unsigned integer array
unsigned_array = arr.array('I', [1, 2, 3])
print("Unsigned integer array:", unsigned_array)


