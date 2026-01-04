import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def KMeans_clustering(data):
    # Convert input data to DataFrame
    df = pd.DataFrame(data)

    # Select numeric columns from CSV for clustering
    X = df[
        [
            'Average_Salary',
            'Years_Experience',
            'AI_Exposure_Index'
        ]
    ]

    # Standardize the data
    scaler = StandardScaler()
    scaled = scaler.fit_transform(X)

    # Apply k-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=98)
    df['Cluster'] = kmeans.fit_predict(scaled)

    # ------------------- Scatter Plot -------------------
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df['Years_Experience'],
        df['Average_Salary'],
        c=df['Cluster'],
        cmap='viridis',
        s=100
    )

    plt.xlabel("Years of Experience")
    plt.ylabel("Average Salary")
    plt.title("k-Means Clustering of Jobs (Scatter Plot)")
    plt.colorbar(label="Cluster")
    plt.tight_layout()
    plt.show()
    # ----------------------------------------------------

    # Display Cluster-wise Data
    print("Cluster 1 Data (Low level jobs):")
    print(df[df['Cluster'] == 0])

    print("\nCluster 2 Data (Mid level jobs):")
    print(df[df['Cluster'] == 1])

    print("\nCluster 3 Data (High level jobs):")
    print(df[df['Cluster'] == 2])

    print("\nComplete Data with Cluster Labels:")
    print(df)

    return df
