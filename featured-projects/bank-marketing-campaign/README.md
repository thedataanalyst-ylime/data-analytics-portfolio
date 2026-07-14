### 📈 Bank Marketing Campaign Response Prediction
#### **💰Predicting High-Potential Bank Customers for Targeted Marketing**</br>
**Using Logistic Regression Classification on the Portuguese Bank Marketing Dataset**</br>

<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

🎯 Developed an end-to-end machine learning solution that **identified customers most likely to subscribe to term deposits**, enabling more targeted marketing and improving campaign effectiveness.</br>

🔍 Performed Exploratory Data Analysis (EDA) and feature engineering to **identify the customer, campaign, and economic factors influencing subscription behaviour**.</br>

🤖 Built and evaluated **Standard and Balanced Logistic Regression models** using Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.</br>

🏆 Selected the **Balanced Logistic Regression model**, improving Recall from 21% to 62% and reducing missed subscribers by over 50%.</br>

💡 Delivered **actionable marketing recommendations** to improve customer targeting, campaign effectiveness, and subscription rates.</br>

</details>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>

Financial institutions rely on direct marketing campaigns to promote term deposit products, but low subscription rates make customer targeting challenging.</br>

This project applies EDA and machine learning to **identify the key factors influencing customer subscriptions and predict high-potential customers for more effective marketing campaigns**.</br>

---

| Category | Details |
|------|--------|
| **Analytics Capabilities** | 🧠 Business Analysis </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering</br> 🤖 Machine Learning </br> 📝 Model Evaluation </br> 💡 Recommendations</br> 📊 Data Storytelling</br> |
| **Technology Stack** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) • ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) • ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) • ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) • ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square&logo=python&logoColor=white) • ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) |
| **Models Evaluated** | Standard Logistic Regression • Balanced Logistic Regression |
| **Project Artefacts** | 📓 [Jupyter Notebook](notebooks/bank-marketing-campaign-notebook.ipynb) |

</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM AND BUSINESS VALUE</b></summary></br>

**💼 Business Problem**</br>

Only **11% of customers** subscribed to the term deposit, making it difficult for the bank to identify high-potential customers and optimise marketing spend.</br>

Without predictive analytics, the bank risks:</br>
- Contacting customers unlikely to subscribe</br>
- Missing revenue opportunities from high-potential customers</br>
- Increasing marketing costs and reducing campaign ROI</br>

---

**💎 Business Value**</br>

By developing a machine learning model, the bank is able to:</br>

- Reduce missed sales opportunities by **over 50%**</br>
- Identify nearly **3× more** potential subscribers</br>
- Improve Recall **from 21% to 62%**</br>
- Deliver an interpretable model to support **data-driven marketing decisions**</br>

**🥡 Business Takeaway**</br>
For customer acquisition campaigns, prioritising Recall over Accuracy **enables the bank to identify substantially more potential subscribers**, where missing a customer is more costly than contacting one who ultimately declines.</br>

</details>

---

<details open>
<summary><b>🔍 EXPLORATORY DATA ANALYSIS & FEATURE ENGINEERING</b></summary></br>

**🔍 Exploratory Data Analysis (EDA)**</br>

EDA was conducted to understand customer subscription behaviour, identify meaningful relationships between variables, and select the most relevant features for predictive modelling. Both numerical and categorical variables were analysed to uncover behavioural patterns, evaluate data quality, and guide feature engineering.</br>

The analysis explored:</br>
- **Customer demographics** (age, education, occupation, marital status)</br>
- Previous campaign interactions and customer engagement history</br>
- **Marketing campaign characteristics** (contact method, month, number of contacts)</br>
- **Economic indicators** (Euribor rate and Consumer Confidence Index)</br>
- Relationships between customer attributes and term deposit subscription outcomes</br>
- **Class imbalance** between subscribers ("Yes") and non-subscribers ("No")</br>

Insights from the EDA informed the feature selection process and the development of both Logistic Regression models.</br>

---

**📥 Data Preparation & Feature Engineering**</br>
To improve model performance and ensure the data was suitable for machine learning, several pre-processing and feature engineering techniques were applied.</br>

