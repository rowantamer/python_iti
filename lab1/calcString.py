def count_chars(string):
    # initialize counters
    num_digits = 0
    num_letters = 0

    # loop through each character in the string
    for char in string:
        # check if the character is a digit or letter
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1

    # print the results
    print("Number of digits:", num_digits)
    print("Number of letters:", num_letters)

# example usage
s = "Hello world! 123"
count_chars(s)