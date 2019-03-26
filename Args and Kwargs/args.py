def square(*nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result

run = square(2,3,5,7,8,9,10)
print(run)



Result:

[4, 9, 25, 49, 64, 81, 100]
