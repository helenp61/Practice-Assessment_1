from tkinter import *

def quit():
    main_window.destroy()

def calculate_deck():
    print("Calculations will go here")

def main():
    global main_window
    global entry_deck_length
    global entry_deck_width
    global entry_deck_heigth   
    main_window =Tk()
    Button(main_window, text="Quit",command=quit) .grid(column=0, row=0)
    Button(main_window, text="Calculate",command=calculate_deck) .grid(column=1,row=0)
    
    Label(main_window, text="Length").grid(column=0,row=1)
    entry_deck_length = Entry(main_window)
    entry_deck_length.grid(column=1,row=1,padx=10,pady=5)
    
    Label(main_window, text="Width").grid(column=0,row=2)
    entry_deck_width = Entry(main_window)
    entry_deck_width.grid(column=1,row=2,padx=10,pady=5)
    
    Label(main_window, text="Height").grid(column=0,row=3)
    entry_deck_heigth = Entry(main_window)
    entry_deck_heigth.grid(column=1,row=3,padx=10,pady=5)
    main_window.mainloop()
    
main()
