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
add_event(datetime.datetime(2024, 12, ), "00:00 - 01:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "01:00 - 02:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "02:00 - 03:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "03:00 - 04:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "04:00 - 05:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "05:00 - 06:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "06:00 - 07:00", "Sleep")
add_event(datetime.datetime(2024, 12, 6), "07:00 - 08:00", "Breakfast")
add_event(datetime.datetime(2024, 12, 6), "08:00 - 09:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "09:00 - 10:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "10:00 - 11:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "11:00 - 12:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "12:00 - 13:00", "Lunch")
add_event(datetime.datetime(2024, 12, 6), "13:00 - 14:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "14:00 - 15:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "15:00 - 16:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "16:00 - 17:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "17:00 - 18:00", "Work")
add_event(datetime.datetime(2024, 12, 6), "18:00 - 19:00", "Dinner")
add_event(datetime.datetime(2024, 12, 6), "19:00 - 20:00", "Relax")
add_event(datetime.datetime(2024, 12, 6), "20:00 - 21:00", "Relax")
add_event(datetime.datetime(2024, 12, 6), "21:00 - 22:00", "Relax")
add_event(datetime.datetime(2024, 12, 6), "22:00 - 23:00", "Relax")
add_event(datetime.datetime(2024, 12, 6), "23:00 - 24:00", "Sleep")


    

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
