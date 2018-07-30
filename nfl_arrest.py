import crime_data
import team_data
import player_data
import position_data
import printers


def stats_by_crime():
    choice = 'run'
    while choice.lower() != 'x':
        url = crime_data.base_url
        choice = input("a. Return most popular crimes in the NFL\n"  # done
                       "b. Return players who have committed the specified crime the most\n"  # done
                       "c. Return teams with most arrests for the specified crime\n"  # done
                       "d. Return most arrested positions for specified crime\n"  # done
                       "e. Returns number of arrests in a specific time period\n"  # done
                       "f. Returns list of arrests with detail for the specified crime\n")  # done

        if choice.lower() == 'a':
            crime_data.all_crime_list(url)

        if choice.lower() == 'b':
            url = url + '/topPlayers'
            crime_data.most_arrests_specified_crime(url)

        if choice.lower() == 'c':
            url = url + '/topTeams'
            crime_data.team_most_arrests_for_crime(url)

        if choice.lower() == 'd':
            url = url + '/topPositions'
            crime_data.most_arrested_pos_for_crime(url)

        if choice.lower() == 'e':
            url = url + '/timeline'
            crime_data.crime_timeline(url)

        if choice.lower() == 'f':
            url = url + '/arrests'
            crime_data.arrest_list(url)


def stats_by_team():
    choice = 'run'
    while choice.lower() != 'x':
        url = team_data.base_url
        choice = input("a. Return teams with the most arrests\n"  # done
                       "b. Returns most arrested players from specified team\n"  # done
                       "c. Returns top crime from specified team\n"  # done
                       "d. Returns a count of arrests for a specified time for a team\n"  # done
                       "e. Returns a list of arrest details for a specified team\n")  # done

        if choice.lower() == 'a':
            results = team_data.top_arrested_teams(url)
            print(f"Displaying {len(results)} results:")
            printers.top_teams(results)
        if choice.lower() == 'b':
            url = url + '/topPlayers'
            results = team_data.top_players_arrested(url)
            print(f"Displaying {len(results)} results:")
            printers.print_top_players(results)
        if choice.lower() == 'c':
            url = url + '/topCrimes'
            results = team_data.top_crimes_committed(url)
            print(f"Displaying {len(results)} results:")
            printers.print_crimes(results)
        if choice.lower() == 'd':
            url = url + '/timeline'
            results = team_data.team_crime_timeline(url)
            print(f"Displaying {len(results)} results")
            printers.crime_timeline(results)
        if choice.lower() == 'e':
            url = url + '/arrests'
            results = team_data.arrest_details(url)
            print(f"Displaying {len(results)} results")
            printers.crime_details(results)


def stats_by_player():
    choice = 'run'
    while choice.lower() != 'x':
        url = player_data.base_url
        choice = input("a. Return the most arrested players\n"  # done
                       "b. Return the top crimes by specific player\n"  # done
                       "c. Search for a player\n"  # done
                       "d. Return list of arrest details for player\n")  # done

        if choice.lower() == 'a':
            results = player_data.top_players_arrested(url)
            print(f"Displaying {len(results)} results:")
            printers.print_top_players_with_team(results)

        if choice.lower() == 'b':
            url = url + '/topCrimes'
            results = player_data.top_crimes(url)
            print(f"Displaying {len(results)} results:")
            printers.print_top_crimes(results)

        if choice.lower() == 'c':
            url = url + '/search'
            results = player_data.player_search(url)
            print(f"Displaying {len(results)} results:")
            printers.print_player_by_name(results)

        if choice.lower() == 'd':
            url = url + '/arrests'
            results = player_data.crime_details(url)
            printers.crime_details(results)


def stats_by_position():
    choice = 'run'
    while choice.lower() != 'x':
        url = position_data.base_url
        choice = input("a. Return the most arrested positions\n"
                       "b. Return teams with most arrested players for specified position\n"
                       "c. Returns crimes with the most arrests committed by specified position\n"
                       "d. Returns number of arrests in a timeframe for a specified position\n"
                       "e. Returns arrest details for all players of a specified position\n")

        if choice.lower() == 'a':
            results = position_data.all_position_crime(url)
            printers.print_top_positions(results)
        if choice.lower() == 'b':
            results = position_data.top_teams_position(url)
            printers.print_top_teams(results)
        if choice.lower() == 'c':
            results = position_data.crime_by_position(url)
            printers.print_crimes(results)
        if choice.lower() == 'd':
            results = position_data.crime_timeline(url)
            printers.crime_timeline(results)
        if choice.lower() == 'e':
            results = position_data.crime_details(url)
            printers.crime_details(results)


def main():
    choice = 'run'
    print('NFL arREST Client\n'
          'created by Ryan Ng\n')
    while choice.lower() != 'x':
        choice = input("a. Look up arrests by crime\n"
                       "b. Look up arrests by team\n"
                       "c. Look up arrests by player\n"
                       "d. Look up arrests by position\n")
        if choice.lower() == 'a':
            stats_by_crime()
        if choice.lower() == 'b':
            stats_by_team()
        if choice.lower() == 'c':
            stats_by_player()
        if choice.lower() == 'd':
            stats_by_position()
    print("Thank you for using this application created by Ryan Ng")


if __name__ == '__main__':
    main()
