# 3.Write a Python code that takes a dictionary and returns the sum of all its values.

student = {
    "aman":34,
    "Rahul":56,
    "Sohan":78
}

values = student.values()
print(sum(values))
# -------------or--------------
sum = 0
for i in values:
    sum+=i
print(sum)