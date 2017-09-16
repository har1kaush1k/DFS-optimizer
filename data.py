import request
import playerlists
import string

def get_data(list):
    username = raw_input("username: ")
    password = raw_input("password: ")
    date = raw_input("Date (YYYYMMDD): ")
    for player in list:
        first = player['FIRST'].translate(None, string.punctuation)
        last = player['LAST'].translate(None, string.punctuation)
        data = request.send_request(username, password, date, first + '-' + last, player['TEAM'].lower())
        player['DATA'] = data

list = playerlists.get_player_list()
get_data(list)
print(list[0]['DATA'])