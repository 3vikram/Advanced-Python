def factorial(input):

    number = 1
    for num in range(1, input+1):
        number = number * num

    return number


run = factorial(6)
print(run)

Result:

720
