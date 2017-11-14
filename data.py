import request
import playerlists
import string
import time
import json

def get_data(list):
    username = raw_input("username: ")
    password = raw_input("password: ")
    date = raw_input("Date (YYYYMMDD): ")
    start_time = time.time()
    for player in list:
        print(player['FIRST'] + ' ' + player['LAST'])
        first = player['FIRST'].translate(None, string.punctuation)
        last = player['LAST'].translate(None, string.punctuation)
        data = request.send_request(username, password, date, first + '-' + last, player['TEAM'].lower())
        decoded = json.loads(data)
        player['DATA'] = decoded
        print("%s seconds" % (time.time() - start_time))
        
list = playerlists.get_player_list()
get_data(list)
print(list[0]['DATA'])