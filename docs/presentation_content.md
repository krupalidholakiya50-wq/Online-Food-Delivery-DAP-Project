# 📑 Final Presentation Content Blueprint (Slide-by-Slide)

**Project:** Online Food Delivery Demand Forecasting & Peak Hour Regression Model  
**Subject:** 602 – Data Analytics Using Python (DAP) | **Group:** 6 | **Semester:** TYBCA Sem-6  

---

### Slide 1: Title Slide
- **Title:** Online Food Delivery Demand Forecasting & Peak Hour Regression Model
- **Subtitle:** Academic Data Analytics Project | Subject: 602 Data Analytics Using Python
- **Metadata:** Group No: 6 | Domain: Food, E-Commerce & Consumer Analytics

### Slide 2: Project Introduction & Domain Overview
- **Domain:** Food Delivery Operations & Consumer Analytics
- **Context:** Rapid expansion of on-demand platforms (Zomato, Swiggy, UberEats) requires precise demand forecasting and operational delivery optimization.
- **Scope:** End-to-end analysis of 45,593 delivery transactions using the 15-Step DAP academic pipeline.

### Slide 3: Problem Statement
- **Operational Challenge:** Severe delays during dinner & lunch peak hours due to traffic congestion and courier shortages.
- **Customer Impact:** Inaccurate delivery estimates degrade customer trust and satisfaction.
- **Analytics Solution:** Data-driven demand profiling, peak-hour prediction, and delivery duration regression modeling.

### Slide 4: Project Objectives
- Profile hourly consumer order patterns and identify peak demand intervals.
- Apply geospatial distance modeling (Haversine formula) to quantify route factors.
- Train Multiple Linear Regression to forecast operational delivery demand duration.
- Build Logistic Regression model to classify peak vs. off-peak order windows.
- Provide actionable fleet dispatch and dynamic surge buffer recommendations.

### Slide 5: Academic Source of Truth & DAP Workflow
- **Framework:** VNSGU 602 DAP Curriculum Reference (`stepbystep.md`, `marking-structure-scheme.md`).
- **Standard Sequence:** 15-Step rigorous pipeline from Library Imports to Conclusions.
- **Evaluation Criteria:** Data Understanding (20M), EDA (25M), Regression/ML (25M), Model Evaluation (15M), Presentation (15M).

### Slide 6: Dataset Description & Characteristics
- **Dataset:** Real Benchmark Food Delivery Operations Dataset (45,593 records).
- **Temporal Features:** Order Date, Time Ordered, Pickup Time.
- **Spatial Features:** Restaurant & Delivery GPS coordinates.
- **Operational Features:** Traffic density, Weather, Vehicle condition, Courier ratings, Delivery duration.

