#  Hurst Exponent Feature

import pyeeg

def Hurst( x ):

	resp = pyeeg.hurst(x)

	return resp
