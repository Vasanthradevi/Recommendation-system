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
import sklearn
import warnings
warnings.filterwarnings("ignore")

channels = ["AF3", "AF4", "F3", "F4", "F7", "F8", "FC5", "FC6", "O1", "O2", "P7", "P8", "T7", "T8"]
labels = ["G1", "G2", "G3", "G4"]
DFA_Features = "Trained data/DFAfeatures.csv"
Hjorith_mobil_valFeatures = "Trained data/Hjorith_mobil_valfeatures.csv"
Hjorith_complex_valFeatures = "Trained data/Hjorith_complex_valfeatures.csv"
Hurst_valFeatures = "Trained data/Hurst_valfeatures.csv"
mean_valFeatures = "Trained data/mean_valfeatures.csv"
pfd_valFeatures = "Trained data/pfd_valfeatures.csv"
DWT_ApproxFeatures = "Trained data/DWTapproxfeatures.csv"
DWT_detailFeatures = "Trained data/DWTdetailfeatures.csv"
with open(DFA_Features, 'w', newline='') as DFAfile:
    with open(Hjorith_mobil_valFeatures, 'w', newline='') as Hjorith_mob_file:
        with open(Hjorith_complex_valFeatures, 'w', newline='') as Hjorith_com_file:
            with open(Hurst_valFeatures, 'w', newline='') as Hurst_file:
                with open(mean_valFeatures, 'w', newline='') as mean_file:
                    with open(pfd_valFeatures, 'w', newline='') as pfd_flie:
                        with open(DWT_ApproxFeatures, 'w', newline='') as DWTapprox_flie:
                            with open(DWT_detailFeatures, 'w', newline='') as DWTdetail_flie:
                                write_DFA = csv.writer(DFAfile, delimiter=',')
                                write_Hjorith_mob = csv.writer(Hjorith_mob_file, delimiter=',')
                                write_Hjorith_com = csv.writer(Hjorith_com_file, delimiter=',')
                                write_Hurst = csv.writer(Hurst_file, delimiter=',')
                                write_mean = csv.writer(mean_file, delimiter=',')
                                write_pfd = csv.writer(pfd_flie, delimiter=',')
                                write_DWTapprox = csv.writer(DWTapprox_flie, delimiter=',')
                                write_DWTdetail = csv.writer(DWTdetail_flie, delimiter=',')
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
                                        DFA_val = []
                                        Hjorith_mobil_val = []
                                        Hjorith_complex_val = []
                                        Hurst_val = []
                                        mean_val = []
                                        pfd_val = []
                                        DWT_Aprox_val = []
                                        DWT_detail_val = []
                                        for ch in range(len(channels)):
                                            DFA_v = DFA(x[ch])
                                            DFA_val.append(DFA_v)
                                            Hjorith_mobility, Hjorith_Complexity = Hjorth(x[ch])
                                            Hjorith_mobil_val.append(Hjorith_mobility)
                                            Hjorith_complex_val.append(Hjorith_Complexity)
                                            Hurst_v = Hurst(x[ch])
                                            Hurst_val.append(Hurst_v)
                                            mean_v = Mean(x[ch])
                                            mean_val.append(mean_v)
                                            pfd_v = PFD(x[ch])
                                            pfd_val.append(pfd_v)
                                            DWT_Aprox, DWT_detail = DWT(x[ch])
                                            DWT_Aprox_val.append(DWT_Aprox)
                                            DWT_detail_val.append(DWT_detail)
                                        write_DFA.writerow(DFA_val)
                                        write_Hjorith_mob.writerow(Hjorith_mobil_val)
                                        write_Hjorith_com.writerow(Hjorith_complex_val)
                                        write_Hurst.writerow(Hurst_val)
                                        write_mean.writerow(mean_val)
                                        write_pfd.writerow(pfd_val)
                                        write_DWTapprox.writerow(DWT_Aprox_val)
                                        write_DWTdetail.writerow(DWT_detail_val)


                        '''
                       DFA_val = []
                                Hjorith_mobil_val = []
                                Hjorith_complex_val = []
                                Hurst_val = []
                                mean_val = []
                                pfd_val = []
                                DWT_Aprox_val = []
                                DWT_detail_val = []
                        write_DFA = csv.writer(DFAfile, delimiter=',')
            write_Hjorith_mob = csv.writer(Hjorith_mob_file, delimiter=',')
            write_Hjorith_com = csv.writer(Hjorith_com_file, delimiter=',')
            write_Hurst = csv.writer(Hurst_file, delimiter=',')
            write_mean = csv.writer(mean_file, delimiter=',')
            write_pfd = csv.writer(pfd_flie, delimiter=',')
            write_DWTapprox = csv.writer(DWTapprox_flie, delimiter=',')
                        write_DWTdetail = csv.writer(DWTdetail_flie, delimiter=',')
                    write_power.writerow(power_val)
                    write_power.writerow(power_val)
                    write_power.writerow(power_val)
                    write_power.writerow(power_val)
                    write_power.writerow(power_val)
'''
