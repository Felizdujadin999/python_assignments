current_day = ""
future_day = ""
first_user_input = int(input("Enter today's day of the week: "))
# while first_user_input > 6 or first_user_input < 0:

if first_user_input == 0:
    current_day = "Sunday"
elif first_user_input == 1:
    current_day = "Monday"
elif first_user_input == 2:
    current_day = "Tuesday"
elif first_user_input == 3:
    current_day = "Wednesday"
elif first_user_input == 4:
    current_day = "Thursday"
elif first_user_input == 5:
    current_day = "Friday "
elif first_user_input == 6:
    current_day = "Saturday"

second_user_input = int(input("Enter the number of days elapsed since today: "))
future_date = first_user_input
for value in range(1, second_user_input + 1, 1):
    future_date += 1
    if future_date == 7:
        future_date = 0

if future_date == 0:
    future_day = "Sunday"
elif future_date == 1:
    future_day = "Monday"
elif future_date == 2:
    future_day = "Tuesday"
elif future_date == 3:
    future_day = "Wednesday"
elif future_date == 4:
    future_day = "Thursday"
elif future_date == 5:
    future_day = "Friday"
elif future_date == 6:
    future_day = "Saturday"

print(f"Today is {current_day}\nand the future day is {future_day}")