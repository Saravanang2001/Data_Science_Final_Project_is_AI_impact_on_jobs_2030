def Descrip(statitists):
    numeric_cols = statitists.select_dtypes(include='number').columns
    for datas in numeric_cols:
       print(f"\nStatistics for '{datas}':")
       mean = statitists[datas].mean()
       median = statitists[datas].median()
       mode = statitists[datas].mode()[0]
       std = statitists[datas].std()
       print(f"Mean: {mean}")
       print(f"Median: {median}")
       print(f"Mode: {mode}")
       print(f"Standard Deviation: {std}")
       print("*"*40)
