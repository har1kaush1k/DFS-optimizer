import csv
import string
# Read through available players from FanDuel player list file.

def get_player_list():
    #csv file of player list
    filename = raw_input('Enter filename (.csv): ') + '.csv'
    file = open(filename)
    player_list = []
    reader = csv.reader(file)
    for row in reader:
        player_list.append(
            {
                'FIRST' : row[1], 'LAST' : row[2], 'POS' : row[0],
                'PRICE' : row[3], 'TEAM' : row[4], 'OPP' : row[5]
            }
        )
    player_list.remove(player_list[0])
    return player_list
