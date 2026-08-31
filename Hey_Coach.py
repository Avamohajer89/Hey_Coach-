import json
def save_data():
    data = {
        "players": players,
        "games": games,
        "present_players": present_players,
        "starters": starters,
        "notes": notes
    }

    with open("coach_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")
def load_data():
    global players
    global games
    global present_players
    global starters
    global notes

    try:
        with open("coach_data.json", "r") as file:
            data = json.load(file)

        players = data["players"]
        games = data["games"]
        present_players = data["present_players"]
        starters = data["starters"]
        notes = data["notes"]

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("No saved data found.")
def show_dashboard():
    print("========================")
    print("       HEY COACH")
    print("========================")

    print("Players:", len(players))
    print("Games:", len(games))
    print("Present Players:", len(present_players))
    print("Starters:", len(starters))
    print("Coach Notes:", len(notes))

    print("========================")


players = []
games=[]
present_players=[]
starters=[]
notes=[]
def save_players():
    with open("players.json", "w") as file:
        json.dump(players, file)
def load_players():
    global players
    
    try:
        with open("playets.json", "r")as file:
            players = json.load( file )
    except:
        players=[]
        
def welcome():
    print("="*45)
    print("  HEY COACH  ")
    print("="*45)
    print()
    print(" Welcom, Coach")
    print("your basketball management assistant")
    
def add_player():
    print("\n----Add new player----")
    
    name=input("Name: ")
    age=int(input("Age: "))
    height=int(input("Height(cm): "))
    weight=int(input("weight(kg): "))
    position=input("Position: ")
    dominant_hand=input("Dominant Hand: ")
    strengths=input("Strengths: ")
    weaknesses=input("Weaknesses: " )
    
    player={ "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "position": position,
            "dominant_hand": dominant_hand,
            "strengths": strengths,
            "weaknesses": weaknesses,
            }
    players.append(player)
    save_players()
     
    print("Player added successfully!")
            
    
def players_menu():
    while True:
        print("\n----players----")
        print("1. Add Players")
        print("2. View Players")
        print("3. Search Players")
        print("4. Edit Players")
        print("5. Delete Players")
        print("6. Back")
        
        choice = input("Choose an option: ")
        
        if choice=="1":
            add_player()

        elif choice=="2":
            print("\n---Players---")
            if len(players) == 0:
                print("No players found.")
            else:
                for player in players:
                    print("----------------")
                    print("Name:", player["name"])
                    print("Age:", player["age"])
                    print("Height:", player["height"])
                    print("Weight:", player["weight"])
                    print("Position:", player["position"])
                    print("Dominant Hand:", player["dominant_hand"])
                    print("Strengths:", player["strengths"])
                    print("Weaknesses:", player["weaknesses"])

        elif choice=="3":
            name=input("Enter player name")
            found=False
            for player in players:
                if player["name"]==name:
                    found=True
                    print("----------------")
                    print("Name:", player["name"])
                    print("Age:", player["age"])
                    print("Height:", player["height"])
                    print("Weight:", player["weight"])
                    print("Position:", player["position"])
                    print("Dominant Hand:", player["dominant_hand"])
                    print("Strengths:", player["strengths"])
                    print("Weaknesses:", player["weaknesses"])
        
            if found==False:
               print("player not found")


        elif choice=="4":
            name=input('Enter player name: ')
            found=False
            for player in players:
                if player['name']==name:
                    found=True
                    print('1.Age')
                    print('2.weight')
                    print('3.Height')
                    print('4.Position')
                    print('5.Dominant_Hand')
                    print('6.Strengths')
                    print('7.Weaknesses')
                    edit_choice=input('Choose what you want to edit: ')
                    
                    if edit_choice=='1':
                        new_age=input('enter new age: ')
                        player['age']=new_age
                    elif edit_choice=='2':
                        new_weight=input('enter new weight: ')
                        player['weight']=new_weight
                    elif edit_choice=='3':
                        new_height=input('enter new height: ')
                        player['height']=new_height
                    elif edit_choice=='4':
                        new_position=input('enter new position: ')
                        player['position']=new_position
                    elif edit_choice=='5':
                        new_hand=input('enter new Dominant Hand: ')
                        player['Dominant Hand']=new_hand
                    elif edit_choice=='6':
                        new_strengths=input('enter new strengths: ')
                        player['strengths']=new_strengths
                    elif edit_choice=='7':
                        new_weaknesses=input('enter new Weaknesses: ')
                        player['Weaknesses']=new_weaknesses
            if found==False:
                print('player not found!')
                
            else:
                print('player updated successfully.')
        elif choice=='5':
            name=input('enter player name: ')
            found=False
            
            for player in players:
                if player['name']==name:
                    found=True
                    players.remove(player)
                    print('player deleted successfully.')
                    break
                if found==False:
                    print('player not found.')
        elif choice=='6':
            break
        
        else:
            print("Invalid option. Pleas try again.")
        
    
