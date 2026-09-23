# 🎓 TYBCA Data Analytics (602 DAP) Viva-Voce Questions & Answers

**Project Title:** Online Food Delivery Demand Forecasting & Peak Hour Regression Model  
**Subject:** 602 – Data Analytics Using Python (DAP)  
**Group:** 6  

---

### Q1. What is the main objective of this project?
**Ans:** The objective is to forecast online food delivery operational demand and delivery duration, identify peak order hours (lunch/dinner), and build predictive regression (`LinearRegression`) and classification (`LogisticRegression`) models following the 15-step academic DAP workflow.

---

### Q2. What dataset was used in this project?
**Ans:** We used a real benchmark Online Food Delivery operations dataset containing **45,593 records** across **20 base features**, covering order dates, order placement times, pickup times, weather conditions, traffic density, courier ratings, age, vehicle condition, and delivery location coordinates.

---

### Q3. How were the missing values handled in the dataset?
**Ans:** We strictly followed the academic DAP curriculum standard:
- For numerical variables, we applied mean imputation: `df.fillna(df.mean(numeric_only=True))`.
- For categorical variables, we applied mode imputation using the most frequent category.

---

### Q4. How did you calculate the delivery distance?
**Ans:** We used the **Haversine formula** on restaurant GPS coordinates (`Restaurant_latitude`, `Restaurant_longitude`) and customer delivery GPS coordinates (`Delivery_location_latitude`, `Delivery_location_longitude`) to calculate the great-circle spherical distance in kilometers.

---

### Q5. What is the difference between Univariate, Bivariate, and Multivariate EDA?
**Ans:**
- **Univariate Analysis:** Analyzing one variable at a time (e.g., histogram of delivery times, countplot of hourly order volume).
- **Bivariate Analysis:** Analyzing relationships between two variables (e.g., scatter plot of distance vs. delivery time, boxplot of traffic levels vs. delivery time).
- **Multivariate Analysis:** Analyzing interactions among three or more variables simultaneously (e.g., two-way cross-tabulation pivot heatmaps and correlation matrix).

---

### Q6. What is `train_test_split` and why is `random_state` defined?
**Ans:** `train_test_split` splits the dataset into a training subset (80%) used to train the model and an independent testing subset (20%) used to evaluate how well the model generalizes to unseen data. `random_state=42` sets the random seed so that the data split is deterministic and 100% reproducible.

---

### Q7. What are the regression evaluation metrics used, and what do they mean?
**Ans:**
1. **MSE (Mean Squared Error):** Measures the average squared difference between actual and predicted delivery times. Penalizes large errors heavily ($MSE = 39.63$).
2. **MAE (Mean Absolute Error):** Measures the average magnitude of absolute errors in the original units (minutes). In our project, $MAE = 4.9990\text{ min}$ (on average, predictions are within ~5 minutes of actual delivery time).
3. **$R^2$ Score (Coefficient of Determination):** Represents the proportion of variance in the target variable explained by the predictors ($R^2 = 0.5480$ or $54.80\%$).

---

### Q8. Why is there a 45-degree line in the Actual vs. Predicted scatter plot?
**Ans:** The 45-degree diagonal dashed line represents the line of perfect prediction where $\text{Actual} = \text{Predicted}$ ($y = x$). Points clustering tightly along this line signify high model accuracy.

---

### Q9. What was the classification target and why was Logistic Regression used?
**Ans:** The classification target was `is_peak_hour` ($1 = \text{Peak Demand Hours (Lunch 12-14h, Dinner 18-23h)}$, $0 = \text{Non-Peak Window}$). Logistic Regression was used because the target is binary (categorical 0/1), estimating the log-odds probability of an order occurring during peak demand.

---

### Q10. What is a Confusion Matrix? What were your project's results?
**Ans:** A confusion matrix is a $2 \times 2$ table showing the counts of True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN).
- **True Positives (Peak correctly predicted):** 5,133
- **True Negatives (Non-peak correctly predicted):** 2,314
- **False Positives:** 834
- **False Negatives:** 838
- **Overall Test Accuracy:** **81.66%**

---

### Q11. How do you diagnose Underfitting and Overfitting in this project?
**Ans:** We compare training scores with testing scores:
- **Regression:** Train $R^2 = 0.5449$ vs. Test $R^2 = 0.5480$ (Gap = $0.0031$).
- **Classification:** Train Accuracy = $81.84\%$ vs. Test Accuracy = $81.66\%$ (Gap = $0.18\%$).
- Since the gap between training and testing performance is nearly zero, the models generalize well to new data with no evidence of overfitting (high variance) or severe underfitting.

---

### Q12. What are the key business insights for food delivery platforms?
**Ans:**
1. Over **65.5%** of daily order demand is concentrated in lunch (12-14h) and dinner (18-22h) peak windows.
2. Severe traffic jams add an average of **+14 minutes** to delivery duration.
3. Delivery partner rating and vehicle condition significantly reduce delivery duration.
4. Platforms should dynamically pre-allocate riders 30 minutes before dinner peak (17:30) and adjust customer ETA buffers during high-traffic alerts.
