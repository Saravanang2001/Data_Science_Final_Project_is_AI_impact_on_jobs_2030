import pandas as pd
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
    kmeans.fit(scaled)

    # Assign cluster labels
    df['Cluster'] = kmeans.labels_

    # Display Cluster 1
    cluster1 = df[df['Cluster'] == 0]
    print("Cluster 1 Data (Low level jobs):")
    print(cluster1)

    # Display Cluster 2
    cluster2 = df[df['Cluster'] == 1]
    print("\nCluster 2 Data (Mid level jobs):")
    print(cluster2)

    # Display Cluster 3
    cluster3 = df[df['Cluster'] == 2]
    print("\nCluster 3 Data (High level jobs):")
    print(cluster3)

    # Display complete dataset
    print("\nComplete Data with Cluster Labels:")
    print(df)

    return df
