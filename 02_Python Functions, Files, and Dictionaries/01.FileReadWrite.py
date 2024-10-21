
sentence = '''
Hello World!! 
>> Hello 2 World
test line
.. Check my file
'''

# Writing to file
with open('input.txt', 'w') as file:
    file.write(sentence)


# Reading from file
with open('input.txt', 'r') as file:
    content = file.read()
    
    print(content)
    
# Reading from file
with open('input.txt', 'r') as file:
    content = file.readlines()
    
    print(content)

# Reading from file
with open('input.txt', 'r') as file:
    count = 0
    while True:
        count += 1
        line = file.readline()

        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))    