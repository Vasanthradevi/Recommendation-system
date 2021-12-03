import pandas as pd

__all__ = ["BandPower", "HOS", "SpectralEntropy"]

from BandPower import BandPower
from SpectralEntropy import SpectralEntropy

fname = "data/s01/S01G1AllChannels.csv"
x = pd.read_csv(fname, low_memory=False,
                usecols=lambda c: not c.startswith('Unnamed:'))
colm = []
for col in x.columns:  # column 0 - 13  (14 channel)
    colm.append(col)
for cl in range(len(colm)):
    x = x.rename(columns={colm[cl]: cl})

bp, bandratio = BandPower(x[0])
print(bp)
