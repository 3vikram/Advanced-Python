def fibonacci(num):
    num1 = 1
    num2 = 1
    for no in range(num):
        if no == 0:
            print(0)
        elif no == 1 or no == 2:
            print(num2)
        else:
            temp = num1
            num1 = num2
            num2 = temp + num1
            print(num2)


run = fibonacci(20)
print(run)


Result:

0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
