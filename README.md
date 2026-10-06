# 🍔 Online Food Delivery Demand Forecasting & Peak Hour Regression Model

**Subject:** 602 – Data Analytics Using Python (DAP)  
**Domain:** Food Delivery Operations & Consumer Logistics Analytics  
**Course:** TYBCA (Semester-6) Minor Project  
**Target Variable:** `delivery_time_min` (Continuous Delivery Duration in Minutes)  
**Primary Analytical Methodology:** Supervised Machine Learning (Continuous Regression Analysis)  
**Target Benchmark:** Variance Explained ($R^2 \ge 80\%$) — **Achieved: $80.34\%$**

---

## 📌 Project Overview

This project presents an empirical Data Analytics and Predictive Regression framework for on-demand online food delivery platforms (such as Swiggy, Zomato, and UberEats). Leveraging **45,593 verified, real-world delivery transactions** across major Indian metropolitan areas, the study investigates key operational factors—spatial travel distance, courier demographics, customer ratings, atmospheric weather conditions, and road traffic congestion—influencing delivery duration.

### 🎓 Academic Standards & Requirements
- **15-Chapter Academic Structure:** Organized strictly in accordance with TYBCA academic curriculum guidelines.
- **Classification Removed:** Strictly continuous regression modeling for delivery latency forecasting.
- **Academic Visualizations:** Exactly **14 standardized visualizations** embedded directly in the master Jupyter Notebook spanning Univariate, Bivariate, Multivariate, Correlation, and Regression Evaluation diagnostics.
- **Real-World Data Integrity:** Strictly zero synthetic or placeholder data; all models and charts are derived directly from the verified 45,593 transaction records.

---

## 📚 Standard 15-Chapter Academic Structure & Analysis Flow

```text
Chapter 01 — Project Definition
Chapter 02 — Dataset Details
Chapter 03 — Python Tools & Libraries Used
Chapter 04 — Understanding the Data
Chapter 05 — Understanding Spread of Data
Chapter 06 — Automating EDA Using Python
Chapter 07 — Handling Missing Data and Outliers
Chapter 08 — Univariate Analysis (Charts 1 to 4)
Chapter 09 — Bivariate Analysis (Charts 5 to 9)
Chapter 10 — Multivariate Analysis (Chart 10: 5×5 Pair Plot)
Chapter 11 — Correlation Analysis (Chart 11: Pearson Heatmap)
Chapter 12 — Regression Analysis (Model Training & Feature Encoding)
Chapter 13 — Model Evaluation & Fit Diagnosis (Charts 12 to 14)
Chapter 14 — Conclusion / Findings
Chapter 15 — References
```

---

## 📊 Complete & Exact Chart Visual Catalog (14 Figures in Master Notebook)

| Chart # | Chart Type | Academic Chapter | Analytical Description & Key Variables |
|:---:|:---|:---|:---|
| **01** | **Histogram (with KDE)** | Chapter 08 — Univariate | Frequency distribution of `delivery_time_min` with Mean (26.2 min) and Median (26.0 min) markers. |
| **02** | **Histogram (with KDE)** | Chapter 08 — Univariate | Spatial distribution of geodesic delivery distances (`distance_km`) across urban delivery zones. |
| **03** | **Histogram (with KDE)** | Chapter 08 — Univariate | Density distribution of courier customer ratings (`Delivery_person_Ratings`) showing peak at 4.6–4.9. |
| **04** | **Box Plot** | Chapter 08 — Univariate | Five-number summary (Q1, Median, Q3, Whiskers) and outlier dispersion of `delivery_time_min`. |
| **05** | **Scatter Plot + Trend Line** | Chapter 09 — Bivariate | Distance vs. Delivery Time with fitted Ordinary Least Squares linear regression trend line. |
| **06** | **Box Plot** | Chapter 09 — Bivariate | Delivery duration spread across road congestion tiers (`Low`, `Medium`, `High`, `Jam`). |
| **07** | **Box Plot** | Chapter 09 — Bivariate | Delivery latency comparison across atmospheric conditions (`Sunny`, `Cloudy`, `Fog`, `Stormy`, etc.). |
| **08** | **Box Plot** | Chapter 09 — Bivariate | Latency impact of dispatching multiple concurrent batch orders (0, 1, 2, 3 orders). |
| **09** | **Grouped Bar Chart** | Chapter 09 — Bivariate | Order volume demand by traffic density clustered across Peak vs. Off-Peak operational windows. |
| **10** | **5×5 Pair Plot** | Chapter 10 — Multivariate | High-dimensional scatter matrix and KDE diagonal plots across 5 continuous variables grouped by Traffic Hue. |
| **11** | **Correlation Heatmap** | Chapter 11 — Correlation | Annotated Pearson correlation matrix ($r$) across all numerical operational features. |
| **12** | **Scatter Plot ($y=x$ Line)** | Chapter 13 — Model Evaluation | Actual vs. Predicted delivery durations plotted against the ideal 45° line on unseen test data ($N=9,119$). |
| **13** | **Histogram (Residuals)** | Chapter 13 — Model Evaluation | Distribution of regression residual errors ($e_i = y_i - \hat{y}_i$) with zero-error reference line. |
| **14** | **Horizontal Bar Chart** | Chapter 13 — Model Evaluation | Benchmark comparison of Test $R^2$ scores across Linear Regression, Random Forest, and Gradient Boosting. |

