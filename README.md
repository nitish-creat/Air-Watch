# AirWatch: Real-Time Air Quality Analysis & AQI Prediction

## 1. Overview

AirWatch is an end-to-end data science project that analyzes air pollution and weather data across major Indian cities and predicts Air Quality Index (AQI) using machine learning techniques.

The project integrates real-time API data with historical datasets to provide insights into pollution patterns and environmental impact.

---

## 2. Objectives

* Analyze air quality trends across cities
* Identify key factors affecting AQI
* Perform statistical validation of data
* Predict AQI using weather parameters
* Build an interactive dashboard for visualization

---

## 3. Features

* Real-time data collection using APIs
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Statistical testing (t-test, Shapiro, VIF)
* AQI prediction using Linear Regression
* Interactive Streamlit dashboard (with fallback system)

---

## 4. Project Structure

```bash
airwatch-aqi-prediction/
│
├── data/
├── notebooks/
├── scripts/
├── database/
├── models/
├── app/
```

---

## 5. Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* SQLite
* Streamlit

---

## 6. Results

* Identified strong correlation between PM2.5 and AQI
* Observed seasonal pollution patterns
* Built a predictive model with measurable accuracy

---

## 7. How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit app:

   ```bash
   streamlit run app/app.py
   ```

---

## 8. Future Improvements

* Add classification models
* Improve prediction accuracy
* Deploy online dashboard