| Transformation                        | Purpose           | Business Value        |
|---------------------------------------|-------------------| ----------------------|
| **Missing Value Handling**            | Preserved meaningful customer information | Preserves data integrity |
| **Feature Selection**                 | Identify the strongest predictors of customer subscription    | Improves prediction accuracy  |
| **Age Segmentation**                  | Created meaningful age bands  | Improves customer targeting       |
| **Campaign Grouping**                 | Grouped contact frequency into business-friendly bands    | Simplifies marketing analysis        |
| **One-Hot Encoding**                  | Converted categories into model-ready variables   | Enables model training      |
| **Feature Scaling**                   | Standardised numerical variables  | Improves model stability      |
| **Stratified Split**                  | Preserved the original class distribution (89%-No, 11%-Yes)   | Ensures reliable model evaluation |

---

**📝 Selected Predictive Features**</br>

The final model combined customer profile, campaign history, current campaign details and economic conditions..</br>

| Customer Profile      | Campaign History      | Campaign Characteristics      | Economic Conditions   |  
|---------------------- | --------------------- | ----------------------------- | --------------------- |
| • Age Group</br> • Job</br> • Education</br> • Marital Status</br> | • Previous Campaign Outcome</br> • Previous Contacts</br> • Previously Contacted</br> </br> | • Contact Method</br> • Campaign Month</br> • Campaign Contact Group</br> </br>| • Euribor 3-Month Rate</br> • Consumer Confidence Index</br> </br></br>  | 

---

<details open>
<summary><b>🤖 PREDICTIVE MODELING</b></summary></br>

| Modelling Workflow    | Evaluation Metrics    |
|-----------------------| ----------------------|
| 🧠 Business Problem </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering </br> 📏 Model 1: Standard Logistic Regression </br> 🤔 Class Imbalance Identified </br> ⚖️ Model 2: Balanced Logistic Regression </br> ☯️ Model Comparison </br> 💡Business Recommendation | 🎯 Accuracy</br> 🔍 Precision</br> ✅ Recall</br> 🏎️ F1 Score</br> 🔢 Confusion Matrix</br> </br> </br> </br>  | 

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

| Metric                | Standard LR  | Balanced LR  | Better Model? | Business Value               |
| --------------------- | ----------------------------- | ----------------------------- | ------------- | ------------------------------|
| Accuracy              | **90%**                       | 80%                           | Standard      | ⬆️ Higher overall prediction accuracy       | 
| Precision             | **61%**                       | 31%                           | Standard      | ⬇️ Fewer unnecessary customer contacts      |
| Recall                | 21%                           | **62%**                       | Balanced      | ⬆️ Identified 3× more actual subscribers   |
| F1 Score              | 0.31                          | **0.42**                      | Balanced      | ⚖️ Better balance of Precision & Recall   |
| TP   | 195                           | **578**                       | Balanced      | ⬆️ More successful subscriber identification   |      
| FN  | 733                           | **350**                       | Balanced      | ⬇️ Reduced missed sales opportunities by 52%  |
| FP  | **125**                       | 1,277                         | Standard      | ⬇️ Lower marketing cost and effort  |
| TN   | **7,185**                     | 6,033                         | Standard      | ⬆️ Correctly ruled out unlikely subscribers   |

**Abbreviations:** TP = True Positive • FP = False Positive • TN = True Negative • FN = False Negative</br>

---

**🏆 Best Performing Model**

**⚖️ Balanced Logistic Regression**

Despite a reduction in overall accuracy (80%) and precision (31%), the Balanced Logistic Regression model delivered significantly stronger business value by **identifying nearly three times more potential subscribers** and **reducing missed opportunities by over 50%**.</br>

For customer acquisition campaigns, missing a potential subscriber is generally more costly than contacting a customer who ultimately does not subscribe. 

Therefore, the Balanced Logistic Regression model provides a more practical and effective solution for supporting targeted marketing decisions.</br>

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

1. **Improving Recall from 21% to 62%** substantially reduced missed sales opportunities.</br>
   
