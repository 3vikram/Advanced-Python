def square(list):
    result = []
    for i in list:
        result.append(i*i)
    return result


if __name__ == '__main__':
    num = [1,2,3,4,5]
    print(square(num))


Result:

[1, 4, 9, 16, 25]

Process finished with exit code 0
