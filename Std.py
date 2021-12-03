# Std feature

import numpy as np
import csv
import pandas as pd

def Std( x ):

	resp = np.std(x)

	return resp


channels = ["AF3", "AF4", "F3", "F4", "F7", "F8", "FC5", "FC6", "O1", "O2", "P7", "P8", "T7", "T8"]
labels = ["G1", "G2", "G3", "G4"]
std_valFeatures = "Trained data/std_valfeatures.csv"
with open(std_valFeatures, 'w', newline='') as std_flie:
	write_std = csv.writer(std_flie, delimiter=',')
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
				std_tot_val = []
			for ch in range(len(channels)):
				std_val = Std(x[ch])
				std_tot_val.append(std_val)
			write_std.writerow(std_tot_val)
