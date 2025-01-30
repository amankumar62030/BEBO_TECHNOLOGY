# zip()---tuple
# join elments from two or more iterables

a = [10,20,30,50]
b = [40,50,60]
# zip()--(10,40),(20,50),(30,60)
z = zip(a,b)
print(list(z))

subjects = ["english","hindi","maths","science","Biology"]
marks = [78,49,30,20]
a = zip(subjects,marks)
print(type(a))
res = list(a)
print(type(res))
print(res)