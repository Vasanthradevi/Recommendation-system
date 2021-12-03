import pandas as pd
from scipy.stats import pearsonr

channel_name = ["AF3", "AF4", "F3", "F4", "F7", "F8", "FC5", "FC6", "O1", "O2", "P7", "P8", "T7", "T8"]
corr_df = pd.read_csv('Trained_val.csv', low_memory=False,
                usecols=lambda c: not c.startswith('Unnamed:'))
corr_df_ar = pd.DataFrame(columns=['channels', 'Delta', 'Theta', 'Alpha', 'Beta', 'Gamma'])
corr_df_ar['channels'] = [i for i in channel_name]

for n in range(len(channel_name)):
    Del_ch = []
    the_ch = []
    alp_ch = []
    beta_ch = []
    gam_ch = []
    ar_val = []
    f_in = n
    while f_in <= 55:
        Del_ch.append(corr_df.at[f_in, 'delta_m'])
        the_ch.append(corr_df.at[f_in, 'theta_m'])
        alp_ch.append(corr_df.at[f_in, 'alpha_m'])
        beta_ch.append(corr_df.at[f_in, 'beta_m'])
        gam_ch.append(corr_df.at[f_in, 'gamma_m'])
        ar_val.append(corr_df.at[f_in, 'arousal'])
        f_in += f_in

    corr_df_ar.at[n, 'Delta'] = pearsonr(Del_ch, ar_val)
    corr_df_ar.at[n, 'Theta'] = pearsonr(the_ch, ar_val)
    corr_df_ar.at[n, 'Alpha'] = pearsonr(alp_ch, ar_val)
    corr_df_ar.at[n, 'Beta'] = pearsonr(beta_ch, ar_val)
    corr_df_ar.at[n, 'Gamma'] = pearsonr(gam_ch, ar_val)

    corr_df_ar.to_csv("Arousal correlation.csv")
