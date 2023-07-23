import time



def set_timer() -> None:

    while True:
        try:
            seconds = int(input("How long would you like to work for?"))
            if seconds <= 0:
                print("Oops! Time only flows forward")
            else:
                break
        except ValueError:
            print("Huh? What do you mean? Please enter a time")

    print(f"Timer set for {seconds} seconds")
    time.sleep(seconds)
    print("Time's up!")

    return None 



def main() -> None:

    while True:
        response = input("Do you want to set a work session?")
        if response.startswith("y" or "Y"):
            set_timer()
        else:
            print("Quit")
            break

    return None



if __name__ == "__main__":
    main()



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
# Set timer
# Set timer for short (1 pom), medium (2 poms) or long (3 poms)
# Play noise when pom is finished
# the time.sleep() function will halt the program execution for the specified duration, so be mindful when using it in your code. If you want to perform other actions while the timer is running, you can consider using threading or asynchronous programming. 

# SECOND BRAIN #

# TASK LIST # 
# Tasks can be allocated an esimated pom time
# Tasks can be allocated a difficulty
# Tasks can be grouped by study subject or catagory



### COMPLETED ###

# POMIDOR TIMER #
# Ask the user if they want to set a timer
# Ask for user input
# Set timer 


