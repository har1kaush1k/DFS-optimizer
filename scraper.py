from lxml import html
from lxml import etree
import requests
import csv
import playerlists

def get_defense(team, position):
    page = requests.get('https://www.rotowire.com/daily/nba/defense-vspos.php?site=FanDuel&statview=last5&pos=' + position)
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()')
    names = []
    defense = []
    team_defense = {}
    for i in range(len(data)):
        if i % 14 == 3:
            defense.append(data[i])
        elif i % 14 == 0:
            if data[i] == 'Golden State Warriors':
                names.append('GS')
            elif data[i] == 'New York Knicks':
                names.append('NY')
            elif data[i] == 'Brooklyn Nets':
                names.append('BKN')
            elif data[i] == 'San Antonio Spurs':
                names.append('SA')
            elif data[i] == 'Los Angeles Clippers':
                names.append('LAC')
            elif data[i] == 'Los Angeles Lakers':
                names.append('LAL')
            elif data[i] == 'Oklahoma City Thunder':
                names.append('OKC')
            elif data[i] == 'New Orleans Pelicans':
                names.append('NO')
            else:
                names.append(data[i][0:3].upper())
    for i in range(len(names)):
        team_defense[names[i]] = defense[i]
    return team_defense[team]

