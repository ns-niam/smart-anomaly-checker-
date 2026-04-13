import matplotlib.pyplot as plt

def plot_data(df):
    normal = df[df['anomaly'] == 1]
    anomaly = df[df['anomaly'] == -1]

    plt.figure()

    plt.scatter(normal.index, normal['value'], label="Normal")
    plt.scatter(anomaly.index, anomaly['value'], label="Anomaly")

    plt.title("Anomaly Detection Result")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()

    plt.show()
