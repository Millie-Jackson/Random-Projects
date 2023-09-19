"""
Main Program

This script provides the user with the choice to use either the Calculator or Pom Timer functionality.
It imports the Calculator and PomTimer classes from their respective modules and creates the corresponding user interfaces.

Author:
    [Millie J]

Date:
    [15.08.2023]

Version:
    0.2
"""



import tkinter as tk # for UI
from PomidorTimer import PomTimer
from Calculator import Calculator



def main() -> None:

    """
    Main program function.

    Prompts the user to choose between using the Calculator or Pom Timer functionality.
    Initializes the chosen functionality's user interface and enters the main event loop.

    Returns:
        None
    """

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
# Social Accountability?
# Gamification
# Schedual relax time
# Start Small
# The Power Of Three Rule
# Daily Journal
# Visualisation
# Recover From mistakes
# Manage Your Thoughts
# Delayed Gratification
# Organisation
# Eliminate 'but'
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
    # App: Habitify
    # App: Awesom Habits
    # App: Habitica
    # App: Strides
    # App: Productive
    # App: Streaks
    # App: Everyday
    # App: HabitBull
    # App: Avocation
    # App: Habit Tracker
    # App: Tangerine 

## Journal ##
# Gratitude Journal
# Reccord thoughts on the fly
    # Ask user to sort/tag thoughts at the end of a session 
# Diary
# Use Tags on Diary
    # Search for relivant entries on a topic
    # Summarise entries on a topic
# Review
    # Habits
    # Progress
    # Calander
    # Study

## NOTES ##
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
    # 5 Step Study System
        # Start Revising Early
        # Automation
        # Notes Consolidation
        # Recap Lecture Slides
        # Past Papers
    # App: Miro
    # App: Scribe

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

### UI ###
# Ask questions in a text box
# Display the timer on screen
# Add a menu to choose between features
# Allow for multiple feature/tool use simultaniously
# Allow for window pop outs for multiple features/tools
# Allow for combined window box placements to customise the 'desktop'
# Themes
    # Neon
    # Spring
    # Autumn
    # Winter
    # Summer
# Tasks can be viewed in an Eisenhower matrix
# Pop out timer (so you can have it in the corner of your screen)
# Notes are contained in a virtual notebook with pages turning and contents

### Research ###
# Forsters Commitment Inventory
# ABC Method
# Kanban Schedual
# Kaizen
# PDCA
# Poke Yoke
# Effortless Productivity
# Ikigai
# App: Tapilo (Linkedin Help)
# App: Tango (Create Tutorials)
# Influencer: Mike Dee


### COMPLETED ###

# POMIDOR TIMER #
# Asks the user if they want to set a timer
# Asks for user input
# Set timer 
# Asks the user how many pomidors
# Set timer for short (1 pom), medium (2 poms) or long (3 poms)
# Add break times to pomidors
# Option for timers to start automatically or on a button press
# Added a calculator fram a previous project
# Implemented OOP

# UI #
# Basic UI
# Displays text to screen



# EDGE CASES #
# try-except added to set_timer to only accept ints
# Text input coverted to lower to account for capital letters
# try-except added to get_pomidors to only accept ints
