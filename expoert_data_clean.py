def correct(exp):
    dat = exp.dropna()
    dat.to_csv('dat_cleaned.csv',index = False)