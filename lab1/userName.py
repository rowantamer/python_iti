first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# reverse the order of first and last name and add a space between them
full_name = last_name[::-1] + " " + first_name[::-1]

print("Your name in reverse order is:", full_name)