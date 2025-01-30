import json
import dateparser
from datetime import datetime

REMINDERS_FILE = "reminders.json"

def load_reminders():
    """Load reminders from the JSON file."""
    try:
        with open(REMINDERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"reminders": []}

def save_reminders(reminders):
    """Save reminders to the JSON file."""
    with open(REMINDERS_FILE, "w") as file:
        json.dump(reminders, file, indent=4)

def set_reminder(task, time_str):
    """Set a new reminder."""
    reminders = load_reminders()
    parsed_time = dateparser.parse(time_str)
    if not parsed_time:
        return "I couldn't understand the time. Please try again."

    reminder = {"task": task, "time": parsed_time.strftime("%Y-%m-%d %H:%M")}
    reminders["reminders"].append(reminder)
    save_reminders(reminders)
    return f"Reminder set: '{task}' at {parsed_time.strftime('%Y-%m-%d %H:%M')}."

def get_upcoming_reminders():
    """Retrieve upcoming reminders."""
    reminders = load_reminders()
    now = datetime.now()
    upcoming = [
        r for r in reminders["reminders"]
        if datetime.strptime(r["time"], "%Y-%m-%d %H:%M") > now
    ]
    if not upcoming:
        return "You have no upcoming reminders."
    return "\n".join([f"{r['task']} at {r['time']}" for r in upcoming])