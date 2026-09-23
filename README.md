# 🍔 Online Food Delivery Demand Forecasting & Peak Hour Regression Model

**Subject:** 602 – Data Analytics Using Python (DAP)  
**Domain:** Food, E-Commerce & Consumer Analytics  
**Group:** 24 
**Semester:** TYBCA Sem-6  

---

## 📌 Project Overview
This project delivers an end-to-end data analytics pipeline and predictive modeling suite for online food delivery platforms (e.g., Zomato, Swiggy, UberEats). By analyzing 45,593 real operational delivery transactions, the project uncovers hourly demand patterns, identifies peak vs. off-peak demand distributions, and builds supervised regression (`LinearRegression`) and classification (`LogisticRegression`) models following the academic 15-step Data Analytics using Python (DAP) workflow.

---

## 📁 Project Structure

```text
Online_Food_Delivery_Demand_Forecasting/
│
├── data/
│   ├── raw/
│   │   └── food_delivery_raw.csv          # Real raw dataset (45,593 records, 20 columns)
│   └── processed/
│       └── food_delivery_clean.csv        # Cleaned and feature-engineered dataset (28 columns)
│
├── notebooks/                              # Academic DAP sequential Jupyter Notebooks
│   ├── 01_data_understanding.ipynb         # Steps 1–3: Imports, Data Loading, Structure Analysis
│   ├── 02_cleaning_eda.ipynb               # Steps 4–9: Cleaning, Imputation, Univariate/Bivariate/Multivariate EDA
│   ├── 03_regression_analysis.ipynb        # Steps 10–11: Train-Test Split, Linear Regression, Evaluation (MSE/MAE/R²)
│   ├── 04_classification_analysis.ipynb    # Steps 12–13: Logistic Regression, Peak Hour Classification, Confusion Matrix
│   └── 05_final_analysis.ipynb             # Steps 14–15: Underfitting/Overfitting Diagnostics & Final Conclusions
│
├── scripts/                                # Modular Python Automation Scripts
│   ├── data_loader.py                      # Data fetching and merging script
│   ├── data_cleaning.py                    # Data cleaning and feature engineering pipeline
│   ├── generate_all_outputs.py             # Execution pipeline generating all figures and models
│   └── build_notebooks.py                  # Jupyter notebook generator adhering to DAP syllabus
│
├── outputs/                                # Generated Project Artifacts
│   ├── figures/                            # High-resolution (300 DPI) analytical visualizations
│   │   ├── 01_delivery_time_distribution.png
│   │   ├── 02_hourly_demand_distribution.png
│   │   ├── 03_peak_vs_nonpeak_demand.png
│   │   ├── 04_day_of_week_demand.png
│   │   ├── 05_distance_vs_delivery_time.png
│   │   ├── 06_traffic_density_boxplot.png
│   │   ├── 07_multivariate_pivot_heatmap.png
│   │   ├── 08_correlation_heatmap.png
│   │   ├── 09_actual_vs_predicted_regression.png
│   │   ├── 10_regression_residuals_distribution.png
│   │   └── 11_classification_confusion_matrix.png
│   └── models/                             # Trained & serialized scikit-learn models
│       ├── linear_regression_demand.joblib
│       └── logistic_regression_peak_hour.joblib
│
├── docs/                                   # Documentation & Academic Viva Resources
│   ├── methodology.md                      # Detailed breakdown of all 15 DAP steps
│   ├── findings.md                         # Detailed empirical analytical findings & metrics
│   └── viva_questions.md                   # Curated TYBCA viva-voce Q&A guide
│
├── requirements.txt                        # Core project dependencies
└── README.md                               # Project documentation & summary
```

---

## 🔄 The 15-Step DAP Academic Workflow

| Step | Phase | Core Methodology & Implementation |
|---|---|---|
| **Step 1** | **Python Libraries Setup** | Import `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `sklearn`. |
| **Step 2** | **Loading Data & DataFrame** | Load `data/raw/food_delivery_raw.csv` (`45,593` rows, `20` cols). |
| **Step 3** | **Understanding the Data** | Analyze `.info()`, `.dtypes`, numerical vs categorical feature separation. |
| **Step 4** | **Data Spread & Preparation** | Clean strings, parse time/hours, calculate **Haversine Distance (km)**. |
| **Step 5** | **Missing Data & Outliers** | Audit missing values via `isnull().sum()`, outlier detection with boxplots. |
| **Step 6** | **Handling Missing Values** | Mean imputation (`df.fillna(df.mean(numeric_only=True))`) & mode imputation. |
| **Step 7** | **Univariate EDA** | Analyze distributions of delivery time, hourly demand, and peak hours. |
| **Step 8** | **Bivariate EDA** | Analyze Distance vs Delivery Time and Traffic Density vs Delivery Duration. |
| **Step 9** | **Multivariate EDA** | Cross-tabulation pivot heatmaps and correlation heatmap matrix. |
| **Step 10** | **Regression Analysis** | Train Multiple Linear Regression (`LinearRegression`) on 80/20 train-test split (`random_state=42`). |
| **Step 11** | **Regression Evaluation** | Calculate **MSE (39.63)**, **MAE (4.99 min)**, **$R^2$ (0.5480)**, and 45° Scatter Plot. |
| **Step 12** | **Classification Model** | Train Logistic Regression (`LogisticRegression`) for Peak vs Non-Peak hour classification. |
| **Step 13** | **Classification Evaluation** | Calculate **Accuracy (81.66%)** and generate Confusion Matrix heatmap. |
| **Step 14** | **Underfitting & Overfitting** | Train vs. Test comparison ($\Delta R^2 = 0.0031$, $\Delta \text{Acc} = 0.18\%$) confirming optimal fit. |
| **Step 15** | **Conclusions & Recommendations** | Summarize insights: 65.5% peak volume, traffic bottlenecks, dynamic fleet dispatch. |

---

## 📊 Key Empirical Findings

1. **Demand Peaks:** Food delivery orders exhibit strong bimodal demand peaks with dinner peak (18:00–22:00) accounting for the highest volume (peak hour: 19:00 with 4,595 orders) and a secondary lunch peak (12:00–14:00).
2. **Peak vs. Off-Peak Split:** Peak hours comprise **65.5%** of daily order demand, while off-peak hours represent **34.5%**.
3. **Traffic Bottlenecks:** `Jam` traffic conditions add an average delay of **+14 minutes** over `Low` traffic.
4. **Regression Forecasting:** Multiple Linear Regression achieves an **$R^2$ score of 0.5480** with a Mean Absolute Error (**MAE**) of **4.99 minutes**.
5. **Peak Hour Classification:** Logistic Regression accurately classifies order demand windows with **81.66% accuracy**.
6. **Model Stability:** Generalization gap between training and testing is under 0.003 for regression and 0.18% for classification, indicating zero overfitting.

---

## 🚀 How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Full Technical Pipeline
```bash
python scripts/generate_all_outputs.py
```

### 3. Launch Notebooks
```bash
jupyter notebook notebooks/01_data_understanding.ipynb
```
