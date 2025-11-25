import datetime

def check_alarms(alarms, maintenance_windows):
    results = []
    for alarm in alarms:
        alarm_time = datetime.datetime.strptime(alarm, "%Y-%m-%dT%H:%M:%S")
        for window in maintenance_windows:
            start = datetime.datetime.strptime(window[0], "%Y-%m-%dT%H:%M:%S")
            end = datetime.datetime.strptime(window[1], "%Y-%m-%dT%H:%M:%S")
            if alarm_time >= start and alarm_time <= end:
                results.append(alarm)
    return results

alarms = ["2023-08-01T12:00:00", "2023-08-01T13:30:00", "2023-08-01T15:00:00"]
maintenance_windows = [
    ("2023-08-01T11:00:00", "2023-08-01T12:30:00"),
    ("2023-08-01T14:00:00", "2023-08-01T14:45:00")
]

print(check_alarms(alarms, maintenance_windows))
