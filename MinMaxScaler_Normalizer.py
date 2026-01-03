from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer

def Standard_Scaler(df):
    scaler = StandardScaler()
    numeric = df.select_dtypes(include='number')
    df[numeric.columns] = scaler.fit_transform(numeric)
    print("\nStandard Scaler Applied Successfully")
    print(df[numeric.columns].head())


def MinMax_Values(df):
    scaler = MinMaxScaler()
    numeric = df.select_dtypes(include='number')
    df[numeric.columns] = scaler.fit_transform(numeric)
    print("\nMinMax Scaler Applied Successfully")
    print(df[numeric.columns].head())


def Normalizer_values(df):
    scaler = Normalizer()
    numeric = df.select_dtypes(include='number')
    df[numeric.columns] = scaler.fit_transform(numeric)
    print("\nNormalizer Applied Successfully")
    print(df[numeric.columns].head())
