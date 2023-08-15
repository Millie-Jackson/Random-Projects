import tkinter as tk # for UI
from PomidorTimer import PomTimer
from Calculator import Calculator



def main() -> None:

    while True:
        response = input("Calculator or Pom Timer?").lower()
        if response.startswith("c"):
            root = tk.Tk()
            calculator = Calculator(root)
            root.mainloop()
        elif response.startswith("p"):
            app = tk.Tk()
            pom_timer = PomTimer(app)
            app.mainloop()
        else:
            print("Quit")
            break

    return None



if __name__ == "__main__":

    main()



### END OF FILE ###



### TO DO ###

# CALENDAR #
# Round up
    # Review previous weeks success and failures
    # Look at thte next 4 weeks
    # Make sure your goals are still aligned to your priorities
    # Update to do list, make sure your on track
    # What 3 things would I accomplish  in the next week?
    # Schedual time to work towards these three things
# Add tasks in pomidors
# Brakes are added at the end of pomidors
# Tasks can be automatically allocated to calendar based on carcadian rythem
# Tasks can be automatically allocated to calendar based on time to complete
# Suggest afternoon slump
# Suggest meal times
    # Takes into account when you get hungry compared to macros
# Suggest bedtime
# Suggest waketime
# Levels
    # Level 1: Not using a calendar
    # Level 2: Schedualing appointments
    # Level 3: Timeboxing
    # Level 4: Ideal w eek
# Research
    # App: Motion
    # Book: The Power of When'

# EMAIL # 
# Research
    #SaneBox

# FINANCES #
# 50/30/20

# HABITS #
# Habit tracker
# System tracker
# System builder
# Experimental habits
    # Define: SMART task
    # Do:
    # Review: Make changes
# Systems
    # Cleaning/tidy habit (everybody cleans/tidy)
    # Cosmetic
    # Hygeine
    # Pre Work Session
    # Post Work Session
    # Gym
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

# STUDY
# Stage 1: Information Capture
# Stage 2: Information Processing
# Reccommended (or automatic) Study Scheduals
# Summerize text/research papers
# Automatically take notes from a text
# Mind Mapping Tool (automatic?)
# Flash Cards
# Research
    # Active Recall
    # Advanced Information Processing
    # Active Recall
    # App: Miro

# TASK LIST # 
# Tasks can be allocated an esimated pom time
# Tasks can be allocated a difficulty
# Tasks can be grouped by study subject or catagory
# Daily Adventure: Choose one task at the begining of each day that is the most important thing you need to do that day
# Side Quests: Choose up to three secondary tasks at the begining of each day (1 work, 1 life, 1 social)
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

# Touchtyping tool
# Learn to touchtype

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