---

## 📈 Supervised Regression Performance Benchmark

Target Variable: `delivery_time_min` | Train Set: 36,474 records (80%) | Test Set: 9,119 records (20%)

| Regression Algorithm | Train $R^2$ | Test $R^2$ | Test $R^2$ (%) | Test MAE (min) | Test RMSE (min) | Academic Status |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Linear Regression (Baseline)** | 0.5644 | 0.5679 | 56.79% | 4.882 min | 6.155 min | Baseline Reference |
| **Random Forest Regressor** | 0.8936 | 0.8042 | 80.42% | 3.288 min | 4.144 min | Ensemble Competitor |
| **Gradient Boosting Regressor (Final)** | **0.8326** | **0.8034** | **80.34%** | **3.307 min** | **4.152 min** | **Selected Final Model ($\ge 80\%$)** |

---

## 🔍 Key Empirical Findings

1. **Traffic Congestion is the Dominant Factor:** Severe road traffic jams (`Jam`) increase median delivery time to **39.0 minutes**, representing an **85.7% increase** over free-flow (`Low`) traffic conditions (median 21.0 minutes).
2. **Batch Multi-Drop Penalty:** Assigning multiple concurrent orders to a single courier escalates delivery times non-linearly, with 3 concurrent orders resulting in a median delivery time of **45.0 minutes**.
3. **Weather Disruption:** Severe adverse weather conditions (`Fog`, `Stormy`, `Sandstorms`) elevate median delivery durations by **10–14 minutes** compared to clear `Sunny` weather.
4. **Spatial Correlation:** Delivery duration exhibits a stable positive linear correlation ($r \approx 0.30$) with geodesic delivery distance, scaling at $\approx 0.52\text{ min/km}$.
5. **Model Accuracy:** The Gradient Boosting Regressor predicts delivery durations with an average absolute error of only **$\pm 3.307$ minutes**, providing dependable estimates for dynamic dispatch and customer ETA presentation.

---

## 📁 Repository Directory Layout

```text
Online_Food_Delivery_Demand_Forecasting/
│
├── data/
│   ├── raw/
│   │   └── food_delivery_raw.csv           # Original 45,593 delivery records (20 raw attributes)
│   └── processed/
│       └── food_delivery_clean.csv         # Cleaned & feature-engineered dataset (31 columns)
│
├── notebooks/                              # Master Academic Jupyter Notebook
│   └── Online_Food_Delivery_DAP_Final.ipynb # ⭐ 15-Chapter Self-Contained Executed Master Notebook (14 Charts)
│
├── outputs/                                # Academic Visualizations
│   └── figures/                            # 14 High-Resolution (300 DPI) Charts
│       ├── 01_delivery_time_distribution.png
│       ├── 02_distance_distribution.png
│       ├── 03_rating_distribution.png
│       ├── 04_delivery_time_boxplot.png
│       ├── 05_distance_vs_delivery_time.png
│       ├── 06_traffic_density_boxplot.png
│       ├── 07_weather_conditions_boxplot.png
│       ├── 08_multiple_deliveries_boxplot.png
│       ├── 09_peak_vs_traffic_barchart.png
│       ├── 10_multivariate_pairplot.png
│       ├── 11_correlation_heatmap.png
│       ├── 12_actual_vs_predicted_regression.png
│       ├── 13_regression_residuals_distribution.png
│       └── 14_regression_model_comparison.png
│
├── docs/                                   # Documentation & Academic Viva Resources
│   ├── methodology.md                      # Detailed technical methodology report
│   ├── findings.md                         # Detailed empirical analytical findings
│   └── viva_questions.md                   # Curated TYBCA viva-voce examination guide
│
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## ⚙️ Quickstart & Reproduction Guide

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Master Jupyter Notebook
Launch Jupyter Notebook or JupyterLab and run the self-contained master notebook:
```bash
jupyter notebook notebooks/Online_Food_Delivery_DAP_Final.ipynb
```
All data cleaning, 14 academic charts, regression models, and diagnostic evaluations execute end-to-end without external script dependencies.
