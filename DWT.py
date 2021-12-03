# Discret Wavelet Transform

import pywt
import pandas as pd
import csv
from Mean import Mean

def DWT( x ):

	resp = pywt.dwt(x, 'db4')

	return resp

channels = ["AF3", "AF4", "F3", "F4", "F7", "F8", "FC5", "FC6", "O1", "O2", "P7", "P8", "T7", "T8"]
labels = ["G1", "G2", "G3", "G4"]
DWT_ApproxFeatures = "Trained data/DWTapproxfeatures.csv"
DWT_detailFeatures = "Trained data/DWTdetailfeatures.csv"
with open(DWT_ApproxFeatures, 'w', newline='') as DWTapprox_flie:
	with open(DWT_detailFeatures, 'w', newline='') as DWTdetail_flie:
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
				DWT_Aprox_val = []
				DWT_detail_val = []
				for ch in range(len(channels)):
					DWT_Aprox, DWT_detail = DWT(x[ch])
					DWT_Aprox_val.append(Mean(DWT_Aprox))
					DWT_detail_val.append(Mean(DWT_detail))
				write_DWTapprox.writerow(DWT_Aprox_val)
				write_DWTdetail.writerow(DWT_detail_val)