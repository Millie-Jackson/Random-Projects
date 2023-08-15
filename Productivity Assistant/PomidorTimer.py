import tkinter as tk # for UI
import time # for timer



class PomTimer:
    def __init__(self, app):
        self.app = app

        # UI

        # Number of poms
        self.pomidor_lable = tk.Label(app, text="How many pomidors would you like to work?")
        self.pomidor_lable.pack()
        self.pomidor_var = tk.IntVar()
        self.pomidor_entry = tk.Entry(app, textvariable=self.pomidor_var)
        self.pomidor_entry.pack()

        # Automatic Start Pom Checkbutton
        self.automatic_start_var = tk.IntVar()
        self.automatic_start_checkbutton = tk.Checkbutton(app, text="Start Timer Automatically", variable=self.automatic_start_var)
        self.automatic_start_checkbutton.pack()

        # Text widget to display messages
        self.text_box = tk.Text(app, height=10, width=40)
        self.text_box.pack()

        # Start timer button
        self.start_button = tk.Button(app, text="Start Timer", command=lambda: self.start_timer(self.pomidor_var.get(), self.text_box, self.automatic_start_var))
        self.start_button.pack()



    def set_timer(self, option) -> None:

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

        if option is not None and tk.text_box is not None:
            work_duration = option * 25
            break_duration = option * 5

            tk.text_box.insert(tk.END, f"Work for {work_duration} minutes\n")
            #time.sleep(work_duration * 60)
            tk.text_box.insert(tk.END, "Break time!\n")

            tk.text_box.insert(tk.END, f"Break for {break_duration} minutes\n")
            #time.sleep(break_duration * 60)
            tk.text_box.insert(tk.END, "Work time!\n")

        return None 
    
    def get_pomidor(self) -> int:

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
                    self.set_timer(option)
                    return option
                else:
                    print("Huh? Tell me again? 1, 2 or 3?")
            except ValueError:
                print("Huh? Tell me again? 1, 2 or 3?")

        return int
    
    def start_timer(self) -> None:

        """
        Start the timer based on user-selected options.

        This function is called when the "Start Timer" button is pressed.
        It reads the user-selected options for 'pomidor' work sessions from the UI.
        If the automatic start option is selected, it calls the set_timer() function
        to start the timer with the selected number of 'pomidors' automatically.
        If the automatic start option is not selected, it displays a message in the text box
        indicating that the timer will start on button press.
        """

        if self.automatic_start_var.get() == 1:
            self.set_timer(tk.option, tk.text_box)
        else:
            self.text_box.insert(tk.END, "Press start to start timer\n")
        
        return None
    


## TO DO ##
# Play noise when pom is finished
# Set a custom time
# Set custom break times
# Wipe text box after typing in a number
# Parkinsons Law
# Display the timer
# the time.sleep() function will halt the program execution for the specified duration, so be mindful when using it in your code. If you want to perform other actions while the timer is running, you can consider using threading or asynchronous programming. 