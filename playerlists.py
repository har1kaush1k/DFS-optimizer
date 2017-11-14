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
                'FIRST' : row[2], 'LAST' : row[4], 'POS' : row[1],
                'PRICE' : row[6], 'TEAM' : row[9], 'OPP' : row[10],
                'INJ' : row[11]
            }
        )
    player_list.remove(player_list[0])
    return player_list

def trim_names(self, p_list):
    for p in p_list:
        p['FIRST'] = p['FIRST'].translate(None, string.punctuation)
        p['LAST'] = p['LAST'].translate(None, string.punctuation)
    return p_list
