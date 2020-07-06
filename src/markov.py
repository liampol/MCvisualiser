"""
Markov Chain - MODEL
Using python package networkx to represent
Markov Chains.
"""

import matplotlib.pyplot as plt
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
        
        Performs a check to make sure the transition matrix is valid. Then 
        constructs a transition diagram from the transition matrix.
        """
        self.trans_matrix = trans_matrix
        
        if test_mode:
            
            pass
            
        else:
            
            if self._is_valid_input():
                
                np.round(self.trans_matrix)
                
                # Add networkx graphing
                
                self.trans_diagram = nx.from_numpy_array(self.trans_matrix, 
                                                parallel_edges=False, 
                                                create_using=nx.MultiDiGraph)
                
                print(f"The graph is: {self.trans_diagram.graph}")
                
                print(f"The nodes in the graph are: {self.trans_diagram.nodes}")
                
                print(f"The edges in the graph are: {self.trans_diagram.edges}")
                
                nx.draw(self.trans_diagram, with_labels=True, arrows = True, 
                        connectionstyle='arc3, rad = 0.1')
                
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
    
    def _create_graph_from_adj_matrix(self):
        """
        This function will need to take a transition matrix/adjacency matrix
        and and construct a transition diagram from it.
        """
    
# Not automated testing, trialing network x graphs.

# Trial 1:

input_data = np.array([[0.0, 0.5, 0.5],
                       [0.5, 0.0, 0.5],
                       [0.5, 0.5, 0.0]])

trial_MC = MarkovChain(input_data)



        
        
    