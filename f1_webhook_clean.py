
import requests
import json

# Webhook URL (replace with your Discord webhook URL)
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

# API endpoints for Formula 1 data (can replace with Jolpica later)
BASE_URL = "http://ergast.com/api/f1/"

# Helper function to send message to Discord via webhook
def send_discord_message(content):
    data = {
        "content": content,
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Helper function to get race results and send to Discord
def send_race_results():
    try:
        url = f"{BASE_URL}current/last/results.json"  # Latest race results
        response = requests.get(url)
        data = response.json()

        race_info = data['MRData']['RaceTable']['Races'][0]
        race_name = race_info['raceName']
        race_date = race_info['date']
        race_location = race_info['Circuit']['Location']

        result_str = f"**{race_name}**\nDate: {race_date}\nLocation: {race_location['locality']}, {race_location['country']}\n\n**Results**\n"
        
        for result in race_info['Results']:
            driver = result['Driver']
            constructor = result['Constructor']
            result_str += f"{result['position']}. {driver['givenName']} {driver['familyName']} ({constructor['name']}) - {result['status']}\n"
        
        send_discord_message(result_str)
    except Exception as e:
        send_discord_message(f"Error fetching race results: {str(e)}")

# Helper function to get upcoming race info and send to Discord
def send_next_race_info():
    try:
        url = f"{BASE_URL}current/next.json"  # Next race info
        response = requests.get(url)
        data = response.json()

        race_info = data['MRData']['RaceTable']['Races'][0]
        race_name = race_info['raceName']
        race_date = race_info['date']
        race_location = race_info['Circuit']['Location']

        message = f"**Next Race: {race_name}**\nDate: {race_date}\nLocation: {race_location['locality']}, {race_location['country']}"
        send_discord_message(message)
    except Exception as e:
        send_discord_message(f"Error fetching next race info: {str(e)}")

# Helper function to get driver standings and send to Discord
def send_driver_standings():
    try:
        url = f"{BASE_URL}current/driverStandings.json"  # Current driver standings
        response = requests.get(url)
        data = response.json()

        standings_info = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        standings_str = "**Driver Standings**\n"
        
        for standing in standings_info[:10]:  # Top 10 drivers
            driver = standing['Driver']
            constructor = standing['Constructors'][0]
            standings_str += f"{standing['position']}. {driver['givenName']} {driver['familyName']} - {standing['points']} points ({constructor['name']})\n"
        
        send_discord_message(standings_str)
    except Exception as e:
        send_discord_message(f"Error fetching driver standings: {str(e)}")

# Example functions to trigger (these could be scheduled with cron jobs or event-based)
send_race_results()  # Post the latest race results to Discord
send_next_race_info()  # Post upcoming race info to Discord
send_driver_standings()  # Post driver standings to Discord
