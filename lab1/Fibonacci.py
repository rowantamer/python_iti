def fibonacci(n):
    # First two terms
    num1 = 0
    num2 = 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(num1)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(num1, end=" ")
            sum = num1 + num2
            # update values
            num1 = num2
            num2 = sum
            count += 1

# Call function with argument 50
fibonacci(50)