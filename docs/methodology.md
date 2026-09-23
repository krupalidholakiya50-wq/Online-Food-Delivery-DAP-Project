# 📋 Academic DAP Project Methodology & 15-Step Architecture

**Project Title:** Online Food Delivery Demand Forecasting & Peak Hour Regression Model  
**Subject:** 602 – Data Analytics Using Python (DAP)  
**Domain:** Food, E-Commerce & Consumer Analytics  
**Group:** 6  

---

## 🎯 Architectural Overview
This project strictly implements the 15-step academic Data Analytics using Python (DAP) methodology as defined in the curriculum reference (`stepbystep.md` and `marking-structure-scheme.md`).

```
+-----------------------------------------------------------------------------------+
|                            THE 15-STEP DAP PIPELINE                               |
+-----------------------------------------------------------------------------------+
|  Step 1: Python Libraries Setup (pandas, numpy, matplotlib, seaborn, sklearn)    |
|  Step 2: Loading Real Food Delivery Dataset (pd.read_csv, head, tail, shape)      |
|  Step 3: Understanding Data Structure (info, dtypes, numerical vs categorical)    |
|  Step 4: Data Spread & Preparation (string strip, time parsing, Haversine dist)   |
|  Step 5: Missing Data & Outliers Detection (isnull.sum, boxplot analysis)         |
|  Step 6: Systematic Imputation (df.fillna(df.mean(numeric_only=True)))            |
|  Step 7: Univariate EDA (Delivery times, Hourly volume, Peak vs Non-Peak)         |
|  Step 8: Bivariate EDA (Distance vs Time, Traffic vs Duration boxplots)           |
|  Step 9: Multivariate EDA (Pivot Heatmap, Correlation Matrix)                     |
|  Step 10: Regression Analysis (Train-Test Split 80/20, LinearRegression fit)      |
|  Step 11: Regression Evaluation (MSE, MAE, R², 45° Scatter Plot)                  |
|  Step 12: Classification Model (LogisticRegression for Peak vs Non-Peak Hour)     |
|  Step 13: Classification Evaluation (Accuracy, Confusion Matrix, Recall)          |
|  Step 14: Underfitting & Overfitting Diagnostics (Train vs Test Metrics)          |
|  Step 15: Conclusions, Limitations & Actionable Business Recommendations          |
+-----------------------------------------------------------------------------------+
```

---

## 🔬 Detailed Step Breakdown

### Step 1: Importing Necessary Python Libraries
- **Data Wrangling:** `pandas`, `numpy`
- **Visualization:** `matplotlib.pyplot`, `seaborn`
- **Machine Learning & Modeling:** `sklearn.model_selection` (`train_test_split`), `sklearn.linear_model` (`LinearRegression`, `LogisticRegression`), `sklearn.metrics` (`mean_squared_error`, `mean_absolute_error`, `r2_score`, `accuracy_score`, `confusion_matrix`)

### Step 2: Loading Data & DataFrame Creation
- Loading the raw benchmark dataset containing 45,593 records across 20 attributes from `data/raw/food_delivery_raw.csv`.
- Inspecting dimensions with `.shape`, top records with `.head()`, and bottom records with `.tail()`.

### Step 3: Understanding the Data
- Identifying data types (`int64`, `float64`, `object`).
- Distinguishing continuous operational metrics (coordinates, ratings, ages) from discrete categorical labels (weather conditions, traffic levels, vehicle types, city types).
- Reviewing five-number descriptive statistics summary via `.describe()`.

### Step 4: Data Spread & Preparation
- **String Cleaning:** Stripping leading/trailing whitespaces and handling format artifacts (e.g. converting `"(min) 24"` to float `24.0`).
- **Geospatial Distance Calculation:** Applying the Haversine spherical trigonometric formula on restaurant and delivery latitude/longitude pairs to compute accurate delivery distance in kilometers.
- **Temporal Parsing:** Converting `Order_Date` to datetime and extracting `order_hour`, `day_of_week`, and `is_weekend`.

