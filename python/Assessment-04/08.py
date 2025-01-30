# Write a Python function that counts the occurrences of a specific element in a tuple


def count_occurrences(n):
    d ={}
    for i in n:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

n = tuple(map(int,input("Enter the elments of tuples: ").split(",")))
result = count_occurrences(n)
print(result)