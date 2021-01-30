import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='cp1251')
player1 = {
    'PlayerName': "Vladimir Girinovsky",
    'Score': 345,
    'Awards': ["Moscow", "Novgorod", "Sochi"]
}

player2 = {
    'PlayerName': "Vladimir Zelensky",
    'Score': 163,
    'Awards': ["Kiev", "Lviv", "Odessa"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ------------------SAVE TO JASON--------------
json.dump(myplayers, myfile)
myfile.close()

# ------------------Load by JSON------------
myfile = open(filename, mode='r', encoding='cp1251')

json_data = json.load(myfile)

for user in json_data:
    print("Player name is: " + str(user['PlayerName']))
    print("Player score is " + str(user['Score']))
    print("Player awards №1 " + str(user['Awards'][0]))
    print("Player awards №2 " + str(user['Awards'][1]))
    print("Player awards №3 " + str(user['Awards'][2]))
    print("------------------------------------------\n\n")
myfile.close()
