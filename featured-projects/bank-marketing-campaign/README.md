### 📈 Bank Marketing Campaign Response Prediction
**<font color="green">Predicting Customer Subscription to Term Deposits using Logistic Regression** </font>
<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

Banks invest heavily in outbound marketing campaigns, yet only a small proportion of customers respond positively. Accurately identifying customers with the highest likelihood of subscribing enables banks to improve campaign effectiveness, reduce marketing costs, and deliver more targeted customer engagement.</br>

This project develops and evaluates predictive classification models using the Portuguese Bank Marketing Dataset to identify customers most likely to subscribe to a term deposit. Through exploratory data analysis, feature engineering, and logistic regression modelling, the project demonstrates how data-driven marketing can improve campaign performance while providing actionable business recommendations.</br>


</details>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>

Financial institutions frequently conduct direct marketing campaigns to promote term deposit products. However, response rates are typically low, making blanket marketing strategies inefficient and costly.</br>

This project explores customer demographics, campaign history, and macroeconomic indicators to determine the factors most strongly associated with successful subscription outcomes and builds predictive models to identify high-potential customers.</br>

---

| Category | Details |
|------|--------|
| **Analytics Capabilities** | 🧠 Business Analysis </br> 📥 Data Collection</br> 🧹 Data Cleaning </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering</br> 📈 Statistical Analysis </br> 🤖 Machine Learning </br>📊 Data Storytelling </br> 💡 Recommendations</br>|
| **Technology Stack** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) • ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) • ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) • ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) |
| **Models Evaluated** | Logistic Regression • Balanced Logistic Regression |
| **Project Artefacts** | 📓 [Jupyter Notebook](notebooks/bank-marketing-campaign-notebook.ipynb) |

</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM AND OBJECTIVE</b></summary></br>

**Business Problem**</br>

Only around **11% of customers** subscribed to the term deposit.</br>

Without predictive analytics, marketing teams:</br>
- Contact many customers unlikely to subscribe</br>
- Spend unnecessary campaign resources</br>
- Miss high-potential customers</br>

---

**Business Objective**</br>

Develop a machine learning model that predicts customer subscription likelihood to support more effective marketing campaigns.</br>

</details>

---

<details open>
<summary><b>🔍 EXPLORATORY DATA ANALYSIS</b></summary></br>

The following data transformation were done:</br>

- Missing value handling</br>
- Feature grouping</br>
- Age segmentation</br>
- Campaign grouping</br>
- One-hot encoding</br>
- Scaling numerical variables</br>
- Train-test split with stratification</br>

</details>

---

<details open>
<summary><b>🤖 PREDICTIVE MODELING</b></summary></br>

**Model 1: Standard Logistic Regression**</br>
Purpose: Establish baseline predictive performance</br>

Evaluation Metrics:</br>
- Accuracy</br>
- Precision</br>
- Recall</br>
- F1 Score</br>
- Confusion Matrix</br>

---

**Model 2: Balanced Logistic Regression**</br>
Purpose: Improve detection of customers who are likely to subscribe by addressing class imbalance.</br>

class_weight='balanced'</br>

Why did recall improved?</br>
Trade-off with precision</br>

</details>

---

<details open>
<summary><b>📊 MODEL COMPARISON</b></summary></br>

| Metric    | Logistic Regression | Balanced Logistic Regression |
| --------- | ------------------- | ---------------------------- |
| Accuracy  | XX                  | XX                           |
| Precision | XX                  | XX                           |
| Recall    | XX                  | XX                           |
| F1 Score  | XX                  | XX                           |

Although overall accuracy decreased slightly, **Balanced Logistic Regression** substantially improved Recall, enabling the bank to identify significantly more potential subscribers.</br>
For marketing campaigns where missed opportunities are costly, this represents a more practical business solution.</br>

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

**1. Customer Behaviour**</br>

- Previous campaign success is the strongest predictor of future subscription.</br>
- Customers contacted multiple times showed higher conversion potential.</br>
- First-time contacts generated the highest false negative rate.</br>

**2. Customer Segments**</br>

- Students and retirees demonstrated higher response rates.</br>
- Blue-collar customers showed lower conversion rates.</br>
- Older customers (65+) were frequently missed by the model.</br>

**3. Campaign Strategy**</br>

- Cellular contact outperformed telephone campaigns.</br>
- Certain months consistently delivered higher conversion performance.</br>
- Macroeconomic indicators contributed meaningful predictive value.</br>

</details>

---

<details open>
<summary><b>📉 ERROR ANALYSIS</b></summary></br>

- False Negatives</br>
- False Positives</br>
- Business interpretation</br>

Missing a likely subscriber represents lost sales opportunities. Error analysis identified demographic groups where the model underperformed, providing opportunities for future feature engineering and targeted campaign strategies.</br>


</details>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

**1. Customer Targeting**</br>

Prioritise customers with successful previous campaign interactions.</br>

**2. Marketing Channels**</br>

Increase investment in cellular campaigns.</br>

**3. Customer Segmentation**</br>

Develop specialised campaigns for:</br>
- Students</br>
- Retirees</br>
- High-value previous responders</br>

**4. Advanced Predictive Modeling** 
- Random Forest</br>
- XGBoost</br>
- Gradient Boosting</br>

</details>

---

<details open>
<summary><b>🗂 DATASET</b></summary></br>

| Description | Link |
|-------------|-----|
| Campaign results for a term deposit product of a Portuguese bank | [View Dataset](data/6.18_bank.csv) |

**Records:** 41,188 customer responses</br>

**Key Variables:**</br>
- Customer Demographics</br>
- Current Campaign Details and Results</br>
- Campaign History</br>
- Macroeconomic Indicators</br>

</details>

---

<details open>
<summary><b>🗂️ REPOSITORY STRUCTURE</b></summary></br>

| Folder        | Description                |
| ------------- | -------------------------- |
| 📁 charts     | Exploratory Visualisations |
| 📁 data       | Raw Dataset               |
| 📁 notebooks  | End-to-end Python analysis |

</details>

---

<details open>
<summary><b>✨ FUTURE ENHANCEMENTS</b></summary></br>

**1. Advanced Predictive Modeling** </br>
- Random Forest</br>
- XGBoost</br>
- Gradient Boosting</br>


ROC-AUC optimisation
SHAP explainability
Streamlit deployment
Hyperparameter tuning
Cost-sensitive learning

</details>

---


**🤝 Let's Connect!**</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

</details>