def main_menu():
    while True:
        print("\n---Main Menu---")
        print("1. Players")
        print("2. Games")
        print("3. Team Lineup")
        print("4. Game Statistics")
        print("5. Coach Notes")
        print("6. Exit")
        
        choice=input("Choose an option: ")
        if choice =="1":
            players_menu()
            
        elif choice=="2":
            while True:
                
                 print("----Games----")
                 print("1. Add Game")
                 print("2. View Games")
                 print("3. Search Game")
                 print("4. Edit Game")
                 print("5. Delete Game")
                 print("6. Back")
                 choice=input("Choose an option: ")
                 
                 if choice=='1':
                     opponent=input('Enter opponent name: ')
                     date=input('Enter match date: ')
                     game={'opponent':opponent,'date':date}
                     games.append(game)
                     
                     print('Game added successfully')
                     
                 elif choice=='2':
                     
                     
                     if len(games)==0:
                         print('no games found')
                     else:
                         for game in games:
                             print('opponent:',game['opponent'])
                             print('date:',game['date'])
                             print('-------------')
                 
                 elif choice=="3":
                     opponent=input("Enter opponent name: ")
                     found=False

                     for game in games:
                         if game["opponent"]==opponent:
                                        found=True
                                        print("----------------")
                                        print("Opponent:", game["opponent"])
                                        print("Date:", game["date"])

                     if found==False:
                         print("Game not found.")
                         
                 elif choice=="4":
                     opponent=input("Enter opponent name: ")
                     found=False

                     for game in games:
                         if game["opponent"]==opponent:
                                        found=True

                                        print("1. Opponent")
                                        print("2. Date")

                                        edit_choice=input("Choose what you want to edit: ")
                                        if edit_choice=="1":
                                           new_opponent=input("Enter new opponent name: ")
                                           game["opponent"]=new_opponent

                                        elif edit_choice=="2":
                                             new_date=input("Enter new match date: ")                                           
                                             game["date"]=new_date
                                             
                 elif choice=="5":
                     opponent=input("Enter opponent name: ")
                     found=False

                     for game in games:
                         if game["opponent"]==opponent:
                                        found=True
                                        games.remove(game)
                                        print("Game deleted successfully.")
                                        break

                     if found==False:
                         print("Game not found.")
                 elif choice=='6':
                     break
                    
                
                
        elif choice=="3":
            while True:
                 print("---- Team Lineup ----")
                 print("1. View Lineup")
                 print("2. Change Starters")
                 print("3. Back")

                 lineup_choice=input("Choose an option: ")

                 if lineup_choice=="1":
                     print("Present Players:")
                     for player in present_players:
                         print("-", player)

                     print("Starters:")
                     for player in starters:
                         print("-", player)
                 elif lineup_choice=="2":

                      print("Choose 5 starters:")

                      while len(starters)<5:
                          name=input("Enter starter name: ")
              
                          if name in present_players:
                              if name not in starters:
                                  starters.append(name)
                              else:
                                  print("This player is already a starter.")
                          else:
                              print("This player is not present.")

                              print("Starters updated successfully.")

                 elif lineup_choice=="3":
                     break

                 else:
                     print("Invalid option.")
            
            
            
            
        elif choice=="4":
             print("----- Game Statistics -----")
             print("1. Add Game Statistics")
             print("2. View Game Statistics")
             print("3.Add game statistics")
             print("View game statistics")
             print("4. Back")

             stats_choice=input("Choose an option: ")

             if stats_choice=="1":
                 opponent=input("Enter opponent name: ")

                 found=False

                 for game in games:
                     if game["opponent"]==opponent:
                                    found=True

                                    print("Game found.")
                                    print("Opponent:", game["opponent"])
                                    print("Date:", game["date"])

                 if found==False:
                    print("Game not found.")

             elif stats_choice=="2":
                 print("---- Games ----")

                 if len(games) == 0:
                     print("No games found.")

                 else:
                     for game in games:
                         print("Opponent:", game["opponent"])
                         print("Date:", game["date"])
                         print()  

             elif stats_choice=="3":
                 opponent=input("Enter opponent name: ")

                 found=False

                 for game in games:
                     if game["opponent"]==opponent:
                                    found=True

                                    print("Game found.")
                                    print("Opponent:", game["opponent"])
                                    print("Date:", game["date"])
                                    print("Enter player statistics:")

                                    game["stats"] = {}

                                    for player in players:
                                        print("Player:", player)

                                        points = input("Points: ")
                                        rebounds = input("Rebounds: ")
                                        assists = input("Assists: ")

                                        game["stats"][player] = {"points": points,
        "rebounds": rebounds,
        "assists": assists}

                                        print("Game statistics added successfully.")
 
                 if found==False:
                    print("Game not found.")
             
             elif stats_choice=="5":
                 opponent=input("Enter opponent name: ")

                 found=False

                 for game in games:
                     if game["opponent"]==opponent:
                                    found=True

                                    print("Opponent:", game["opponent"])
                                    print("Date:", game["date"])
                                    print("Player Statistics:")

                                    if "stats" in game:
                                        for player in game["stats"]:
                                            print("Player:", player)
                                            print("Points:", game["stats"][player]["points"])
                                            print("Rebounds:", game["stats"][player]["rebounds"])
                                            print("Assists:", game["stats"][player]["assists"])
                                            print("----------------")
                                    else:
                                        print("No statistics found.")

                 if found==False:
                     print("Game not found.")       
             
                
             elif stats_choice=="4":
                 continue
 
             else:
                 print("Invalid option.")
                 
        elif choice=="5":
            print("---- Coach Notes ----")
            print("1. Add Note")
            print("2. View Notes")
            print("3. Back")
            notes_choice=input("Choose an option: ")
            
            if notes_choice=="1":
                note=input("Enter your note: ")
                notes.append(note)

                print("Note added successfully.")
                
            elif notes_choice=="2":
                if len(notes)==0:
                    print("No notes found.")
                else:
                    print("---- Notes ----")

                    for note in notes:
                        print("-", note)

            elif notes_choice=="3":
                break

            else:
                print("Invalid option.")


        elif choice=="6":
            save_data()
            print("Goodbye, Coach!")
            break
        else:
            print("Invalid option. Pleas try again.")
            
welcome()
load_players()
main_menu()
        
        
        
        
    
