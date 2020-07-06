"""Simple test to make sure tkinter and git are working"""

from tkinter import *
from tkinter import ttk

def main():
    master = Tk()
    set_master_settings(master)
    label = Label(master, text='This is our label.')
    label.grid(row=0, column=0)
    master.mainloop()
    
def set_master_settings(master_window):
    """Sets the arguments of the master window to the final settings"""
    master_window.geometry("800x600")
    master_window.maxsize(800, 600)
    #master_window.resizable(False)    
    
main()