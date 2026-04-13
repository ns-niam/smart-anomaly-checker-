# 🧠 Smart Anomaly Checker

> Detect abnormal patterns in data using Machine Learning (Isolation Forest)

---

## 🚀 Overview

Smart Anomaly Checker is a machine learning-based web application that detects unusual or abnormal values in datasets.
It helps identify outliers, anomalies, or suspicious data points in real-time.

This project demonstrates practical applications of anomaly detection in real-world scenarios like fraud detection, system monitoring, and data validation.

---

## ✨ Features

* 📂 Upload CSV dataset
* 🤖 Detect anomalies using Isolation Forest
* 📊 Visualize normal vs anomalous data
* 🚨 Highlight suspicious values
* 🌐 Interactive web app using Streamlit

---

## 🧠 How It Works

1. Upload a dataset (CSV file)
2. Data is cleaned and processed
3. Isolation Forest model is applied
4. Each data point is classified as:

   * ✅ Normal
   * 🚨 Anomaly
5. Results are visualized for better understanding

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

## 📁 Project Structure

```
smart-anomaly-checker/
│
├── data/               # Sample datasets
├── src/                # Core ML logic
│   ├── preprocess.py
│   ├── detect.py
│   └── visualize.py
│
├── app.py              # Streamlit web app
├── main.py             # CLI version
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run (Local)

### 1️⃣ Clone the repository

```
git clone https://github.com/ns-niam/smart-anomaly-checker.git
cd smart-anomaly-checker
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the web app

```
streamlit run app.py
```

---

## 📊 Example Input

```
value
10
12
11
100
9
150
```

---

## 📈 Output

* Data labeled as Normal or Anomaly
* Visual graph showing anomalies clearly

---

## 💡 Use Cases

* 💳 Fraud Detection (bank transactions)
* 📊 Data Quality Checking
* ⚙️ System Monitoring
* 🧪 Experimental Data Analysis

---

## 🔮 Future Improvements

* Upload multi-column datasets
* Real-time anomaly detection
* Model selection options
* Cloud deployment (live demo)
* Download results as CSV

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📫 Contact

* GitHub: https://github.com/ns-niam
* LinkedIn: https://lnkd.in/eu4ztb_j

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

## 🧑‍💻 Author

**Md Sha Niamatullah**
AI Engineer | Software Engineer | ML Enthusiast

---
