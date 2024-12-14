import datetime
import pytz
import tkinter as tk
import ctypes

# Set the timezone to Hawaii-Aleutian Standard Time
hawaii_tz = pytz.timezone('Pacific/Honolulu')

# Define constants for preventing sleep mode on Windows
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002
ES_AWAYMODE_REQUIRED = 0x00000040

def prevent_sleep():
    """Prevents the system from going to sleep."""
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED | ES_AWAYMODE_REQUIRED)

def allow_sleep():
    """Allows the system to go to sleep."""
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

# Function to update the clock display
def update_clock():
    prevent_sleep()  # Prevent sleep mode while the clock is running

    # Get the current UTC time
    now_utc = datetime.datetime.now(pytz.utc)
    
    # Convert UTC time to HST
    now_hst = now_utc.astimezone(hawaii_tz)
    
    # Format the time, date, and timezone as strings
    formatted_time_hst = now_hst.strftime('%I:%M:%S %p')
    formatted_date_hst = now_hst.strftime('%Y-%m-%d')
    formatted_tz_hst = now_hst.strftime('%Z %z')
    
    # Update the labels with the current time, date, and timezone
    time_label.config(text=formatted_time_hst)
    date_label.config(text=formatted_date_hst)
    tz_label.config(text=formatted_tz_hst)
    
    # Schedule the function to update the time after 1 second
    time_label.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("ClockWork")

# Create labels to display the time, date, and timezone
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='darkgreen', foreground='gold')
time_label.pack(anchor='center')

date_label = tk.Label(root, font=('calibri', 20, 'bold'), background='darkgreen', foreground='gold')
date_label.pack(anchor='center')

tz_label = tk.Label(root, font=('calibri', 15, 'bold'), background='darkgreen', foreground='gold')
tz_label.pack(anchor='center')

# Add a protocol handler to allow sleep mode when the window is closed
def on_closing():
    allow_sleep()  # Allow the system to sleep again
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the clock update function
update_clock()

# Run the main event loop
root.mainloop()

