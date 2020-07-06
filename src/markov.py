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
    and numpy for adjacency/transition matrices.
    
    When initialising a Markov Chain, they have all probabilities
    rounded to 2dp
    
        - trans_matrix is a numpy n x n ndarray, where n > 1
        
        - test_mode is a condition that stops the Markov Chain from
          running the constructor
        
    TODO: Fully implement
    """
    def __init__(self, trans_matrix, test_mode=False):
        """
        Markov Chain constructor
        """
        
        if test_mode:
            
            self.trans_matrix = trans_matrix
            
        else:
            
            if self._is_valid_input():
                np.round(self.trans_matrix)
            else:
                raise ValueError("Not a valid transition matrix")
        
    def _is_valid_input(self):
        """
        Checks whether the input is a valid transition matrix. That is,
        1. All probabilities are >= 0 and <= 1
        2. The matrix is SQUARE (n x n)
        3. The sum of each row in the transition matrix equals 1
        """
        return self.trans_matrix.shape[0] == self.trans_matrix.shape[1] \
            and (self.trans_matrix >= 0).all() \
            and (self.trans_matrix <= 1).all() \
            and (np.round(self.trans_matrix.sum(axis=1), 2) <= 1).all()
        
        
    