'''with open('sampledata.csv', 'r') as csv_file:
    for line in csv_file:
        data = line.split(',')
        name = data[0]
        print(f"{name} scored in exam 1 scored: {data[2]} and in exam 2 scored {data[3]}")'''

name = ['George', 'Josiah', 'Don', 'Ryan', 'Kevin', 'Kieran', 'Robocon']
score_1 = [10, 54, 45, 23, 76, 35, 67]
score_2 = [43, 23, 73, 94, 84, 76, 78]
age = [16, 15, 14, 16, 16, 17, 2]

with open('csv_testing.csv', 'w') as csv_file:
    