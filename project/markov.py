"""
Markov Chain - MODEL
Using python package networkx to represent
Markov Chains.
"""

import networkx as nx
import numpy as np

class MarkovChain():
    """
    A class for a Markov Chain Model, made using networkx graphs
    and numpy for adjacency/transition matrices
    
        - input_data is restricted to a numpy n x n ndarray, where n > 1
        
    TODO: Fully implement
    """
    def __init__(input_data):
        
        self._check_input()
        
    def _check_input():
        """
        - Checks whether input is in the form of a N x N (square) 
          matrix/numpy array
        
        """
        pass
        