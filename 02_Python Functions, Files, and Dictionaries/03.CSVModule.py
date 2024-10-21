import csv

lst = [
    ('name', 'age', 'profession'),
    ('Dhruv', '18', 'SDE'),
    ('DhruvS', '19', 'SDE2'),
    ('DhruvSaini', '20', 'SDE3'),
    ('DSaini', '21', 'SDE4'),
    ('DS', '21', 'SDE5')
    ]

with open('input.csv', 'w') as file:
    writer = csv.writer(file)
    
    for item in lst:
        print(item)
        writer.writerow(item)

with open('input.csv', 'r') as file:
    readerobj = csv.reader(file)
    for sent in readerobj:
        print(sent)
