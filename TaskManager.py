import csv
from datetime import datetime, timedelta
import re


def convert_to_metric_time(time_str):
    # Convert time to 24-hour format
    try:
        time_24hr = datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")
    except ValueError:
        # If the time format is only 'H'
        time_24hr = datetime.strptime(time_str, "%H").strftime("%H:%M")

    # Split hours and minutes
    hours, minutes = map(int, time_24hr.split(':'))

    # Convert to metric time
    metric_hours = hours // 2
    metric_minutes = (hours % 2) * 50 + minutes // 6

    # Format metric time
    metric_time = "{:02d}:{:02d}".format(metric_hours, metric_minutes)

    return metric_time


def add_task_to_csv(command):
    # Extract date, time, and task from the command
    temp_date = None
    temp_time = None
    task = None

    # Check if date and time are mentioned in the command
    date_match = re.search(r'\bon\s(\w+\s\d+)', command)

    if date_match:
        # Extract date if provided
        date_str = date_match.group(1)
        temp_date = datetime.strptime(date_str, '%b %d').replace(year=datetime.today().year)
        if temp_date < datetime.today():
            temp_date = temp_date.replace(year=temp_date.year + 1)

    # Extract time if provided
    time_keywords = ["am", "pm"]
    time_list = re.split(r'\s+', command)

    if any(keyword in time_list for keyword in time_keywords):
        keyword_index = next(
            (i for i, item in enumerate(time_list) if any(keyword in item.lower() for keyword in time_keywords)), None)
        if keyword_index is not None:
            # Extract the time string before the keyword
            time_str = time_list[keyword_index - 1]

            # Convert and set time to metric time
            temp_time = convert_to_metric_time(time_str)
    else:
        # Set default time to 08:00 if no time is specified
        temp_time = '08:00'

    # Extract the task
    task_start_index = command.find('that') + 4
    task = command[task_start_index:].strip()

    # Set default values if date or time is not provided
    if temp_date is None:
        temp_date = datetime.today()

    # Add the extracted data to the CSV file
    with open('CsvFiles/tasks.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Time', 'Task']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write a new row
        writer.writerow({'Date': temp_date.strftime('%Y-%m-%d'), 'Time': temp_time, 'Task': task})


if __name__ == "__main__":
    # Test cases
    commands = [
        "hey set a task on jan 5  that I wanna go to a party at 5 a.m.",

    ]

    # Add tasks to the CSV for each command
    for command in commands:
        add_task_to_csv(command)
