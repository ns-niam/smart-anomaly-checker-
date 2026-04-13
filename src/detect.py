from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.2, random_state=42)

    df['anomaly'] = model.fit_predict(df[['value']])

    # convert labels: -1 → anomaly, 1 → normal
    df['anomaly_label'] = df['anomaly'].apply(
        lambda x: "Anomaly" if x == -1 else "Normal"
    )

    return df
