import requests
import printers
import collections
from valid_data import valid_crimes
import datetime

base_url = 'http://nflarrest.com/api/v1/crime'

all_crimes = collections.namedtuple('all_crimes',
                                    'Category arrest_count')

top_players_for_crime = collections.namedtuple('top_players_for_crime',
                                               'Name arrest_count')

top_teams_for_crime = collections.namedtuple('top_teams_for_crime',
                                             'Team Team_name Team_city arrest_count')

top_positions_for_crime = collections.namedtuple('top_positions_for_crime',
                                                 'Position arrest_count')

number_arrests = collections.namedtuple('number_arrests',
                                        'Month Year arrest_count')

arrest_detail_list = collections.namedtuple('arrest_detail_list',
                                            'Date Team Name Position Position_name Encounter Crime_category Description Outcome Season')


def get_crime_id():
    while True:
        try:
            CrimeID = input("Enter the crime you'd like to look up\n"
                            "or type 'HELP' for all valid crime types\n")
            if CrimeID.upper() == 'HELP':
                for each in sorted(valid_crimes):
                    print(each)
                print()
                continue
            if CrimeID not in valid_crimes:
                raise ValueError
        except ValueError:
            print("Please enter a valid crime")
            continue
        else:
            return CrimeID


def get_data(url, term=None):
    while True:
        try:
            start_date = input("Enter a start date (default is 2000-01-01)\n"
                               "Format: YYYY-MM-DD\n")
            if start_date == '':
                start_date = '2000-01-01'
                break
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid input, please use the correct format\n")
            continue
        else:
            break
    while True:
        try:
            end_date = input("Enter an end date (default is today)\n"
                             "Format: YYYY-MM-DD\n")
            if end_date == '':
                end_date = datetime.datetime.now().strftime("%Y-%m-%d")
                break
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid input, please use the correct format\n")
            continue
        else:
            break
    while True:
        try:
            limit = input("How many results would you like to see? (int)\n"
                          "Default is all\n")
            if limit == '':
                limit = 1500
                break
            if type(int(limit)) is not int:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter an integer")
            continue
        else:
            break

    if term is None:
        payload = {'start_date': start_date, 'end_date': end_date, 'limit': limit}
    else:
        payload = {'term': term, 'start_date': start_date, 'end_date': end_date, 'limit': limit}

    resp = requests.get(url, params=payload)
    resp.raise_for_status()
    results = resp.json()

    return results


def all_crime_list(url):
    results = get_data(url)
    crimes = [all_crimes(**c) for c in results]
    printers.print_crimes(crimes)


def most_arrests_specified_crime(url):
    CrimeID = get_crime_id()
    url = url + f'/{CrimeID}'
    results = get_data(url)
    players = [top_players_for_crime(**p) for p in results]
    printers.print_top_players(players)


def team_most_arrests_for_crime(url):
    CrimeID = get_crime_id()
    url = url + f'/{CrimeID}'
    results = get_data(url)
    teams = [top_teams_for_crime(**t) for t in results]
    printers.print_top_teams(teams)


def most_arrested_pos_for_crime(url):
    CrimeID = get_crime_id()
    url = url + f'/{CrimeID}'
    results = get_data(url)
    positions = [top_positions_for_crime(**p) for p in results]
    printers.print_top_positions(positions)


def crime_timeline(url):
    CrimeID = get_crime_id()
    url = url + f'/{CrimeID}'
    results = get_data(url)
    timeline = [number_arrests(**a) for a in results]
    printers.crime_timeline(timeline)


def arrest_list(url):
    CrimeID = get_crime_id()
    url = url + f'/{CrimeID}'
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
    printers.crime_details(details)
