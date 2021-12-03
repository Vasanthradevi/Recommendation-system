from BandPower import BandPower
from SpectralEntropy import SpectralEntropy
from Mean import Mean
from Power import Power
from Std import Std
from Hjorth import Hjorth
from CorrelationDimension import CorrelationDimension
from Hurst import Hurst
from DFA import DFA
from FirstDiff import FirstDiff
from PFD import PFD
from DWT import DWT
import csv
import numpy as np
import pandas as pd

channels = ["AF3","AF4","F3","F4","F7","F8","FC5","FC6","O1","O2","P7","P8","T7","T8"]
labels = ["G1", "G2", "G3", "G4"]
Mean_ch = []
std_ch = []
powerval = []
MSCE_ch = []
Spectral_powerFeatures = "Trained data/spectralpowerfeatures.csv"
Spectral_ratioFeatures = "Trained data/spectralratiofeatures.csv"
Spectral_entropyFeatures = "Trained data/spectralentropyfeatures.csv"
with open(Spectral_powerFeatures, 'w', newline='') as power:
    with open(Spectral_ratioFeatures, 'w', newline='') as ratio:
        with open(Spectral_entropyFeatures, 'w', newline='') as entropy:
                write_power = csv.writer(power, delimiter=',')
                write_ratio = csv.writer(ratio, delimiter=',')
                write_entropy = csv.writer(entropy, delimiter=',')
                for j in range(28):  # 20 users for training and 8 users for testing
                    if j % 1 == 0:
                        if j < 10:
                            name = '%0*d' % (2, j + 1)
                        else:
                            name = j + 1

                    for i in labels:
                        fname = "data/s" + str(name) + "/S" + str(
                            name) + i + "Allchannels.csv"  # data/s01/S01G1AllChannels.csv
                        print('fname:', fname)
                        x = pd.read_csv(fname, low_memory=False,
                                        usecols=lambda c: not c.startswith('Unnamed:'))
                        colm = []
                        for col in x.columns:  # column 0 - 13  (14 channel)
                            colm.append(col)
                        for cl in range(len(colm)):
                            x = x.rename(columns={colm[cl]: cl})
                        power_val = []
                        ratio_val = []
                        Entropyval = []
                        for ch in range(len(channels)):
                            power, ratio = BandPower(x[ch])
                            power_val.append(Mean(power))
                            ratio_val.append(Mean(ratio))
                            entropy = SpectralEntropy(x[ch])
                            Entropyval.append(Mean(entropy))
                        write_power.writerow(power_val)
                        write_ratio.writerow(ratio_val)
                        write_entropy.writerow(Entropyval)






