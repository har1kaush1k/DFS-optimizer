import base64
import requests
def send_request(username, password, date, player, team):
    try:
        response = requests.get(
            url = 'https://api.mysportsfeeds.com/v1.1/pull/nba/2016-2017-regular/player_gamelogs.json',
            params = {
                "player" : player,
                "team" : team,
                "date" : 'until-' + date
            },
            headers = {
                # replace username and password with credentials
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format(username, password).encode('utf-8')).decode('ascii')
            }
        )
        #print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(content=response.content))
        return response
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

