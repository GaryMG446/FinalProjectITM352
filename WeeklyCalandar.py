import datetime
import pandas as pd


# Set the start date
start_date = datetime.datetime(2024, 11, 29)

# Create a list of dates for the week
dates = [start_date + datetime.timedelta(days=i) for i in range(7)]

# Create a list of time slots for each hour of the day
time_slots = [f"{hour:02d}:00 - {hour + 1:02d}:00" for hour in range(24)]

# Create a multi-index from dates and time slots
index = pd.MultiIndex.from_product([dates, time_slots], names=['Date', 'Time Slot'])

# Create an empty DataFrame with the multi-index
weekly_calendar = pd.DataFrame(index=index, columns=['Event'])

# Function to add an event to the calendar
def add_event(date, time_slot, event):
    if (date, time_slot) in weekly_calendar.index:
        weekly_calendar.loc[(date, time_slot), 'Event'] = event
    else:
        print("Invalid date or time slot")

# Add events for the entire day on 11/29/2024
add_event(datetime.datetime(2024, 11, 29), "00:00 - 01:00", "Sleep")
add_event(datetime.datetime(2024, 11, 29), "01:00 - 02:00", "Sleep")
add_event(datetime.datetime(2024, 11, 29), "02:00 - 03:00", "Sleep")
add_event(datetime.datetime(2024, 11, 29), "03:00 - 04:00", "Sleep")
add_event(datetime.datetime(2024, 11, 29), "04:00 - 05:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 29), "05:00 - 06:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 29), "06:00 - 07:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 29), "07:00 - 08:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 29), "08:00 - 09:00", "Morning Exercise")
add_event(datetime.datetime(2024, 11, 29), "09:00 - 10:00", "Morning Exercise")
add_event(datetime.datetime(2024, 11, 29), "10:00 - 11:00", "Morning Exercise")
add_event(datetime.datetime(2024, 11, 29), "11:00 - 12:00", "School Work")
add_event(datetime.datetime(2024, 11, 29), "12:00 - 13:00", "School Work")
add_event(datetime.datetime(2024, 11, 29), "13:00 - 14:00", "School Work")
add_event(datetime.datetime(2024, 11, 29), "14:00 - 15:00", "School Work")
add_event(datetime.datetime(2024, 11, 29), "15:00 - 16:00", "School Work")
add_event(datetime.datetime(2024, 11, 29), "16:00 - 17:00", "School Work")
add_event(datetime.datetime(2024, 11, 29), "17:00 - 18:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 29), "18:00 - 19:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 29), "19:00 - 20:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 29), "20:00 - 21:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 29), "21:00 - 22:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 29), "22:00 - 23:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 29), "23:00 - 24:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "00:00 - 01:00", "Sleep")
add_event(datetime.datetime(2024, 11, 30), "01:00 - 02:00", "Sleep")
add_event(datetime.datetime(2024, 11, 30), "02:00 - 03:00", "Sleep")
add_event(datetime.datetime(2024, 11, 30), "03:00 - 04:00", "Sleep")
add_event(datetime.datetime(2024, 11, 30), "04:00 - 05:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 30), "05:00 - 06:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 30), "06:00 - 07:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 30), "07:00 - 08:00", "Morning Walk")
add_event(datetime.datetime(2024, 11, 30), "08:00 - 09:00", "Morning Exercise")
add_event(datetime.datetime(2024, 11, 30), "09:00 - 10:00", "Morning Exercise")
add_event(datetime.datetime(2024, 11, 30), "10:00 - 11:00", "Morning Exercise")
add_event(datetime.datetime(2024, 11, 30), "11:00 - 12:00", "School Work")
add_event(datetime.datetime(2024, 11, 30), "12:00 - 13:00", "School Work")
add_event(datetime.datetime(2024, 11, 30), "13:00 - 14:00", "School Work")
add_event(datetime.datetime(2024, 11, 30), "14:00 - 15:00", "School Work")
add_event(datetime.datetime(2024, 11, 30), "15:00 - 16:00", "School Work")
add_event(datetime.datetime(2024, 11, 30), "16:00 - 17:00", "School Work")
add_event(datetime.datetime(2024, 11, 30), "17:00 - 18:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "18:00 - 19:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "19:00 - 20:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "20:00 - 21:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "21:00 - 22:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "22:00 - 23:00", "Work GEN")
add_event(datetime.datetime(2024, 11, 30), "23:00 - 24:00", "Work GEN")
add_event(datetime.datetime(2024, 12, 1), "00:00 - 01:00", "Sleep")
add_event(datetime.datetime(2024, 12, 1), "01:00 - 02:00", "Sleep")



# Function to view the calendar with only scheduled events
def view_scheduled_events():
    scheduled_events = weekly_calendar.dropna()
    print(scheduled_events)

# Verify that every time slot for each day is present
def verify_time_slots():
    expected_slots = set(index)
    actual_slots = set(weekly_calendar.index)
    missing_slots = expected_slots - actual_slots

    if not missing_slots:
        print("All time slots are correctly included.")
    else:
        print("Missing time slots:")
        for slot in sorted(missing_slots):
            print(slot)

# Verify all time slots are present
verify_time_slots()

# View the calendar with only scheduled events
view_scheduled_events()
