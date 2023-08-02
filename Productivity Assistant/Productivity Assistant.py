import tkinter as tk # for ui
import time # for pomidor timer



def set_timer(option=None, text_box=None) -> None:

    """
    Set a timer for 'pomidor' work sessions with breaks.

    Parameters:
        option (int, optional): The number of 'pomidors' (work sessions) chosen by the user.
                                Valid options are 1, 2, or 3. Defaults to None.
        text_box (Text, optional): The tkinter Text widget to display the timer messages.
                                   Defaults to None.

    Returns:
        None

    The function sets two timers: one for the work session and another for the break session.
    For each 'pomidor', the work timer is set for 25 minutes, followed by a 5-minute break.
    The work timer will display messages for "Work time!" and "Break time!" in the specified
    text_box after the work and break durations expire.
    """

    if option is not None and text_box is not None:
        work_duration = option * 25
        break_duration = option * 5

        text_box.insert(tk.END, f"Work for {work_duration} minutes\n")
        #time.sleep(work_duration * 60)
        text_box.insert(tk.END, "Break time!\n")

        text_box.insert(tk.END, f"Break for {break_duration} minutes\n")
        #time.sleep(break_duration * 60)
        text_box.insert(tk.END, "Work time!\n")

    return None 

def get_pomidor() -> int:

    """
    Prompt the user to choose the number of 'pomidor' work sessions and set a timer.

    Returns:
        int: The number of 'pomidors' (work sessions) chosen by the user.

    This function asks the user to input the desired number of 'pomidor' work sessions (1, 2, or 3).
    It validates the input, and if the chosen option is valid, it sets a timer for the work sessions.
    For each 'pomidor', the work timer is set for 25 minutes, followed by a 5-minute break.
    The function calls the set_timer() function to handle the actual timer functionality.
    If the user provides an invalid input or a non-integer value, the function will keep asking
    until a valid option is provided.
    """

    while True:
        try:
            option = int(input("How many pomidors would you like to work?"))
            if option in[1, 2, 3]:
                print(f"Setting timer for {option} poms")
                set_timer(option)
                return option
            else:
                print("Huh? Tell me again? 1, 2 or 3?")
        except ValueError:
            print("Huh? Tell me again? 1, 2 or 3?")

    return int

def start_timer(option, text_box, automatic_start_var) -> None:

    """
    Start the timer based on user-selected options.

    This function is called when the "Start Timer" button is pressed.
    It reads the user-selected options for 'pomidor' work sessions from the UI.
    If the automatic start option is selected, it calls the set_timer() function
    to start the timer with the selected number of 'pomidors' automatically.
    If the automatic start option is not selected, it displays a message in the text box
    indicating that the timer will start on button press.
    """

    if automatic_start_var.get() == 1:
        set_timer(option, text_box)
    else:
        text_box.insert(tk.END, "Press start to start timer\n")
    
    return None

def ui() -> None:
   
    """
    Create the tkinter-based user interface for the Pom Timer application.

    Returns:
        None

    The function sets up the graphical user interface using tkinter.
    It includes an entry field for the user to input the desired number of 'pomidor' work sessions.
    The user can also choose an option to start the timer automatically or manually on button press.
    The timer messages are displayed on a text box within the application window.
    When the user clicks the "Start Timer" button, the timer messages are displayed in the text box
    as the timers progress.
    """

    # Main application
    app = tk.Tk()
    app.title("Pom Timer")

    # Number of poms
    pomidor_lable = tk.Label(app, text="How many pomidors would you like to work?")
    pomidor_lable.pack()
    pomidor_var = tk.IntVar()
    pomidor_entry = tk.Entry(app, textvariable=pomidor_var)
    pomidor_entry.pack()

    # Automatic Start Pom Checkbutton
    automatic_start_var = tk.IntVar()
    automatic_start_checkbutton = tk.Checkbutton(app, text="Start Timer Automatically", variable=automatic_start_var)
    automatic_start_checkbutton.pack()

    # Text widget to display messages
    text_box = tk.Text(app, height=10, width=40)
    text_box.pack()

    # Start timer button
    start_button = tk.Button(app, text="Start Timer", command=lambda: start_timer(pomidor_var.get(), text_box, automatic_start_var))
    start_button.pack()

    app.mainloop()

    return None


