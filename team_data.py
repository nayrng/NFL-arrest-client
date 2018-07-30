import collections
from crime_data import get_data, arrest_detail_list
from valid_data import valid_teams

base_url = 'http://nflarrest.com/api/v1/team'

top_teams = collections.namedtuple('top_teams',
                                   'Team_preffered_name arrest_count')
top_players = collections.namedtuple('top_players',
                                     'Name arrest_count')
top_crimes = collections.namedtuple('top_crimes',
                                    'Category arrest_count')

timeline = collections.namedtuple('timeline',
                                  'Month Year arrest_count')


def get_teams():
    while True:
        try:
            team = input("Enter the name of the team you'd like to look up\n"
                         "Format: SF, NYG, etc..\n"
                         "Type 'HELP' for list of all valid teams\n")
            if team.upper() == 'HELP':
                for each in sorted(valid_teams):
                    print(each)
                print()
                continue
            if team.upper() not in valid_teams:
                raise ValueError
        except ValueError:
            print("Please enter a valid team")
            continue
        else:
            return team


def top_arrested_teams(url):
    results = get_data(url)
    teams = []

    for t in results:
        team = top_teams(
            Team_preffered_name=t.get('Team_preffered_name'),
            arrest_count=t.get('arrest_count')
        )
        teams.append(team)
    return teams


def top_players_arrested(url):
    team = get_teams()
    url = url + f'/{team}'
    results = get_data(url)
    players = [top_players(**p) for p in results]
    return players


def top_crimes_committed(url):
    team = get_teams()
    url = url + f'/{team}'
    results = get_data(url)
    crimes = [top_crimes(**c) for c in results]
    return crimes


def team_crime_timeline(url):
    team = get_teams()
    url = url + f'/{team}'
    results = get_data(url)
    crimeline = [timeline(**t) for t in results]
    return crimeline


def arrest_details(url):
    team = get_teams()
    url = url + f'/{team}'
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
