import collections
import requests
from crime_data import get_data, arrest_detail_list

base_url = 'http://nflarrest.com/api/v1/player'

most_players = collections.namedtuple('most_players',
                                      'Name Team Position arrest_count')

all_crimes = collections.namedtuple('all_crimes',
                                    'category arrest_count')

player_searcher = collections.namedtuple('player_searcher',
                                         'Name Position arrest_count')


def top_players_arrested(url):
    results = get_data(url)
    players = []
    for p in results:
        data = most_players(
            Name=p.get('Name'),
            Team=p.get('Team'),
            Position=p.get('Position'),
            arrest_count=p.get('arrest_count')
        )
        players.append(data)
    return players


def top_crimes(url):
    basic_url = url
    while True:
        url = basic_url
        try:
            player = input("Enter the name of the player: ")
            url = url + f'/{player}'
            resp = requests.get(url)
            data = resp.json()
            if len(data) == 0:
                raise LookupError
        except LookupError:
            print("Can't find player, please enter another name\n")
            continue
        else:
            break
    results = get_data(url)
    crimes = [all_crimes(**c) for c in results]
    print(f"Displaying crimes for {player}")
    return crimes


def player_search(url):
    basic_url = url
    while True:
        url = basic_url
        try:
            player = input("Enter a name (first name, last name, or both) ")
            url = url + f'/?term={player}'
            resp = requests.get(url)
            data = resp.json()
            if len(data) == 0:
                raise LookupError
        except LookupError:
            print("Can't find player, please enter another name\n")
            continue
        else:
            break
    results = get_data(basic_url, player)
    players = [player_searcher(**p) for p in results]
    return players


def crime_details(url):
    basic_url = url
    while True:
        url = basic_url
        try:
            player = input("Enter a player's full name: ")
            url = url + f'/{player}'
            resp = requests.get(url)
            print(url)
            data = resp.json()
            if len(data) == 0:
                raise LookupError
        except LookupError:
            print("Can't find player, please enter another name\n")
            continue
        else:
            break
    results = get_data(url)
    details = []
    for d in results:
        de = arrest_detail_list(
            Date=d.get("Date"),
            Team=d.get("Team"),
            Name=d.get("Name"),
            Position=d.get("Position"),
            Position_name=d.get("Position_name"),
            Encounter=d.get("Encounter"),
            Crime_category=d.get("Crime_category"),
            Description=d.get("Description"),
            Outcome=d.get("Outcome"),
            Season=d.get("Season")
        )
        details.append(de)
    return details