def main() -> None:

    while True:
        response = input("Do you want to set a work session?").lower()
        if response.startswith("y"):
            get_pomidor()
        else:
            print("Quit")
            break

    return None



if __name__ == "__main__":
    #main() # Terminal based UI
    ui() # UI



### END OF FILE ###



### TO DO ###

# CALENDAR #
# Add tasks in pomidors
# Brakes are added at the end of pomidors
# Tasks can be automatically allocated to calendar based on carcadian rythem
# Tasks can be automatically allocated to calendar based on time to complete
# Suggest afternoon slump
# Suggest meal times
    # Takes into account when you get hungry compared to macros
# Suggest bedtime
# Suggest waketime
# Research
    # App: Motion
    # Book: The Power of When'

# FINANCES #
# 50/30/20

# HABITS #
# Habit tracker
# System tracker
# System builder
# Systems
    # Cleaning/tidy habit (everybody cleans/tidy)
    # Cosmetic
    # Hygeine
    # Pre Work Session
    # Post Work Session
# Research
    # The Poka-Yoke Approach
    # Book: Atomic Habits
    # Book: The Life-Changing Magic of Tidying
    # Book: Working Hard, Hardly Working

# NOTES #
# Research how to take good notes
# Templates
    # Meeting notes template
    # Class notes template
    # Programming schematic template
# Incorporate SEN tactics
    # Spell checker
    # Grammer checker
    # Text to speech

# POMIDOR TIMER #
# Play noise when pom is finished
# Set a custom time
# Set custom break times
# Wipe text box after typing in a number
# Parkinsons Law
# Display the timer
# the time.sleep() function will halt the program execution for the specified duration, so be mindful when using it in your code. If you want to perform other actions while the timer is running, you can consider using threading or asynchronous programming. 

# SECOND BRAIN #
# Capture
    #
# Organise
    #
# Distill
    #
# Express
    #
# Research 
    # Book: Building a Second Brain

# TASK LIST # 
# Tasks can be allocated an esimated pom time
# Tasks can be allocated a difficulty
# Tasks can be grouped by study subject or catagory
# Automatic Eisenhower matrix
    # Auto list tasks that can be delegated to chatGPT
        # Make key notes from a source
        # Summerise a source
        # Write LinkedIn posts
        # Write a text
        # Ask interview questions with feedback
# Parkinsons Law
# Prep for tomorrow
# Study with me
# Study motivation
# Chores
    # Clean surfaces
    # Tidy surfaces
    # Clean windows
    # Hoover
    # Washing
        # Lights
        # Darks
        # Colours
        # Bedding/Towels
# Challenges
    # 1 week
        #
    # 2 week
        #
    # 3 week
        #
    # 4 week
        #
    # 3 month
        #
    # 6 month
        #
    # 1 year
        #

# UI #
# Ask questions in a text box
# Display the timer on screen
# Add a menu to choose between features
# Themes
    # Neon
    # Spring
    # Autumn
    # Winter
    # Summer
# Tasks can be viewed in an Eisenhower matrix
# Pop out timer (so you can have it in the corner of your screen)
# Notes are contained in a virtual notebook with pages turning and contents


### COMPLETED ###

# POMIDOR TIMER #
# Asks the user if they want to set a timer
# Asks for user input
# Set timer 
# Asks the user how many pomidors
# Set timer for short (1 pom), medium (2 poms) or long (3 poms)
# Add break times to pomidors
# Option for timers to start automatically or on a button press

# UI #
# Basic UI
# Displays text to screen



# EDGE CASES #
# try-except added to set_timer to only accept ints
# Text input coverted to lower to account for capital letters
# try-except added to get_pomidors to only accept ints