### Step 5: Checking Missing Data & Outliers
- Auditing missing values via `df.isnull().sum()`.
- Performing IQR and boxplot inspections on numerical fields. Extreme delivery times (e.g. > 45 minutes) are analyzed and confirmed as valid operational events caused by severe traffic or bad weather.

### Step 6: Handling Missing Data & Outliers
- Applying standard academic mean imputation for numerical attributes: `df.fillna(df.mean(numeric_only=True))`.
- Applying mode imputation for categorical columns (`Weatherconditions`, `Road_traffic_density`, `City`).
- Defining the empirical peak-hour target: `is_peak_hour = 1` for hours `[12, 13, 14, 18, 19, 20, 21, 22, 23]`.

### Step 7: Univariate EDA
- Analyzing single-variable frequency distributions:
  1. Delivery Time histogram and kernel density estimation.
  2. Hourly order volume count distribution.
  3. Peak hour vs Non-Peak hour volume proportions.
  4. Order volume by Day of Week.
- Adding an explicit written conclusion under every graph.

### Step 8: Bivariate EDA
- Investigating pairwise relationships:
  1. Distance (km) vs Delivery Duration (min) with linear trendline.
  2. Road Traffic Density levels vs Delivery Time distribution spread via boxplots.
- Writing comparative interpretations for operational insights.

### Step 9: Multivariate EDA
- Constructing two-way pivot tables (`Type_of_order` vs `Road_traffic_density` on mean delivery duration).
- Generating full numerical feature correlation heatmap matrix (`sns.heatmap(annot=True)`).

### Step 10: Regression Analysis (Supervised Learning)
- **Target Variable ($y$):** Continuous delivery time in minutes (`delivery_time_min`).
- **Predictor Features ($X$):** `distance_km`, `order_hour`, `Delivery_person_Age`, `Delivery_person_Ratings`, `Vehicle_condition`, `multiple_deliveries`, `is_weekend`, `is_peak_hour`, one-hot encoded traffic density and weather indicators.
- **Data Partitioning:** 80% Training ($N=36,474$), 20% Testing ($N=9,119$) with `random_state=42`.
- **Model:** `LinearRegression().fit(X_train, y_train)`.

### Step 11: Regression Model Evaluation
- Computing standard metrics:
  - **MSE (Mean Squared Error)**
  - **MAE (Mean Absolute Error)**
  - **$R^2$ Score (Coefficient of Determination)**
- Generating the mandatory **Actual vs. Predicted Scatter Plot** with the 45-degree reference diagonal line ($y=x$).
- Plotting residual error distribution.
- Serializing model to `outputs/models/linear_regression_demand.joblib`.

### Step 12: Classification Model (Peak Hour Prediction)
- **Target Variable ($y$):** Binary peak hour indicator (`is_peak_hour` $\in \{0, 1\}$).
- **Predictor Features ($X$):** Delivery metrics, distance, courier features, vehicle condition, and traffic/weather dummies.
- **Data Partitioning:** Stratified 80/20 train-test split (`random_state=42`).
- **Model:** `LogisticRegression(max_iter=1000).fit(X_train, y_train)`.

### Step 13: Classification Model Evaluation
- Computing classification accuracy score via `accuracy_score()`.
- Generating classification confusion matrix via `confusion_matrix()`.
- Plotting and saving confusion matrix heatmap to `outputs/figures/11_classification_confusion_matrix.png`.
- Serializing model to `outputs/models/logistic_regression_peak_hour.joblib`.

### Step 14: Underfitting & Overfitting Diagnostics
- Comparing training vs testing performance across both regression ($R^2_{\text{train}}$ vs $R^2_{\text{test}}$) and classification ($\text{Acc}_{\text{train}}$ vs $\text{Acc}_{\text{test}}$).
- Confirming that the minimal generalization gap indicates optimal bias-variance tradeoff without overfitting.

### Step 15: Conclusions & Actionable Insights
- Synthesizing core empirical findings, model limitations, fleet dispatch recommendations, dynamic surge buffers, and future scope.
