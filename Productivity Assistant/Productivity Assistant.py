import time



def set_timer(minutes) -> None:

    print(f"Timer set for {minutes} minutes")
    #time.sleep(minutes * 60)
    print("Time's up!")

    return None 



def get_pomidor() -> int:

    while True:
        try:
            option = int(input("How many pomidors would you like to work?"))
            if option in[1, 2, 3]:
                print(f"Setting timer for {option} poms")
                if option == 1:
                    set_timer(25)
                elif option == 2:
                    set_timer(50)
                elif option == 3:
                    set_timer(75)
                return option
            else:
                print("Huh? Tell me again? 1, 2 or 3?")
        except ValueError:
            print("Huh? Tell me again? 1, 2 or 3?")

    return int



def main() -> None:

    while True:
        response = input("Do you want to set a work session?").lower()
        if response.startswith("y"):
            set_timer()
        else:
            print("Quit")
            break

    return None



if __name__ == "__main__":
    #main()
    pomidor_duration = get_pomidor()



### END OF FILE ###



### TO DO ###

# CALENDAR #
# Add tasks in pomidors
# Brakes are added at the end of pomidors
# Tasks can be automatically allocated to calendar based on carcadian rythem
# Tasks can be automatically allocated to calendar based on time to complete
# Suggest afternoon slump
# Suggest meal times
# Suggest bedtime
# Suggest waketime

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
# the time.sleep() function will halt the program execution for the specified duration, so be mindful when using it in your code. If you want to perform other actions while the timer is running, you can consider using threading or asynchronous programming. 

# SECOND BRAIN #

# TASK LIST # 
# Tasks can be allocated an esimated pom time
# Tasks can be allocated a difficulty
# Tasks can be grouped by study subject or catagory
# Automatic Eisenhower matrix

# UI #
# Ask questions in a text box
# Display the timer on screen
# Tasks can be viewed in an Eisenhower matrix


### COMPLETED ###

# POMIDOR TIMER #
# Asks the user if they want to set a timer
# Asks for user input
# Set timer 
# Asks the user how many pomidors
# Set timer for short (1 pom), medium (2 poms) or long (3 poms)



# EDGE CASES #
# try-except added to set_timer to only accept ints
# Text input coverted to lower to account for capital letters
# try-except added to get_pomidors to only accept ints
