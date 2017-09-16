import csv, string
# Read through available players from FanDuel player list file.

def get_player_list():
    #csv file of player list
    file = open('FanDuel-NBA-2017-03-30-18476-players-list.csv')
    player_list = []
    reader = csv.reader(file)
    for row in reader:
        player_list.append(
            {
                'NAME' : row[1].translate(None, string.punctuation) + " " + row[2].translate(None, string.punctuation),
                'POS' : row[0], 'PRICE' : row[3], 'TEAM' : row[4], 'OPP' : row[5]
             }
        )
    player_list.remove(player_list[0])
    return player_list