import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Anomaly Checker", layout="centered")

st.title("🧠 Smart Anomaly Checker")
st.write("Upload your CSV file to detect anomalies using Machine Learning")

# upload file
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.write(df)

    if 'value' not in df.columns:
        st.error("CSV must contain a 'value' column")
    else:
        # model
        model = IsolationForest(contamination=0.2, random_state=42)
        df['anomaly'] = model.fit_predict(df[['value']])

        df['label'] = df['anomaly'].apply(
            lambda x: "Anomaly" if x == -1 else "Normal"
        )

        st.subheader("🤖 Results")
        st.write(df)

        # anomalies
        anomalies = df[df['anomaly'] == -1]
        st.subheader("🚨 Detected Anomalies")
        st.write(anomalies)

        # plot
        st.subheader("📈 Visualization")

        normal = df[df['anomaly'] == 1]
        anomaly = df[df['anomaly'] == -1]

        fig, ax = plt.subplots()
        ax.scatter(normal.index, normal['value'], label="Normal")
        ax.scatter(anomaly.index, anomaly['value'], label="Anomaly")
        ax.legend()

        st.pyplot(fig)
