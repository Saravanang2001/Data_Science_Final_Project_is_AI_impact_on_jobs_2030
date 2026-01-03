def knn_modeling(df):
    # DO NOT read CSV again
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from sklearn.metrics import accuracy_score, classification_report

    label_encoder = LabelEncoder()
    df['Risk_Category'] = label_encoder.fit_transform(df['Risk_Category'])

    X = df[
        [
            'Average_Salary',
            'Years_Experience',
            'AI_Exposure_Index',
            'Tech_Growth_Factor',
            'Automation_Probability_2030'
        ]
    ]

    y = df['Risk_Category']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
