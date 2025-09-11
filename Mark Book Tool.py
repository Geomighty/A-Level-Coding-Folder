name_list =  ['Ryansh', 'Oliver', 'Edward', 'Daniel', 'Alex']
scores_list = [[] for i in name_list]           # Create a lists of empty lists

# Menu:
print("What do you want to do: ")
print("\n1. Add to the scores list.")
print("2. Get whole scores list.")
print("3. Get a specific pupils scores list.")
print("4. Get the class average.")
print("5. Know who is top scorer.")
print("6. Learn who is the lowest scorer.")
option = int(input("Enter the number of the menu option you want: "))

#1. Add to the scores list:
if option == 1:
    name = str(input("Enter the name of a pupil from the list enter stop to quit: "))
    while name != "stop":
        name_index = name_list.index(name)
        new_score = int(input("Enter the persons score: "))
        scores_list[name_index].append(new_score)
        name = str(input("Enter the name of a pupil from the list enter stop to quit: "))

#2. Get whole scores list:
if option == 2:
    for i in range(len(name_list)):
        print(f"{name_list[i]} score was {scores_list[i]}")

#3. Get a specific pupils scores list:
if option == 3:
    name = str(input("Enter the name of a pupil from the list enter stop to quit: "))
    while name != "stop":
        name_index = name_list.index(name)
        print(f"{name} score(s) were {scores_list[name_index]}")
        name = str(input("Enter the name of a pupil from the list enter stop to quit: "))

#4. Get the class average:
if option == 4:
    print(f"{(sum(scores_list))/len(name_list)}")