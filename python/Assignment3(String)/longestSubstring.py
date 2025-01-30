# Longest substring without repeating characters


n = input("Enter the String: ")
st = 0
m = 0
d = {}

for i in range(len(n)):
    if n[i] in d and d[n[i]] >= st:
        st = d[n[i]] + 1
    d[n[i]] = i
    m = max(m, i - st + 1)

print("Length of the longest substring without repeating characters:", m)
