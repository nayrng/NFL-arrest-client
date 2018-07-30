import collections
from crime_data import get_data, all_crimes as position_crime, number_arrests, arrest_detail_list
from valid_data import valid_positions

base_url = 'http://nflarrest.com/api/v1/position'

position_count = collections.namedtuple('position_count',
                                        'Position arrest_count')

team_positions = collections.namedtuple('team_positions',
                                        'Team arrest_count')


def get_position():
    while True:
        try:
            position = input("Enter a position\n"
                             "or type 'HELP' for all valid positions\n")
            if position.upper() == 'HELP':
                for each in valid_positions:
                    print(each)
                print()
                continue
            if position.upper() not in valid_positions:
                raise LookupError
        except LookupError:
            print("Please enter a valid position")
            continue
        else:
            return position


def all_position_crime(url):
    results = get_data(url)
    positions = [position_count(**p) for p in results]
    return positions


def top_teams_position(url):
    position = get_position()
    url = url + f'/topTeams/{position}'
    results = get_data(url)

    data = []
    for each in results:
        pos = team_positions(
            Team=each.get('Team'),
            arrest_count=each.get('arrest_count')
        )
        data.append(pos)
    return data


def crime_by_position(url):
    position = get_position()
    url = url + f'/topCrimes/{position}'
    results = get_data(url)
    crimes = [position_crime(**p) for p in results]
    return crimes


def crime_timeline(url):
    position = get_position()
    url = url + f'/timeline/{position}'
    results = get_data(url)
    timeline = [number_arrests(**c) for c in results]
    return timeline


def crime_details(url):
    position = get_position()
    url = url + f'/arrests/{position}'
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
