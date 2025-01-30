# Festival Ticket: A festival has different ticket prices based on age and time of day. If the person is 18 or younger, the ticket costs $10. If theyâ€™re between 19 and 59, itâ€™s $20. For those aged 60 and above, itâ€™s $15. However, after 8 pm, all tickets are discounted by 50%. Write a function that takes in age and time (in 24-hour format) and returns the ticket price after any applicable discounts.

def festival_ticket_price(age, time):

    if age <= 18:
        price = 10
    elif 19 <= age <= 59:
        price = 20
    else:
        price = 15


    if time >= 20:
        price /= 2

    return price



age = int(input("Enter your age: "))
time = int(input("Enter the time (24-hour format): "))

ticket_price = festival_ticket_price(age, time)

print(f"Ticket price: ${ticket_price:.2f}")
