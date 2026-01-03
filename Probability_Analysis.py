import matplotlib.pyplot as plt
def range(datasets):
    """
    Calculates Range and Variance for numeric features
    """
    numeric_cols = datasets.select_dtypes(include='number').columns
    
    for col in numeric_cols:
        rng = datasets[col].max() - datasets[col].min()
        var = datasets[col].var()
        
        print(f"\nStatistics for '{col}':")
        print(f"Range        : {rng}")
        print(f"Variance     : {var}")
def hist_rang(datasets):
    """
    Visualizes probability distributions for numeric features
    using histograms
    """
    numeric_cols = datasets.select_dtypes(include='number').columns

    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        plt.hist(datasets[col], bins=10, density=True, edgecolor='black')
        plt.title(f"Probability Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Probability Density")
        plt.grid(True)
        plt.show()
