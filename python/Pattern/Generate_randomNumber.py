import random
count =0
num = random.randint(1,100)
print(num)

while True:
    n = int(input("Enter any number: "))
    count+=1
    if(n==num):
        print(f"You guessed the right number in step {count}")
        break
    elif(n<num):
        print("Enter the high number")
    else:
        print("Enter the less number")


