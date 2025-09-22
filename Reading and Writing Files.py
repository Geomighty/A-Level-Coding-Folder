def reading_files(read_filename):
    with open(read_filename, 'r') as file:
        for line in file:
            print(line)


def writing_files(write_filename):
    with open(write_filename, 'w') as file:
        text = str(input("What would you like to write to the file. write quit to exit "))
        file.write(text)
        while text != "quit":
            text = str(input("What would you like to write to the file. write quit to exit "))
            file.write(input)

print("Which option do you want to choose:")
print("1. read files")
print("2. write files")
print("enter quit to stop the program")
option = int(input("Enter what number option you want to choose "))

while option != "quit":
    if option == 1:
        read_filename = str(input("What file would you like to read "))
        reading_files(read_filename)

        print("Which option do you want to choose:")
        print("1. read files")
        print("2. write files")
        print("enter quit to stop the program")
        option = int(input("Enter what number option you want to choose"))

    if option == 2:
        write_filename = str(input("What file would you like to write to "))
        writing_files(write_filename)

        print("Which option do you want to choose:")
        print("1. read files")
        print("2. write files")
        print("enter quit to stop the program")
        option = int(input("Enter what number option you want to choose")) # I ran into a problem when writing to files and I can't quite work out where I am going wrong. 

exit()