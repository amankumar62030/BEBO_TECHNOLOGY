# Ride Height Requirement: Youâ€™re managing a theme park ride. To go on the ride, a person must be at least 48 inches tall. However, if theyâ€™re between 42 and 47 inches, they can ride if accompanied by an adult. If they are under 42 inches, they cannot ride at all. Write a function that takes in the height and a boolean for whether an adult is present, and returns True if they can ride, False otherwise.

def can_ride(height, has_adult):
    if height>=48:
        return True
    elif 42<=height<48 and has_adult:
        return True
    return False

height = int(input("Enter the height: "))
has_adult = input("Is there an adult present? (yes/no): ").lower()=="yes"
result = can_ride(height,has_adult)

print(result)
