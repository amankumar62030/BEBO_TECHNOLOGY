# 8.	Count the Occurrence of Items in a List and Store in a Dictionary

my_list = ["Mango","Banana","Strawberry","Orange","Mango","Banana"]
d ={}
for items in my_list:
    if items in d:
        d[items]+=1
    else:
        d[items]=1
print(d)