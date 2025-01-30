# 18.	Write a function that takes a string and returns a dictionary with the frequency of each word in the string.



def freq(s1):
    d = {}
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    print(d)
s1 = input("Enter the String: ")
freq(s1)