
# Formula 1 Webhook Script

This Python script fetches the latest Formula 1 race results, upcoming race information, and driver standings, then sends updates to a specified Discord channel using a webhook. It runs on a Raspberry Pi and can be scheduled using cron jobs.

## Features
- **Race Results**: Fetches and sends the results of the most recent Formula 1 race.
- **Upcoming Race Info**: Sends information about the next scheduled Formula 1 race (date, location, etc.).
- **Driver Standings**: Sends the top 10 drivers' current standings.

## Prerequisites
1. **Python 3**: Ensure Python 3 is installed on your system.
2. **Required Libraries**: Install the `requests` library to handle API requests.
   ```bash
   pip3 install requests
   ```

3. **Discord Webhook**: A Discord webhook URL is required to post the updates in a Discord channel. You can create a webhook by going to the settings of your desired Discord channel and navigating to **Integrations** > **Webhooks**.

## Setup Instructions

### 1. Clone or Download the Script
Place the script in the `/home/daspanda/scripts/` directory on your Raspberry Pi. You can name it `f1_webhook.py`.

### 2. Configure Webhook URL
Update the `DISCORD_WEBHOOK_URL` variable in the script with your Discord webhook URL.

```python
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

### 3. Run the Script Manually
You can manually test the script to ensure it works by running:

```bash
python3 /home/daspanda/scripts/f1_webhook.py
```

### 4. Automating the Script with Cron Jobs
To automate the script, you can set up a cron job to run it at regular intervals.

#### Example Cron Jobs

- **Race Results on Sundays at 5 PM**:
  ```bash
  0 17 * * SUN /usr/bin/python3 /home/daspanda/scripts/f1_webhook.py
  ```

- **Next Race Info on Fridays at 9 AM**:
  ```bash
  0 9 * * FRI /usr/bin/python3 /home/daspanda/scripts/f1_webhook.py
  ```

- **Daily Standings Update at 9 AM**:
  ```bash
  0 9 * * * /usr/bin/python3 /home/daspanda/scripts/f1_webhook.py
  ```

To edit your crontab, use the following command:
```bash
crontab -e
```

### 5. Updating the Script
For any changes, you can directly edit the script at `/home/daspanda/scripts/f1_webhook.py` and re-run or re-schedule it as needed.

### 6. Stopping or Adjusting Cron Jobs
To stop or modify any scheduled jobs, use `crontab -e` and either remove or update the relevant cron entries.

## Known Issues
- The Ergast API is deprecated at the end of 2024. After that, you’ll need to switch to the Jolpica API (a replacement API) to continue fetching live Formula 1 data.
- The script currently fetches only the most recent results and upcoming race details. Future features can include live race updates or custom notifications based on race events.

## Contributing
If you'd like to enhance the script or add new features (such as live race tracking or race reminders), feel free to modify the code or reach out!
