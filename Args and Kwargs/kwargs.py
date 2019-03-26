def person(**namevalues):
    result = []
    for name, value in namevalues.items():
        result.append(value)
    return result

run = person(name = 'trivikram', age = 30, address = 'Halasuru', city= 'Bangalore', state= 'Karnataka')
print(run)


Result:

['trivikram', 30, 'Halasuru', 'Bangalore', 'Karnataka']
