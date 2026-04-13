from src.preprocess import load_data, clean_data
from src.detect import detect_anomalies
from src.visualize import plot_data


def main():
    file_path = "data/sample.csv"

    # load
    df = load_data(file_path)
    if df is None:
        return

    # clean
    df = clean_data(df)

    # detect
    df = detect_anomalies(df)

    # print result
    print("\n=== RESULT ===")
    print(df)

    # show anomalies
    anomalies = df[df['anomaly'] == -1]
    print("\n=== ANOMALIES ===")
    print(anomalies)

    # visualize
    plot_data(df)


if __name__ == "__main__":
    main()
