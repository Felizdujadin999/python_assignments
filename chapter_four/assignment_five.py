negative_numbers = 0
positive_numbers = 0
total = 0
user_input = int(input("Enter a list of numbers or press 0 to exit: "))
if user_input == 0:
    print("No numbers were entered except 0")

while user_input != 0:
    if user_input < 0:
        negative_numbers += 1
    else:
        positive_numbers += 1
    total += user_input
    user_input = int(input("Enter a list of numbers or press 0 to exit: "))

average = total / (positive_numbers + negative_numbers)

print(f"The number of positives is: {positive_numbers}\n"
      f"The number of negatives is: {negative_numbers}\n"
      f"The average is: {average}\n"
      f"The total numbers are: {total}")
print("Thanks for using my small app......")
