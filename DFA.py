# Detrended Fluctuation Analysis

import nolds
import pyeeg

def DFA( x ):

	resp = pyeeg.dfa(x)

	return resp
