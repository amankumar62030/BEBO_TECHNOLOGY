# 2.Write a Python code that takes a dictionary representing student names and their scores and a new student-score pair. If the student already exists, update the score; if not, add the new student. Use the update() method.
# Example Input: {'John': 85, 'Emma': 92}, {'Lucas': 78}


student = {
    "aman":34,
    "Rahul":56,
    "Sohan":78
}

student2 = {
    "aman":98,
    "Sohit":45
}

student.update(student2)
print(student)

