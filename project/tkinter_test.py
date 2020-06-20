"""Simple test to make sure tkinter and git are working"""

import tkinter as tk

def main():
    window = tk.Tk()
    label = tk.Label(window, text='This is our label.')
    label.grid(row=0, column=0)
    window.mainloop()
    
main()