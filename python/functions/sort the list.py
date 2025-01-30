city = ["jaipur","kota","chandigarh","delhi","patna"]

def length(city):
    return len(city)
sort = sorted(city,key=length,reverse=True)     #iterative
print(sort)

print("-------------using lambda----------")

sort = sorted(city,key=lambda x:len(x),reverse=True)
print(sort)