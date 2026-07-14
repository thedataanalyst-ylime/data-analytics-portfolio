### 📈 Bank Marketing Campaign Analytics
#### **💰Predicting High-Potential Customers using Machine Learning**</br>

<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

🎯 Developed an end-to-end machine learning solution that **identified customers most likely to subscribe to term deposits**, enabling more targeted marketing and improving campaign effectiveness.</br>

🔍 Performed Exploratory Data Analysis (EDA) and feature engineering to **identify the customer, campaign, and economic factors influencing subscription behaviour**.</br>

🤖 Built and evaluated **Standard and Balanced Logistic Regression models** using Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.</br>

🏆 Selected the **Balanced Logistic Regression model**, improving Recall from 21% to 62% and reducing missed subscribers by over 50%.</br>

💡 Delivered **actionable recommendations** to improve customer targeting, campaign ROI, and subscription rates.</br>

</details>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>

Financial institutions rely on direct marketing campaigns to promote term deposit products, but low subscription rates make customer targeting challenging.</br>

This project applies EDA and machine learning to **identify the strongest drivers of customer subscription and predict high-potential customers.**.</br>

---

| Category | Details |
|------|--------|
| **Analytics Capabilities** | 🧠 Business Analysis </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering</br> 🤖 Machine Learning </br> 📝 Model Evaluation </br> 💡 Recommendations</br> 📊 Data Storytelling</br> |
| **Technology Stack** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) • ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) • ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) • ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) • ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square&logo=python&logoColor=white) • ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikitlearn&logoColor=white) |
| **Models Evaluated** | Standard Logistic Regression • Balanced Logistic Regression |
| **Business Outcome** | Improved Recall from 21% → 62%, 3× more subscribers identified  |
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

The selected Balanced Logistic Regression model delivered measurable business value by:</br>
- Identifying **nearly 3× more **potential subscribers</br>
- Reducing missed sales opportunities by **over 50%**</br>
- Improving **Recall from 21% to 62%**</br>
- Supporting transparent and **data-driven marketing decisions**</br>

**🥡 Business Takeaway**</br>

For customer acquisition campaigns, **identifying more potential subscribers creates greater business value than maximising overall prediction accuracy.** The Balanced Logistic Regression model therefore provides a better balance between marketing efficiency and revenue opportunity.</br>

</details>

---

<details open>
<summary><b>🔍 EXPLORATORY DATA ANALYSIS & FEATURE ENGINEERING</b></summary></br>

**🔍 Exploratory Data Analysis (EDA)**</br>

EDA was conducted to understand customer subscription behaviour, identify meaningful relationships between variables, and select the most relevant features for predictive modelling. Numerical and categorical variables were analysed to uncover behavioural patterns, evaluate data quality, and guide feature engineering.</br>

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
| **One-Hot Encoding**                  | Converted categories into model-ready variables   | Enables machine learning models      |
| **Feature Scaling**                   | Standardised numerical variables  | Improves model stability      |
| **Stratified Split**                  | Preserved the original class distribution (89%-No, 11%-Yes)   | Ensures reliable model evaluation |

---

**📝 Selected Predictive Features**</br>

The final model combined customer profile, campaign history, current campaign details and economic conditions..</br>

| Customer Profile      | Campaign History      | Current Campaign      | Economic Conditions   |  
|---------------------- | --------------------- | ----------------------------- | --------------------- |
| • Age Group</br> • Job</br> • Education</br> • Marital Status</br> | • Previous Campaign Outcome</br> • Previous Contacts</br> • Previously Contacted</br> </br> | • Contact Method</br> • Campaign Month</br> • Campaign Contact Group</br> </br>| • Euribor 3-Month Rate</br> • Consumer Confidence Index</br> </br></br>  | 

---

<details open>
<summary><b>🤖 PREDICTIVE MODELING</b></summary></br>

