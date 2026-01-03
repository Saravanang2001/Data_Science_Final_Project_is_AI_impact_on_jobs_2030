import seaborn as sns
import matplotlib.pyplot as plt

# Select only numeric columns
NUM_COLS = [
    'Average_Salary',
    'Years_Experience',
    'AI_Exposure_Index',
    'Tech_Growth_Factor',
    'Automation_Probability_2030'
]


# PAIR PLOT
def Pair_plot(df):
    sns.pairplot(
        df[NUM_COLS],
        diag_kind='kde'
    )
    plt.suptitle("Pair Plot of Numeric Features", y=1.02)
    plt.show()


# CORRELATION HEATMAP
def Heat_plot(df):
    corr = df[NUM_COLS].corr()

    plt.figure(figsize=(20, 16))
    sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")
    plt.show()


# COVARIANCE HEATMAP
def Heat_cov(df):
    cov = df[NUM_COLS].cov()

    plt.figure(figsize=(20, 16))
    sns.heatmap(
        cov,
        annot=True,
        cmap='viridis',
        linewidths=0.5
    )

    plt.title("Covariance Heatmap")
    plt.show()


# 4️⃣ VIOLIN PLOT
def Violin_plot(df):
    plt.figure(figsize=(20, 16))

    sns.violinplot(
        x='Risk_Category',
        y='Average_Salary',
        data=df
    )

    plt.title("Violin Plot: Salary Distribution by Risk Category")
    plt.xlabel("Risk Category")
    plt.ylabel("Average Salary")
    plt.show()
