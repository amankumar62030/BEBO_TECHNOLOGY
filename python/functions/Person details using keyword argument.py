
def person_details(name,Address,id):
    return(name,Address,id)

name = input("Enter name:")
Address = input("Enter Address:")
id = int(input("Enter id: "))
print(person_details(name=name,Address=Address, id=id))
print(person_details(Address=name,name=Address, id=id))