"""
Markov Chain Visualiser

Author: Liam Pol
Created: 20/06/20
"""

from tkinter import *
from tkinter import ttk

class Gui():
    """
    The GUI for Markov Chain Visualiser.
    
        - self.markov_frame is the frame that will contain
        the Markov Chain (MODEL)
        
        - self.algo_frame is the frame that will contain
        the algorithm selection (VIEW)
        
        - self.desc_frame is the frame that will contain
        the description for the selected algorithm (VIEW)
        
    TODO: Document further once done.
    """
    
    def __init__(self, root):
        self._root = root
        self.algo_frame = ttk.Frame(self._root)
        self.markov_frame = ttk.Frame(self._root)
        self.desc_frame = ttk.Frame(self._root)
        
        self._set_master_args()
        self._init_frames()
        
    def _set_master_args(self):
        """Sets the top level (master/root) window arguments to the 
        constant values:
            Dimensions: 800 x 600 pixels
            Resizable: False
        """
        self._root.geometry("800x600")
        # Not resizable in x or y
        self._root.resizable(FALSE, FALSE)
        
    def _init_frames(self):
        """
        Adds the new frames to the master window.
        """
        self.algo_frame.grid(row=0, column=0)
        self.markov_frame.grid(row=0, column=1)
        self.desc_frame.grid(row=1, column=0, columnspan=2)
        
        
    

def main():
    """Entry point into the program"""
    root = Tk()
    gui = Gui(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
