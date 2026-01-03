def salary_outliers(df):
    """Detect outliers in Average Salary using IQR method."""
    qt1 = df['Average_Salary'].quantile(0.25)
    qt3 = df['Average_Salary'].quantile(0.75)
    iqr = qt3 - qt1
    print(f"\nSalary IQR (Interquartile Range): {iqr}")
    
    Lower_Bound = qt1 - 1.5 * iqr  # Any value below this is considered a low salary outlier
    Upper_Bound = qt3 + 1.5 * iqr  # Any value above this is considered a high salary outlier
    
    outliers = df[(df['Average_Salary'] < Lower_Bound) | (df['Average_Salary'] > Upper_Bound)]
    print("\nSalary Outliers:")
    print(outliers)


def experience_outliers(df):
    """Detect outliers in Years of Experience using IQR method."""
    qt1 = df['Years_Experience'].quantile(0.25)
    qt3 = df['Years_Experience'].quantile(0.75)
    iqr = qt3 - qt1
    print(f"\nExperience IQR (Interquartile Range): {iqr}")
    
    Lower_Bound = qt1 - 1.5 * iqr  # Any value below this is considered a low experience outlier
    Upper_Bound = qt3 + 1.5 * iqr  # Any value above this is considered a high experience outlier
    
    outliers = df[(df['Years_Experience'] < Lower_Bound) | (df['Years_Experience'] > Upper_Bound)]
    print("\nExperience Outliers:")
    print(outliers)


def ai_exposure_outliers(df):
    """Detect outliers in AI Exposure Index using IQR method."""
    qt1 = df['AI_Exposure_Index'].quantile(0.25)
    qt3 = df['AI_Exposure_Index'].quantile(0.75)
    iqr = qt3 - qt1
    print(f"\nAI Exposure IQR (Interquartile Range): {iqr}")
    
    Lower_Bound = qt1 - 1.5 * iqr  # Any value below this is considered a low AI exposure outlier
    Upper_Bound = qt3 + 1.5 * iqr  # Any value above this is considered a high AI exposure outlier
    
    outliers = df[(df['AI_Exposure_Index'] < Lower_Bound) | (df['AI_Exposure_Index'] > Upper_Bound)]
    print("\nAI Exposure Outliers:")
    print(outliers)
