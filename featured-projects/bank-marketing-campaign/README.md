### 📈 Bank Marketing Campaign Response Prediction
**<font color="green">Predicting Customer Subscription to Term Deposits using Logistic Regression** </font>
<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

🎯 Developed a machine learning classification model to **predict term deposit subscriptions** using the Portuguese Bank Marketing Dataset, enabling more targeted marketing campaigns.</br>

🔍 Performed Exploratory Data Analysis (EDA) and feature engineering to **identify the customer, campaign, and economic factors influencing subscription behaviour**.</br>

🤖 Built and evaluated **Standard and Balanced Logistic Regression models** using Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.</br>

🏆 Selected the **Balanced Logistic Regression model**, improving Recall from 21% to 62% and reducing missed subscribers by over 50%.</br>

💡 Delivered **actionable marketing recommendations** to improve customer targeting, campaign effectiveness, and subscription rates.</br>

</details>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>

Financial institutions rely on direct marketing campaigns to promote term deposit products, but low subscription rates make customer targeting challenging.</br>

This project applies exploratory data analysis and machine learning to identify the key factors influencing customer subscriptions and predict high-potential customers for more effective marketing campaigns.</br>

---

| Category | Details |
|------|--------|
| **Analytics Capabilities** | 🧠 Business Analysis </br> 📥 Data Collection</br> 🧹 Data Cleaning </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering</br> 📈 Statistical Analysis </br> 🤖 Machine Learning </br>📊 Data Storytelling </br> 💡 Recommendations</br>|
| **Technology Stack** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) • ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) • ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) • ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) • ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square&logo=python&logoColor=white) • ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) |
| **Models Evaluated** | Standard Logistic Regression • Balanced Logistic Regression |
| **Project Artefacts** | 📓 [Jupyter Notebook](notebooks/bank-marketing-campaign-notebook.ipynb) |

</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM AND OBJECTIVE</b></summary></br>

**💼 Business Problem**</br>

Only **11% of customers** subscribed to the term deposit, making customer acquisition costly and inefficient.</br>

Without predictive analytics, the bank risks:</br>
- Contacting unlikely customers</br>
- Missing high-potential subscribers</br>
- Increasing campaign costs</br>

---

**🎯 Business Objective**</br>

Build a machine learning model to:</br>
- Predict customers likely to subscribe</br>
- Improve campaign targeting</br>
- Reduce missed opportunities</br>
- Support data-driven marketing decisions</br>

</details>

---

<details open>
<summary><b>🔍 EXPLORATORY DATA ANALYSIS & FEATURE ENGINEERING</b></summary></br>

**🔍 Exploratory Data Analysis**</br>

Exploratory Data Analysis (EDA) was conducted to understand customer subscription behaviour, identify meaningful relationships between variables, and select the most relevant features for predictive modelling. Both numerical and categorical variables were analysed to uncover behavioural patterns, evaluate data quality, and guide feature engineering.</br>

The analysis explored:</br>
- **Customer demographics** (age, education, occupation, marital status)</br>
- Previous campaign interactions and customer engagement history</br>
- **Marketing campaign characteristics** (contact method, month, number of contacts)</br>
-  **Economic indicators** (Euribor rate and Consumer Confidence Index)</br>
- Relationships between customer attributes and term deposit subscription outcomes</br>
- **Class imbalance** between subscribers ("Yes") and non-subscribers ("No")</br>

Insights from the EDA informed the feature selection process and the development of both Logistic Regression models.</br>

---

**💻 Data Preparation & Feature Engineering**</br>
To improve model performance and ensure the data was suitable for machine learning, several pre-processing and feature engineering techniques were applied.</br>

| Transformation                        | Purpose           |
|---------------------------------------|-------------------|
| **Missing Value Handling**            | Preserved meaningful customer information |
| **Feature Selection**                 | Identify the strongest predictors of customer subscription    |
| **Age Segmentation**                  | Created meaningful age bands  |
| **Campaign Grouping**                 | Grouped contact frequency into business-friendly bands    |
| **One-Hot Encoding**                  | Converted categories into model-ready variables   |
| **Feature Scaling**                   | Standardised numerical variables  |
| **Stratified Split**                  | Preserved the original class distribution (89%-No, 11%-Yes)   |

---

**Selected Predictive Features**</br>

The final model combined customer profile, campaign history, current campaign details and economic conditions..</br>

| Customer Profile      | Campaign History      | Current Campaign Details      | Economic Conditions   |  
|---------------------- | --------------------- | ----------------------------- | --------------------- |
| - Age Group</br> - Job</br> - Education</br> - Marital Status</br> | - Previous Campaign Outcome</br> - Previous Contacts</br> - Previously Contacted</br> | - Contact Method</br> - Campaign Month</br> - Campaign Contact Group</br> | - Euribor 3-Month Rate</br> - Consumer Confidence Index</br> | 

---

<details open>
<summary><b>🤖 PREDICTIVE MODELING</b></summary></br>

