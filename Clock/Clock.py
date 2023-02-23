# Asks the user how long to wait then counts down and plays a sound file

import time
import playsound
from playsound import playsound

# Countdown on one line
# ANSI = invisible characters that manipulate the terminal went printed to the terminal
CLEAR = "\033[2J" # Clear the terminal screen 
CLEAR_AND_RETURN = "\033[H" # returns the curser to its home position so it prints over the original


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # 125 // 60 = 2
        seconds_left = time_left % 60 # 125 % 60 = 5

        # 02s = make it 2 didets pad it with 0 if it only has 1
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")

    playsound("Alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds) 