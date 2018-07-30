from prettytable import PrettyTable


def print_crimes(list):
    tables = PrettyTable(['Crime', 'Arrest Count'])
    for c in list:
        tables.add_row([c.Category, c.arrest_count])
    print(tables)


def print_top_players(list):
    tables = PrettyTable(['Name', 'Arrest Count'])
    for p in list:
        tables.add_row([p.Name, p.arrest_count])
    print(tables)


def print_top_teams(list):
    tables = PrettyTable(['Team', 'Arrest Count'])
    for t in list:
        tables.add_row([f'{t.Team}', t.arrest_count])
    print(tables)


def print_top_positions(list):
    tables = PrettyTable(['Position', 'Arrest Count'])
    for p in list:
        tables.add_row([p.Position, p.arrest_count])
    print(tables)


def crime_timeline(list):
    tables = PrettyTable(['Month - Year', 'Arrest Count'])
    for t in list:
        tables.add_row([f'{t.Month}/{t.Year}', t.arrest_count])
    print(tables)


def crime_details(list):
    tables = PrettyTable(['Date', 'Name', 'Position', 'Team', 'Crime', 'Description', 'Outcome'])
    for d in list:
        tables.add_row([d.Date, d.Name, d.Position, d.Team, d.Crime_category, d.Description, d.Outcome])
    print(tables)


def top_teams(list):
    tables = PrettyTable(['Team', 'Arrest Count'])
    for t in list:
        tables.add_row([t.Team_preffered_name, t.arrest_count])
    print(tables)


def print_top_players_with_team(list):
    tables = PrettyTable(['Name', 'Team', 'Position', 'Arrest Count'])
    for t in list:
        tables.add_row([t.Name, t.Team, t.Position, t.arrest_count])
    print(tables)


def print_top_crimes(list):
    tables = PrettyTable(['Crime', 'Arrest Count'])
    for t in list:
        tables.add_row([t.category, t.arrest_count])
    print(tables)


def print_player_by_name(list):
    tables = PrettyTable(['Name', 'Position', 'Arrest Count'])
    for t in list:
        tables.add_row([t.Name, t.Position, t.arrest_count])
    print(tables)
