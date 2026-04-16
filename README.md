# AirWatch: Air Quality Analysis & AQI Prediction

## 1. Overview

AirWatch is an end-to-end data science project that analyzes air pollution data across major Indian cities and predicts Air Quality Index (AQI) using machine learning techniques.

The project provides comprehensive insights into pollution patterns, statistical validation, and predictive modeling.

---

## 2. Objectives

- Analyze air quality trends across cities
- Identify key factors affecting AQI
- Perform statistical validation of data
- Predict AQI using machine learning
- Build robust predictive models

---

## 3. Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical testing (t-test, Shapiro, VIF)
- AQI prediction using Machine Learning
- Classification and Regression models
- Comprehensive data visualization

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

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- SQLite
- Jupyter Notebooks

---

## 6. Results

- Identified strong correlation between PM2.5 and AQI
- Observed seasonal pollution patterns
- Built a predictive model with measurable accuracy

---

## 7. Workflow

**Notebook 1: Data Cleaning & Preparation**

- Load and clean historical dataset
- Handle missing values and duplicates
- Extract temporal features

**Notebook 2: Exploratory Data Analysis (EDA)**

- Analyze data distributions
- Visualize AQI patterns
- Identify correlations

**Notebook 3: Statistical Validation**

- Perform hypothesis testing
- Test for normality and multicollinearity
- Validate data quality

**Notebook 4: Machine Learning Models**

- Train classification models
- Train regression models
- Evaluate model performance

## 8. How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run notebooks in order:

   ```bash
   jupyter notebook NoteBooks/1_dataClean.ipynb
   jupyter notebook NoteBooks/2_EDA.ipynb
   jupyter notebook NoteBooks/3_Statistical_valid.ipynb
   jupyter notebook NoteBooks/4_ML.ipynb
   ```

---

## 9. Future Improvements

- Integrate real-time API data for live predictions
- Build interactive dashboard for monitoring
- Develop advanced ensemble models
- Deploy prediction service
