
userdata = [
    'name, age, profession',
    'Dhruv, 18, SDE',
    'DhruvS, 19, SDE2',
    'DhruvSaini, 20, SDE3',
]

with open('input.csv', 'w') as file:
    for user in userdata:
        file.write(user + '\n')
    

with open('input.csv', 'r') as file:
    print(file.readlines())


# Reading from file
with open('input.csv', 'r') as file:
    count = 0
    while True:
        count += 1
        line = file.readline()

        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))    