| Modelling Workflow    | Evaluation Metrics    |
|-----------------------| ----------------------|
| 🧠 Business Problem </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering </br> 📏 Model 1: Standard Logistic Regression </br> 🤔 Class Imbalance Identified </br> ⚖️ Model 2: Balanced Logistic Regression </br> ☯️ Model Comparison </br> 💡Business Recommendation | 🎯 Accuracy</br> 🔍 Precision</br> ✅ Recall</br> 🏎️ F1 Score</br> 🔢 Confusion Matrix</br>   | 


**📏 Model 1: Standard Logistic Regression**</br>
**Purpose:** Establish a baseline classification model using the original dataset.</br>

**Approach:**</br>
- Trained using the original class distribution.</br>
- Assumes all observations have equal importance.</br>
- Serves as the benchmark for evaluating model improvements.</br>

---

**⚖️ Model 2: Balanced Logistic Regression**</br>
**Purpose:** Improve the model's ability to identify potential subscribers by addressing the class imbalance within the dataset.</br>

**Why was balancing needed?**
Only **11%** of customers subscribed to the term deposit, while **89%** did not.
Without balancing, the model naturally learns to predict **"No"** most of the time because it achieves high accuracy simply by favouring the majority class.

This assigns greater importance to the minority class **"Yes"**, encouraging the model to learn patterns associated with potential subscribers instead of predominantly predicting non-subscribers.

```bash 
class_weight='balanced'
```

</details>

---

<details open>
<summary><b>📊 MODEL COMPARISON</b></summary></br>

| Metric                | Standard Logistic Regression  | Balanced Logistic Regression  | Better Model? |
| --------------------- | ----------------------------- | ----------------------------- | ------------- |
| Accuracy              | **90%**                       | 80%                           | Standard      |
| Precision             | **61%**                       | 31%                           | Standard      |
| Recall                | 21%                           | **62%**                       | Balanced      |
| F1 Score              | 0.31                          | **0.42**                      | Balanced      |
| True Positives (TP)   | 195                           | **578**                       | Balanced      |       
| False Negatives (FN)  | 733                           | **350**                       | Balanced      |
| False Positives (FP)  | **125**                       | 1,277                         | Standard      |
| True Negatives (TN)   | **7,185**                     | 6,033                         | Standard      |

</details>

---

**🏆 Best Performing Model**</br>

**<font color="green">⚖️ Balanced Logistic Regression**</font></br>

Despite a reduction in overall accuracy (80%) and precision (31%), the Balanced Logistic Regression model delivered significantly stronger business value by **identifying nearly three times more potential subscribers** and **reducing missed opportunities by over 50%**.</br>

For customer acquisition campaigns, missing a potential subscriber is generally more costly than contacting a customer who ultimately does not subscribe. 

Therefore, the Balanced Logistic Regression model provides a more practical and effective solution for supporting targeted marketing decisions.</br>

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

1. **Previous campaign success** was the strongest predictor of future subscription.</br>

2. **Cellular campaigns** consistently outperformed telephone campaigns.</br>

3. **Retirees and students** responded more positively than other customer groups.</br>

4. **Economic conditions** influenced customer subscription behaviour.</br>

5. **Improving Recall from 21% to 62%** substantially reduced missed sales opportunities.</br>

</details>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

1. Prioritise customers with **successful previous campaign responses**.</br>

2. Increase investment in **cellular campaigns** and **schedule campaigns during peak months** such as March, October, September, and December.</br> 

3. Personalise marketing **by customer segment**.</br>

4. Incorporate **economic indicators** into campaign planning.</br>

5. Deploy the **Balanced Logistic Regression model**.</br>

</details>

---

<details open>
<summary><b>📝 DEFINITION OF TERMS</b></summary></br>

| Term                | Definition  | 
| --------------------- | ----------------------------- |
| Accuracy              | The percentage of **all predictions the model got correct**, whether the customer subscribed or not.</br>     |
| Precision              | Of all customers the model predicted **would subscribe**, how many actually did. A higher precision means fewer unnecessary marketing calls.</br>        |
| Recall              | Of all customers who actually subscribed, how many the model successfully identified. **A higher recall means fewer missed sales opportunities.**</br>      |
| F1 Score              | A single measure that balances **Precision** and **Recall**, showing how well the model identifies subscribers while minimizing incorrect predictions.</br>       |
| True Negative (TN)              | Model correctly predicted that customer will NOT subscribe</br>     |
| True Positive (TP)              | Model correctly predicted that customer WILL subscribe</br>     |
| False Positive (FP)              | Model predicted that customer WILL subscribe BUT actual result customer did NOT subscribe</br> The bank targeted a customer expecting them to subscribe, but the customer ultimately DID NOT subscribe.</br>       |
| False Negative (FN)              | Model predicted customer will NOT subscribe BUT actual result customer WOULD HAVE subscribed</br>  The bank failed to identify a customer who was ACTUALLY LIKELY to subscribe. The bank may not contact them, miss potential revenue and lose conversion opportunities.</br>      |
| Confusion Matrix      | Shows the number of correct and incorrect predictions, providing insight into business trade-offs such as missed subscribers and unnecessary customer contacts.</br>      |
  
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

