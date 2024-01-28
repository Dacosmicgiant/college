"""
Write a menu driven program to store data of cricketers in objects:
1. Store player's name, total_runs, wickets_taken and country
2. Display specific player's and all players records
3. Add 200 runs to player
4. Delete specified player

Expected Output:
PS C:\Users\Administrator> & C:/Users/Administrator/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/Administrator/Downloads/Python Practs/p8.py"        
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 1
Enter the no of players to add: 2
Enter players name: Ninad
Enter total runs scored: 100
Enter total wickets taken: 5
Enter country name: India
Enter players name: Sachin
Enter total runs scored: 10000
Enter total wickets taken: 50 
Enter country name: India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 2
Enter name of player to fetch record (write all for 'all' players): all
Name:  Ninad    Total runs:  100        Wickets taken:  5       Country India
Name:  Sachin   Total runs:  10000      Wickets taken:  50      Country India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 1
Enter the no of players to add: 1
Enter players name: Rohit
Enter total runs scored: 2000
Enter total wickets taken: 30
Enter country name: India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 3
Enter the name of player to add 200 runs: Rohit
Name:  Rohit    Total runs:  2200       Wickets taken:  30      Country India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 2
Enter name of player to fetch record (write all for 'all' players): all
Name:  Ninad    Total runs:  100        Wickets taken:  5       Country India
Name:  Sachin   Total runs:  10000      Wickets taken:  50      Country India
Name:  Rohit    Total runs:  2200       Wickets taken:  30      Country India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 4
Enter the player name to delete: Sachin
Name:  Ninad    Total runs:  100        Wickets taken:  5       Country India
Name:  Rohit    Total runs:  2200       Wickets taken:  30      Country India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 2
Enter name of player to fetch record (write all for 'all' players): all
Name:  Ninad    Total runs:  100        Wickets taken:  5       Country India
Name:  Rohit    Total runs:  2200       Wickets taken:  30      Country India
1. Accept 3 players
2. Display Player records
3. Add 200 to player runs
4. Remove a particular player
0. For exit
Enter choice: 0
"""

class Player():
    def __init__(self):
        self.name=input("Enter players name: ")
        self.total_runs=int(input("Enter total runs scored: "))
        self.wickets_taken=int(input("Enter total wickets taken: "))
        self.country=input("Enter country name: ")
    
    def display(self):
        print("Name: ",self.name,"\tTotal runs: ",self.total_runs, "\tWickets taken: ", self.wickets_taken, "\tCountry", self.country)

    def modify_runs(self):
        self.total_runs+=200
        self.display()

def delete_player(list_of_players, name):
    for p in list_of_players:
            if p.name == name:
                list_of_players.remove(p)
    for p in list_of_players:
        p.display()

list_of_players= list()
choice = -1
while choice !=0:
    print("1. Accept 3 players\n2. Display Player records\n3. Add 200 to player runs\n4. Remove a particular player\n0. For exit")
    choice=int(input("Enter choice: "))
    if choice == 1:
        # Accept players
        n = int(input("Enter the no of players to add: "))
        for i in range(n):
            p = Player()
            list_of_players.append(p)
    elif choice == 2:
        # display individual player data
        name= input("Enter name of player to fetch record (write all for 'all' players): ")
        if name=='all':
            for p in list_of_players:
                p.display()
        else:
            for p in list_of_players:
                if name==p.name:
                    p.display()
    elif choice == 3:
        # Modify player record
        name = input("Enter the name of player to add 200 runs: ")
        for p in list_of_players:
            if p.name == name:
                p.modify_runs()
    elif choice== 4:
        # Delete sachin as he is retiring
        name = input("Enter the player name to delete: ")
        delete_player(list_of_players, name)