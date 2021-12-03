import numpy as np
import pandas as pd
import dataframe_image as dfi
import matplotlib.pyplot as plt
import csv
from itertools import zip_longest
from scipy.stats import pearsonr
import math
from scipy import signal
import seaborn as sns
from scipy.integrate import simps
from scipy.signal import welch
from mne.time_frequency import psd_array_multitaper
import nolds
import pyeeg
from scipy.signal import coherence
import pywt
from DA import DA
from MSCE import MSCE

channels = ["AF3","AF4","F3","F4","F7","F8","FC5","FC6","O1","O2","P7","P8","T7","T8"]
labels = ["G1", "G2", "G3", "G4"]
Mean_ch = []
std_ch = []
powerval = []
MSCE_ch = []
DA_meanFeatures = "Trained data/DA_meanfeatures.csv"
DA_stdFeatures = "Trained data/DA_stdfeatures.csv"
DA_powerFeatures = "Trained data/DA_powerfeatures.csv"
MSCE_features = "Trained data/MSCE_features.csv"
with open(DA_meanFeatures, 'w', newline='') as file_mean:
    with open(DA_stdFeatures, 'w', newline='') as file_std:
        with open(DA_powerFeatures, 'w', newline='') as file_power:
            with open(MSCE_features, 'w', newline='') as file_MSCE:
                write_mean = csv.writer(file_mean, delimiter=',')
                write_std = csv.writer(file_std, delimiter=',')
                write_power = csv.writer(file_power, delimiter=',')
                write_MSCE = csv.writer(file_MSCE, delimiter=',')
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
                        chan = [0, 2, 4, 6, 8, 10, 12]
                        mean_val = []
                        std_val = []
                        powerval = []
                        MSCE_val = []
                        for ch in chan:
                            mean, std, power = DA(x[ch], x[ch+1])
                            mean_val.append(mean)
                            std_val.append(std)
                            for p in power:
                                powerval.append(p)
                            MSCE_freq, MSCE_fe = MSCE(x[ch], x[ch+1])  # MSCE function return sample frequencies and MSCE
                            for v in MSCE_fe:
                                MSCE_val.append(v)
                        write_MSCE.writerow(MSCE_val)
                        write_mean.writerow(mean_val)
                        write_std.writerow(std_val)
                        write_power.writerow(powerval)












