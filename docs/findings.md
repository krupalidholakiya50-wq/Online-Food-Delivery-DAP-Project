# 📊 Empirical Analytical Findings & Model Evaluation Report

**Project Title:** Online Food Delivery Demand Forecasting & Peak Hour Regression Model  
**Subject:** 602 – Data Analytics Using Python (DAP)  
**Group:** 6  

---

## 1. Dataset Summary & Characteristics

| Parameter | Value |
|---|---|
| **Raw Records (Rows)** | 45,593 |
| **Total Attributes (Columns)** | 20 (Raw) $\rightarrow$ 28 (Feature-Engineered) |
| **Processed Records** | 45,593 |
| **Missing Values Handled** | Numeric (Mean Imputed), Categorical (Mode Imputed) |
| **Mean Delivery Time** | 26.30 minutes |
| **Median Delivery Time** | 26.00 minutes |
| **Delivery Time Range** | 10.00 to 54.00 minutes |
| **Average Delivery Distance** | 9.74 km |
| **Peak Demand Proportion** | 65.48% (29,853 orders) |
| **Off-Peak Demand Proportion** | 34.52% (15,740 orders) |

---

## 2. Exploratory Data Analysis (EDA) Findings

### A. Hourly Order Demand Trends
- **Primary Peak (Dinner):** 18:00 to 22:00 (Peak hour: 19:00 with 4,595 orders, followed by 18:00 with 4,480 orders).
- **Secondary Peak (Lunch):** 12:00 to 14:00 (Lunch peak: 13:00 with ~1,850 orders).
- **Trough Period (Off-Peak):** 00:00 to 07:00 and mid-afternoon (15:00 to 17:00).

### B. Traffic & Environmental Impact on Delivery Times
- **Low Traffic:** Median delivery duration = 21.0 minutes.
- **Medium Traffic:** Median delivery duration = 26.0 minutes.
- **High Traffic:** Median delivery duration = 29.0 minutes.
- **Jam Conditions:** Median delivery duration = 35.0 minutes (**+14 minutes delay over low traffic**).
- **Weather Impact:** Sunny/Clear weather conditions reduce average delivery time by ~6.7 minutes compared to Foggy or Stormy weather.

---

## 3. Regression Modeling & Evaluation (Demand Duration Forecasting)

**Target Variable ($y$):** `delivery_time_min` (Continuous Delivery Duration)  
**Algorithm:** Multiple Linear Regression (`LinearRegression`)  
**Data Partition:** 80% Training ($N = 36,474$), 20% Testing ($N = 9,119$), `random_state = 42`  

### Calculated Evaluation Metrics

| Metric | Training Set | Testing Set | Performance Evaluation |
|---|---|---|---|
| **Mean Squared Error (MSE)** | 40.1144 | **39.6322** | Low residual variance |
| **Mean Absolute Error (MAE)** | 5.0236 min | **4.9990 min** | Average error < 5 minutes |
| **$R^2$ Score (Variance Explained)** | 0.5449 | **0.5480 (54.80%)** | Strong predictive fit on unseen data |

### Top Regression Feature Coefficients

| Rank | Feature Name | Coefficient ($\beta$) | Direction & Interpretation |
|---|---|---|---|
| 1 | `multiple_deliveries` | **+3.4409** | Each additional batch delivery increases delivery time by ~3.44 min. |
| 2 | `traffic_Jam` | **+1.0032** | Jam conditions add noticeable delivery delays. |
| 3 | `Delivery_person_Age` | **+0.4176** | Slightly longer delivery times with older courier age. |
| 4 | `distance_km` | **+0.3667** | Each additional kilometer adds ~0.37 min (22 seconds) transit time. |
| 5 | `Vehicle_condition` | **-2.3176** | Better vehicle condition reduces delivery time by ~2.32 min per tier. |
| 6 | `traffic_Low` | **-6.5874** | Low traffic conditions save ~6.59 minutes compared to baseline. |
| 7 | `weather_Sunny` | **-6.7157** | Clear/Sunny weather accelerates delivery by ~6.72 minutes. |
| 8 | `Delivery_person_Ratings` | **-7.1816** | Higher rated delivery personnel deliver ~7.18 minutes faster per rating point. |

---

## 4. Classification Modeling & Evaluation (Peak Hour Prediction)

**Target Variable ($y$):** `is_peak_hour` ($1 = \text{Peak Demand Hour}$, $0 = \text{Non-Peak Window}$)  
**Algorithm:** Logistic Regression (`LogisticRegression`)  
**Data Partition:** 80% Train, 20% Test (Stratified, `random_state = 42`)  

### Calculated Evaluation Metrics

| Metric | Training Set | Testing Set |
|---|---|---|
| **Accuracy Score** | 81.84% | **81.66%** |
| **Macro Average F1-Score** | 0.80 | 0.80 |
| **Weighted Average F1-Score** | 0.82 | 0.82 |

### Testing Confusion Matrix ($N = 9,119$)

| Actual \ Predicted | Predicted Non-Peak (0) | Predicted Peak Hour (1) | Total |
|---|---|---|---|
| **Actual Non-Peak (0)** | **2,314 (TN)** | 834 (FP) | 3,148 |
| **Actual Peak Hour (1)** | 838 (FN) | **5,133 (TP)** | 5,971 |
| **Total** | 3,152 | 5,967 | 9,119 |

- **True Positive Rate (Recall for Peak Hours):** $5,133 / 5,971 = 85.97\%$
- **Precision for Peak Hours:** $5,133 / 5,967 = 86.02\%$

---

## 5. Underfitting & Overfitting Diagnostics

| Model Type | Train Score | Test Score | Generalization Gap ($\Delta$) | Diagnostic Status |
|---|---|---|---|---|
| **Linear Regression ($R^2$)** | 0.5449 | 0.5480 | **0.0031** | Optimal Generalization (No Overfitting) |
| **Logistic Regression (Accuracy)** | 81.84% | 81.66% | **0.18%** | Optimal Generalization (No Overfitting) |

**Diagnostic Conclusion:** The difference between training and testing evaluation metrics is negligible ($\Delta R^2 < 0.01$, $\Delta \text{Acc} < 0.5\%$). The models demonstrate consistent generalization to unseen operational food delivery data without evidence of overfitting or high variance.