### Slide 7: Step 1 — Python Libraries & Environment Setup
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib.pyplot`, `seaborn`
- **Machine Learning:** `sklearn.model_selection`, `sklearn.linear_model`, `sklearn.metrics`

### Slide 8: Step 2 — Loading Data & DataFrame Creation
- **Method:** `pd.read_csv('../data/raw/food_delivery_raw.csv')`
- **Dimensions:** 45,593 rows × 20 columns.
- **Verification:** `.head()`, `.tail()`, and `.shape` inspections.

### Slide 9: Step 3 — Understanding Data Structure & Types
- **Data Types:** 10 numerical features, 13 categorical/string features, 1 datetime feature.
- **Descriptive Statistics:** Five-number summary via `.describe()`.
- **Target Identification:** Continuous target (`delivery_time_min`) and temporal target (`is_peak_hour`).

### Slide 10: Step 4 — Data Cleaning & Feature Engineering
- **String Parsing:** Cleaning `"(min) 24"` format artifacts into numeric float values.
- **Haversine Distance:** Calculating spherical distance in kilometers between restaurant and customer coordinates.
- **Temporal Feature Extraction:** Extracting `order_hour`, `day_of_week`, and `is_weekend`.

### Slide 11: Step 5 & 6 — Missing Values & Outlier Handling
- **Missing Value Audit:** Systematic identification via `df.isnull().sum()`.
- **Numerical Imputation:** Mean imputation following DAP reference: `df.fillna(df.mean(numeric_only=True))`.
- **Categorical Imputation:** Mode imputation for traffic, weather, and city columns.
- **Outliers Analysis:** Validated extreme values (>45 min) as genuine traffic/weather delays.

### Slide 12: Step 7 — Univariate EDA: Delivery Time Distribution
- **Visual:** `01_delivery_time_distribution.png`
- **Mean:** 26.30 min | **Median:** 26.00 min | **Range:** 10 to 54 min.
- **Takeaway:** Symmetric bell-shaped distribution with typical deliveries taking 15–40 minutes.

### Slide 13: Step 7 — Univariate EDA: Hourly Demand Pattern
- **Visual:** `02_hourly_demand_distribution.png`
- **Primary Peak (Dinner):** 18:00–22:00 (Max: 19:00 with 4,595 orders).
- **Secondary Peak (Lunch):** 12:00–14:00.
- **Takeaway:** Clear bimodal consumer demand curve guiding courier fleet scheduling.

### Slide 14: Step 7 — Univariate EDA: Peak vs. Non-Peak Split
- **Visual:** `03_peak_vs_nonpeak_demand.png`
- **Peak Volume:** 65.48% (29,853 orders).
- **Off-Peak Volume:** 34.52% (15,740 orders).
- **Takeaway:** Nearly two-thirds of all platform traffic is concentrated in peak windows.

### Slide 15: Step 7 — Univariate EDA: Weekly Demand Trends
- **Visual:** `04_day_of_week_demand.png`
- **Pattern:** Steady weekday demand with noticeable surges on Friday, Saturday, and Sunday.
- **Takeaway:** Weekend demand requires +15% extra courier workforce allocation.

### Slide 16: Step 8 — Bivariate EDA: Distance vs. Delivery Duration
- **Visual:** `05_distance_vs_delivery_time.png`
- **Pattern:** Positive linear correlation between transit distance and delivery time.
- **Takeaway:** Higher traffic density shifts delivery time upward across all distances.

### Slide 17: Step 8 — Bivariate EDA: Traffic Density Impact
- **Visual:** `06_traffic_density_boxplot.png`
- **Low Traffic:** Median 21 min | **Jam Traffic:** Median 35 min.
- **Takeaway:** Severe traffic jam introduces an average delay of +14 minutes per delivery.

### Slide 18: Step 9 — Multivariate EDA: Order Type & Traffic Cross-Tab
- **Visual:** `07_multivariate_pivot_heatmap.png`
- **Finding:** Preparation times across order types (Snack, Meal, Drinks, Buffet) are uniform (~25–27 min).
- **Takeaway:** Traffic condition is the primary external variance driver across all meal categories.

### Slide 19: Step 9 — Multivariate EDA: Feature Correlation Matrix
- **Visual:** `08_correlation_heatmap.png`
- **Positive Drivers:** `multiple_deliveries`, `distance_km`, `Delivery_person_Age`.
- **Negative Drivers (Efficiency):** `Delivery_person_Ratings`, `Vehicle_condition`, `traffic_Low`.

### Slide 20: Step 10 — Regression Modeling Architecture
- **Objective:** Operational Delivery Demand Duration Forecasting.
- **Target ($y$):** `delivery_time_min` | **Model:** `LinearRegression()`
- **Train-Test Split:** 80% Train ($N=36,474$), 20% Test ($N=9,119$), `random_state=42`.
- **Encoding:** One-hot encoding for road traffic density and weather conditions.

### Slide 21: Step 10 — Regression Coefficients & Feature Importance
- **Top Delay Factors:** Multiple Deliveries (+3.44 min), Jam Traffic (+1.00 min), Distance (+0.37 min/km).
- **Top Speed Factors:** Courier Rating (-7.18 min/star), Low Traffic (-6.59 min), Vehicle Condition (-2.32 min/tier).

### Slide 22: Step 11 — Regression Evaluation Metrics
- **Mean Squared Error (MSE):** 39.6322 (Test) vs 40.1144 (Train).
- **Mean Absolute Error (MAE):** 4.9990 min (Average error < 5 minutes).
- **Coefficient of Determination ($R^2$):** 0.5480 (54.80% variance explained on unseen data).

### Slide 23: Step 11 — Actual vs. Predicted Scatter Plot (45° Line)
- **Visual:** `09_actual_vs_predicted_regression.png`
- **DAP Requirement:** 45-degree reference diagonal line ($y=x$).
- **Takeaway:** Points cluster evenly around the diagonal, demonstrating unbiased linear prediction.

### Slide 24: Step 12 & 13 — Classification Modeling (Peak Hour Prediction)
- **Objective:** Classify whether an order occurs during peak demand intervals.
- **Target ($y$):** `is_peak_hour` ($1 = \text{Peak}$, $0 = \text{Off-Peak}$).
- **Model:** `LogisticRegression(max_iter=1000)`.
- **Split:** Stratified 80/20 train-test split ($N=9,119$).

### Slide 25: Step 13 — Classification Evaluation & Confusion Matrix
- **Visual:** `11_classification_confusion_matrix.png`
- **Test Accuracy:** 81.66% | **Train Accuracy:** 81.84%.
- **Confusion Matrix:** True Negatives = 2,314 | False Positives = 834 | False Negatives = 838 | True Positives = 5,133.
- **Peak Hour Recall:** 85.97% | **Peak Hour Precision:** 86.02%.

### Slide 26: Step 14 — Underfitting vs. Overfitting Diagnostics
- **Regression Gap:** Train $R^2 = 0.5449$ vs. Test $R^2 = 0.5480$ ($\Delta = 0.0031$).
- **Classification Gap:** Train Acc = 81.84% vs. Test Acc = 81.66% ($\Delta = 0.18\%$).
- **Diagnosis:** Optimal generalization with negligible variance gap and zero overfitting.

### Slide 27: Step 15 — Key Findings & Business Recommendations
- **Dynamic Rider Pre-Allocation:** Position couriers in high-density restaurant hubs 30 min before dinner peak.
- **Dynamic ETA Buffers:** Increase customer delivery time estimates by 8–12 min during peak traffic jams.
- **Fleet Maintenance Incentives:** Support delivery partners in vehicle servicing to maintain Tier 1/2 condition.

### Slide 28: Future Scope & Enhancements
- Incorporation of real-time GPS live routing via OpenStreetMap / Google Maps API.
- Non-linear ensemble model exploration (Random Forest, XGBoost) for non-linear weather interactions.
- Customer order item volume and dynamic pricing integration.

### Slide 29: References & Academic Acknowledgements
- VNSGU 602 Data Analytics Using Python (DAP) Syllabus & Guidelines.
- Scikit-learn, Pandas, Seaborn, Matplotlib Documentation.
- Zomato/Swiggy Operational Benchmark Dataset Reference.
- Q&A / Viva-Voce Discussion.