| Modelling Workflow    | Evaluation Metrics    |
|-----------------------| ----------------------|
| 🧠 Business Problem </br> 🔍 Exploratory Data Analysis </br> 💻 Feature Engineering </br> 📏 Model 1: Standard Logistic Regression </br> 🤔 Class Imbalance Identified </br> ⚖️ Model 2: Balanced Logistic Regression </br> ☯️ Model Comparison </br> 💡Business Recommendation | 🎯 Accuracy</br> 🔍 Precision</br> ✅ Recall</br> 🏎️ F1 Score</br> 🔢 Confusion Matrix</br> </br> </br> </br>  | 

Two Logistic Regression models were evaluated to determine the optimal balance between identifying potential subscribers and minimising unnecessary customer contacts.

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

**🏆 Best Performing Model**

**⚖️ Balanced Logistic Regression**

Despite a reduction in overall accuracy (80%) and precision (31%), the Balanced Logistic Regression model delivered significantly stronger business value by **identifying nearly three times more potential subscribers** and **reducing missed opportunities by over 50%**.</br>

For customer acquisition campaigns, missing a potential subscriber is generally more costly than contacting a customer who ultimately does not subscribe. 

Therefore, the Balanced Logistic Regression model provides a more practical and effective solution for supporting targeted marketing decisions.</br>

---

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

**Abbreviations:** TP = True Positive • FN = False Negative • FP = False Positive • TN = True Negative</br>

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

1. **Improving Recall from 21% to 62%** substantially reduced missed sales opportunities.</br>
   
2. **Previous campaign success** was the strongest predictor of future subscription.</br>

3. Customers contacted via **cellular channels** consistently achieved higher subscription rates than telephone campaigns.</br>

4. **Retirees and students** responded more positively than other customer groups.</br>

5. **Macroeconomic conditions such as consumer confidence and interest rates** influenced subscription behaviour.</br>

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

**1. 🌲 Evaluate Random Forest, XGBoost and Gradient Boosting.**</br>

Compare predictive performance against Logistic Regression and identify the best-performing model.</br>

**Why it matters:** Improve Recall, F1 Score, and overall predictive performance by capturing complex, non-linear relationships.</br>

**2. 🔍 Apply SHAP (SHapley Additive exPlanations) for model explainability.**</br>

Explains how individual features influence prediction outcomes and improve model transparency.</br>

**Why it matters:** Understand the key drivers of subscription decisions.</br>

**3. 🌐 Deploy an Interactive Streamlit Application**</br>

Allow users to input customer attributes and receive real-time subscription predictions.</br>

**Why it matters:** A practical application of machine learning for users by having an accessible decision-support tool.</br>

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
| TP              | Model correctly predicted that customer WILL subscribe</br>     |
| FN              | Model predicted customer will NOT subscribe BUT actual result customer WOULD HAVE subscribed</br>  The bank failed to identify a customer who was ACTUALLY LIKELY to subscribe. The bank may not contact them, miss potential revenue and lose conversion opportunities.</br>      |
| FP              | Model predicted that customer WILL subscribe BUT actual result customer did NOT subscribe</br> The bank targeted a customer expecting them to subscribe, but the customer ultimately DID NOT subscribe.</br>       |
| TN              | Model correctly predicted that customer will NOT subscribe</br>     |
| Confusion Matrix      | Shows the number of correct and incorrect predictions, providing insight into business trade-offs such as missed subscribers and unnecessary customer contacts.</br>      |

**Abbreviations:** TP = True Positive • FN = False Negative • FP = False Positive • TN = True Negative</br>

</details>

---

<details>
<summary><b>🗂 DATASET</b></summary></br>

| Attribute         | Value                                         |
|-------------------|-----------------------------------------------|
| Source            | Portuguese Bank Marketing Dataset             |
| Description       | Campaign results for a term deposit product   |
| Link              | [View Dataset](data/6.18_bank.csv.zip)        |
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

⭐ View More Analytics Projects</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

</details>