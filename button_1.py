from tkinter import *


def quit():
    main_window.destroy()


def main():
    main_window = Tk()
    Button(main_window, text="Quit", command=quit) .grid()
    main_window.mainloop()


main()
# Previos
# Next
# Home
# Exit
# First Name
# Last Name
# Email address
# Contact Phone Number
