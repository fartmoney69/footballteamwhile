football_team = []

#append 11 players name
for i in range(11):
    name = input("Enter the name of the player: ")
    football_team.append(name)
print(football_team)

repeat = "Y"
while repeat == "Y":
     edit = int(input("Which player do you want to change?: "))
     football_team[edit-1] = input("Enter a new player: ")
     print(football_team)

     delete = int(input("Which player do you want to delete?: "))
     del football_team[delete-1]
     print(football_team)

     repeat = input('Do you want to edit or delete name(Y/N) ')
   
