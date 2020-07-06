"""
Test suite for MCvisualiser.
Using pytest for unit testing.

:$ pytest tests.py to run tests if in src directory
"""

import pytest
import numpy as np
from markov import *

class TestSuiteMarkovChain():
    """
    Tests for class MarkovChain
    - be sure to activate test mode when creating the MarkovChain object
    """
    
    def test_check_input_one(self): 
        
        identity = np.identity(3)
        identity_MC = MarkovChain(identity, test_mode=True)
        assert identity_MC._is_valid_input() == True
        
    def test_check_input_two(self): 
        
        # Doesn't sum to one
        
        ones = np.ones((3,3))
        ones_MC = MarkovChain(ones, test_mode=True)
        assert ones_MC._is_valid_input() == False
        
    def test_check_input_three(self):
        
        # Doesn't sum to one
        
        trans = np.full((3,3), 0.5)
        trans_MC = MarkovChain(trans, test_mode=True)
        assert trans_MC._is_valid_input() == False
        
    def test_check_input_four(self):
        
        trans = np.array([[0.4, 0.3, 0.3],
                         [0.6, 0.2, 0.2],
                         [0.5, 0.5, 0]])
        trans_MC = MarkovChain(trans, test_mode=True)
        assert trans_MC._is_valid_input() == True
        
    def test_check_input_five(self):
        
        # Boundary Case, value larger than one
        
        trans = np.array([[0.9, 0.0, 0.11],
                         [0.6, 0.2, 0.2],
                         [0.5, 0.5, 0]])
        trans_MC = MarkovChain(trans, test_mode=True)
        assert trans_MC._is_valid_input() == False    
        
    def test_check_input_six(self):
        
        # Negative value
        
        trans = np.array([[0.9, 0.0, 0.1],
                         [0.6, -0.2, 0.4],
                         [0.5, 0.5, 0]])
        trans_MC = MarkovChain(trans, test_mode=True)
        assert trans_MC._is_valid_input() == False
        