2. **Previous campaign success** was the strongest predictor of future subscription.</br>

3. Customers contacted via **cellular channels** consistently achieved higher subscription rates than telephone campaigns.</br>

4. **Retirees and students** responded more positively than other customer groups.</br>

5. **Consumer confidence and interest rates** influenced subscription behaviour.</br>

</details>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

1. Deploy the **Balanced Logistic Regression model** for more effective marketing campaigns.</br>
   
2. Prioritise customers with **successful previous campaign responses**.</br>

3. Increase investment in **cellular campaigns** and **schedule campaigns during peak months** such as March, October, September, and December.</br> 

4. Personalise marketing **by customer segment**.</br>

5.  Incorporate **economic indicators** into campaign planning.</br>

</details>

---

<details open>
<summary><b>✨ FUTURE ENHANCEMENTS</b></summary></br>

**1. 🌐 Deploy an Interactive Streamlit Application**</br>

Allow users to input customer attributes and receive real-time subscription predictions.</br>

**Why it matters:** A practical application of machine learning for users by having an accessible decision-support tool.</br>

**2. 🔍 Apply SHAP (SHapley Additive exPlanations) for model explainability.**</br>

Explains how individual features influence prediction outcomes and improve model transparency.</br>

**Why it matters:** Understand the key drivers of subscription decisions.</br>

**3. 🌲 Evaluate Random Forest, XGBoost and Gradient Boosting.**</br>

Compare predictive performance against Logistic Regression and identify the best-performing model.</br>

**Why it matters:** Improve Recall, F1 Score, and overall predictive performance by capturing complex, non-linear relationships.</br>

</details>

---

<details>
<summary><b>📝 DEFINITION OF TERMS</b></summary></br>

| Term                  | Definition                    | 
| --------------------- | ----------------------------- |
| Accuracy              | The percentage of **all predictions the model got correct**, whether the customer subscribed or not.</br>     |
| Precision              | Of all customers the model predicted **would subscribe**, how many actually did. A higher precision means fewer unnecessary marketing calls.</br>        |
| Recall              | Of all customers who actually subscribed, how many did the model successfully identified. **A higher recall means fewer missed sales opportunities.**</br>      |
| F1 Score              | A single measure that balances **Precision** and **Recall**, showing how well the model identifies subscribers while minimizing incorrect predictions.</br>       |
| True Negative (TN)              | Model correctly predicted that customer will NOT subscribe</br>     |
| True Positive (TP)              | Model correctly predicted that customer WILL subscribe</br>     |
| False Positive (FP)              | Model predicted that customer WILL subscribe BUT actual result customer did NOT subscribe</br> The bank targeted a customer expecting them to subscribe, but the customer ultimately DID NOT subscribe.</br>       |
| False Negative (FN)              | Model predicted customer will NOT subscribe BUT actual result customer WOULD HAVE subscribed</br>  The bank failed to identify a customer who was ACTUALLY LIKELY to subscribe. The bank may not contact them, miss potential revenue and lose conversion opportunities.</br>      |
| Confusion Matrix      | Shows the number of correct and incorrect predictions, providing insight into business trade-offs such as missed subscribers and unnecessary customer contacts.</br>      |

</details>

---

<details>
<summary><b>🗂 DATASET</b></summary></br>

| Attribute         | Value                                         |
|-------------------|-----------------------------------------------|
| Source            | Portuguese Bank Marketing Dataset             |
| Description       | Campaign results for a term deposit product   |
| Link              | [View Dataset](data/6.18_bank.csv)            |
| No. of Records    | 41,188                                        |
| Target Variable   | Subscription (Yes/No)                         |
| Features          | 20+                                           |
| Problem Type      | Binary Classification                         |

</details>

---

<details>
<summary><b>🗂️ REPOSITORY STRUCTURE</b></summary></br>

| Folder        | Description                |
| ------------- | -------------------------- |
| 📁 charts     | Exploratory Visualisations |
| 📁 data       | Raw Dataset               |
| 📁 notebooks  | End-to-end Python analysis |

</details>

---

**🤝 Let's Connect!**</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

</details>