**1. 🌲 Evaluate Random Forest, XGBoost and Gradient Boosting.**</br>

To compare predictive performance against Logistic Regression and identify the best-performing model.</br>

**Why it matters:**</br>

Improve Recall, F1 Score, and overall predictive performance by capturing complex, non-linear relationships.</br>

**2. 🔍 Apply SHAP (SHapley Additive exPlanations) for model explainability.**</br>

Explains how individual features influence prediction outcomes and improve model transparency.</br>

**Why it matters:**</br>

Understand the key drivers of subscription decisions.</br>

**3. 🌐 Deploy an Interactive Streamlit Application**</br>

To allow users to input customer attributes and receive real-time subscription predictions.</br>

**Why it matters:**</br>

A practical application of machine learning for users by having an accessible decision-support tool.</br>

</details>

---

**🤝 Let's Connect!**</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

</details>

---

<details>
<summary><b>📉 ERROR ANALYSIS</b></summary></br>

**A. False Negatives (Missed Opportunities)**</br>

| Model                         | False Negatives   | 
| ----------------------------- | ------------------| 
| Standard Logistic Regression  | 733               |
| Balanced Logistic Regression  | 350               |

**🔂 Business Interpretation**</br>

False negatives represent customers who would have subscribed but were predicted as non-subscribers.</br>

**💎 Business Impact**</br>

The Balanced Logistic Regression reduced missed opportunities by **383 customers (52%)**, making it significantly more effective at identifying potential subscribers.</br>

- Lost term deposit revenue</br>
- Missed cross-selling opportunities</br>
- Lower campaign conversion rates</br>
- Reduced customer acquisition effectiveness</br>

**B. False Positives (Additional Marketing Cost)**</br>

| Model                         | False Positives   | 
| ----------------------------- | ------------------| 
| Standard Logistic Regression  | 125               |
| Balanced Logistic Regression  | 1,277             |

**🔂 Business Interpretation**</br>

False positives represent customers predicted to subscribe but who ultimately did not.</br>

**💎 Business Impact**</br>

The increase in false positives is an expected trade-off for achieving substantially higher recall.</br>
- Higher call centre workload</br>
- Increased marketing costs</br>
- Lower campaign efficiency</br>
- More customers contacted unnecessarily</br>

---

**💡 Key Takeaways**

- Improved recall from 21% to 62%, identifying nearly three times more potential subscribers.
- Reduced false negatives by 52% (733 to 350), substantially lowering missed sales opportunities.
- Increased true positives from 195 to 578, enabling the bank to target significantly more customers likely to subscribe.
- Traded higher precision and overall accuracy for improved campaign effectiveness, resulting in more false positives and increased marketing costs.
- Selected the Balanced Logistic Regression model because maximizing customer acquisition aligns more closely with the bank's marketing objectives than minimizing operational costs.

</details>

---

<details>
<summary><b>📋 MODEL SUMMARY</b></summary></br>

**📋 MODEL SUMMARY**</br>

**A. 📏 Standard Logistic Regression**</br>

**💪 Strengths**</br>
- Highest overall accuracy of **90%**</br>
- Higher precision **61%**, meaning fewer customers are contacted unnecessarily</br>
- Very low number of false positives of **125**, improving operational efficiency</br>

**⚠️ Limitations**</br>
- Very poor recall (21%)</br>
- Missed 733 actual subscribers</br>
- Only identified 195 customers who eventually subscribed</br>

**💎 Business Impact**</br>
The model performs well at *identifying customers who are unlikely to subscribe* but fails to identify many customers who would have responded positively. This reduces campaign effectiveness and results in lost sales opportunities.</br>

**B. ⚖️ Balanced Logistic Regression**</br>

**💪 Strengths**</br>
- Recall improved from **21% → 62%**
- Identified **578** actual subscribers (almost three times more)
- Reduced false negatives from **733 → 350**
- Better overall F1-score (0.42)

**⚠️ Limitations**</br>
- Accuracy decreased to 80%
- Precision dropped to 31%
- False positives increased substantially (125 → 1,277)

**💎 Business Impact**</br>
The model contacts more customers who ultimately do not subscribe but *captures significantly more potential subscribers*, making it better suited for customer acquisition campaigns.

| Metric        | 📏 Standard Logistic Regression   | ⚖️ Balanced Logistic Regression   | 
| --------------| ----------------------------------| ----------------------------------| 
| Accuracy      | **90%**                           | 80%                               |
| Recall        | 21%                               | **62%**                           |
| Precision     | **61%**                           | 31%                               |
| Limitation    | Missed 733 actual subscribers     | Contacted 1,277 non-subscribers   |
| Best For      | Reducing Marketing Cost           | Maximizing Customer Acquisition   |

---