import requests
from bs4 import BeautifulSoup, Comment
import re
import warnings
import datetime
from enums import NFL_TEAMS

# Suppresses Beautiful Soup warnings due to reading HTML as a string instead of a file
warnings.filterwarnings("ignore", category=UserWarning)

def schedule (team_name, year):
    schedule = []
    for abbr, name in NFL_TEAMS.items():
        if name.lower() == team_name.lower():
            team_abbr = abbr
            break

    if team_abbr is None:
        print("Error: Team not found.")
        return

    # Uses the datetime package to store the current year
    # current_year = datetime.datetime.now().year

    # Configures the URL with the team and year
    url = f"https://www.pro-football-reference.com/teams/{team_abbr.lower()}/{year}.htm"

        # Sends GET request to the URL
    response = requests.get(url)
    # Checks if the page loaded, if not print error and return empty list
    if response.status_code != 200:
        print("Error: Unable to fetch roster.")
        return
    # Parses the HTML content using Beautiful Soup package
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', id="games")
    if table:
        # Table found within comments
        rows = table.find('tbody').find_all('tr')
        for row in rows:
        # Splits the row at the table cell delimeter
            row_parts = str(row).split('</td><td')
            week_num_match = re.search(r'"week_num" scope="row">(.*?)</th>', str(row_parts))
            # Checks if the name exists
            if week_num_match:
                # Stores the line with the players name as additional splitting needed
                week_num = week_num_match.group(1)

            date_match = re.search(r'data-stat="game_date">(.*?)'+"',", str(row_parts))
            # Checks if the name exists
            if date_match:
                # Stores the line with the players name as additional splitting needed
                date = date_match.group(1)

            time_match = re.search(r'data-stat="game_time">(.*?)'+"',", str(row_parts))
            # Checks if the name exists
            if time_match:
                # Stores the line with the players name as additional splitting needed
                time = time_match.group(1)

            opponent_match = re.search(r''+str(year)+'.htm">(.*?)</a>', str(row_parts))
            # Checks if the name exists
            if opponent_match:
                # Stores the line with the players name as additional splitting needed
                opponent = opponent_match.group(1)
            
            location_match = re.search(r'data-stat="game_location">(.*?)'+"',", str(row_parts))
            # Checks if the name exists
            if location_match:
                # Stores the line with the players name as additional splitting needed
                location = location_match.group(1)
                if location == "":
                    location = "vs."

            team_score_match = re.search(r'data-stat="pts_off">(.*?)'+"',", str(row_parts))
            # Checks if the name exists
            if team_score_match:
                # Stores the line with the players name as additional splitting needed
                team_score = team_score_match.group(1)

            opponent_score_match = re.search(r'data-stat="pts_def">(.*?)'+"',", str(row_parts))
            # Checks if the name exists
            if opponent_score_match:
                # Stores the line with the players name as additional splitting needed
                opponent_score = opponent_score_match.group(1)

            player_data = {
                    'week': week_num,
                    'date': date,
                    'time': time,
                    'opponent': opponent,
                    'location': location,
                    'team_score': team_score,
                    'opponent_score': opponent_score
                }
            schedule.append(player_data)
    return schedule
            

def main ():
    team_name = input ("Enter Team: ")
    week_number = input ("Enter Week Number or 'All' for All: ")
    year = input ("Enter Year (YYYY): ")
    if year == '':
        year = 2023
    
    team_schedule = schedule(team_name, year)

    for game in team_schedule:
        print (game)

    for game in team_schedule:
        week = game['week']
        date = game['date']
        time = game['time']
        opponent = game['opponent']
        location = game['location']
        team_score = game['team_score']
        opponent_score = game['opponent_score']

        if week_number == "All":
            print ("Week " + week + " - " + date + ", " + time, sep="\n")
        else:
            if week == week_number:
                print ("Week " + week + " - " + date + ", " + time, sep="\n")
            else:
                continue

main ()

