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

**Business Context**</br>
A Portuguese bank launched a **direct marketing campaign to promote term deposit products** through outbound telephone calls. While these campaigns generated customer responses, the overall subscription rate remained low, making it difficult to efficiently identify customers most likely to purchase the product.</br>

Exploratory Data Analysis (EDA) revealed that customer subscription behaviour was influenced by a combination of **demographic characteristics, previous campaign interactions, communication channels, campaign timing, and macroeconomic conditions,** suggesting that predictive analytics could improve future campaign targeting.</br>

**Business Problem**</br>

Only **11% of customers** subscribed to the term deposit, resulting in a highly imbalanced dataset where the majority of customers declined the offer.</br>

Without predictive analytics, **marketing teams face several challenges:**</br>
- Contact many customers who are unlikely to subscribe, increasing operational costs.</br>
- Miss high-potential customers who are more likely to respond positively.</br>
- Apply broad marketing strategies instead of targeted customer segmentation.</br>
- Underutilise valuable customer behavioural and campaign history data.</br>
- Reduce campaign efficiency and overall return on marketing investment.</br>

---

**Business Objective**</br>

Develop a machine learning classification model that **predicts a customer's likelihood of subscribing to a term deposit**, enabling the bank to deliver more targeted, efficient, and data-driven marketing campaigns.</br>

The project aims to:</br>
- Identify the customer, campaign, and economic factors most strongly associated with successful subscriptions.</br>
- Evaluate how customer demographics, engagement history, communication methods, campaign timing, and macroeconomic indicators influence purchasing behaviour.</br>
- Compare baseline and balanced Logistic Regression models to address class imbalance and improve prediction performance.</br>
- Recommend the most suitable predictive model based on business objectives rather than overall accuracy alone.</br>
- Translate analytical findings into actionable marketing strategies that improve customer acquisition while optimising campaign resources.</br>

**💼 Business Value**</br>

The insights generated from this analysis enable the bank to:</br>
- **Improve customer targeting** by focusing on high-probability subscribers</br>
- **Reduce missed sales opportunities** through more effective predictive modelling</br>
- **Optimise campaign timing and communication channels** based on historical performance</br>
- **Support personalised marketing** using customer demographics and behavioural insights</br>
- Make more **informed, data-driven marketing decisions** that maximise campaign effectiveness and return on investment</br>

</details>

---

<details open>
<summary><b>🔍 EXPLORATORY DATA ANALYSIS & FEATURE ENGINEERING</b></summary></br>

**Exploratory Data Analysis**</br>

Exploratory Data Analysis (EDA) was conducted to understand customer subscription behaviour, identify meaningful relationships between variables, and select the most relevant features for predictive modelling. Both numerical and categorical variables were analysed to uncover behavioural patterns, evaluate data quality, and guide feature engineering.</br>

The analysis explored:</br>
- Customer demographics (age, education, occupation, marital status)</br>
- Previous campaign interactions and customer engagement history</br>
- Marketing campaign characteristics (contact method, month, number of contacts)</br>
- Economic indicators (Euribor rate and Consumer Confidence Index)</br>
- Relationships between customer attributes and term deposit subscription outcomes</br>
- Class imbalance between subscribers ("Yes") and non-subscribers ("No")</br>

Insights from the EDA informed the feature selection process and the development of both Logistic Regression models.</br>

---

**Data Preparation & Feature Engineering**</br>
To improve model performance and ensure the data was suitable for machine learning, several preprocessing and feature engineering techniques were applied.</br>

| Transformation                | Summary           |
|-------------------------------|-------------------|
| **Missing Value Handling**    | **Unknown and missing categorical values were reviewed** and retained or grouped where appropriate to preserve potentially meaningful customer information rather than discarding observations.   |
| **Feature Selection**         | Numerical and categorical variables were evaluated using exploratory analysis to **identify the strongest predictors of customer subscription** while removing less informative attributes.   |
| **Feature Grouping**          | Categories with **similar business meaning were consolidated** to simplify the feature space, reduce sparsity, and improve model interpretability.    |
| **Age Segmentation**          | Continuous age values were **grouped into meaningful age bands** to better capture behavioural differences across customer life stages observed during EDA.   |
| **Campaign Grouping**         | Campaign-related numerical variables, such as the number of contacts, were **grouped into business-friendly categories** to reduce skewness and better represent customer engagement levels.  |
| **Categorical Encoding**      | **One-hot encoding** was applied to categorical variables, converting them into numerical features suitable for Logistic Regression while preserving all category information.    |
| **Feature Scaling**           | Numerical variables were **standardised** to ensure comparable feature magnitudes, improving model stability and optimisation during Logistic Regression training.    |
| **Train-Test Split**          | The dataset was split into training and testing sets **using stratified sampling** to preserve the original class distribution (89% No, 11% Yes), ensuring fair and representative model evaluation.  |

---

**Selected Predictive Features**</br>

The final feature set was selected based on business relevance, behavioural patterns identified during EDA, reduced redundancy, and predictive value.</br>

**Customer Demographics**</br>
- Age Group</br>
- Job</br>
- Education</br>
- Marital Status</br>

**Customer Engagement History**</br>
- Previous Campaign Outcome (poutcome)</br>
- Previous Contacts (previous)</br>
- Previously Contacted</br>

**Campaign Characteristics**</br>
- Contact Method</br>
- Campaign Month</br>
- Campaign Contact Group</br>

**Economic Indicators**</br>
- Euribor 3-Month Rate</br>
- Consumer Confidence Index</br>

Together, these features capture customer demographics, historical engagement, campaign execution, and economic conditions that influence the likelihood of term deposit subscription.</br>

---

**Key Outcomes from EDA**</br>

The exploratory analysis revealed several patterns that directly influenced feature engineering and model development:</br>

- Previous campaign success was the strongest behavioural indicator of future subscription</br>
- Customer response varied across demographic groups, highlighting the importance of customer segmentation</br>
- Communication channel and campaign timing significantly influenced conversion rates</br>
- Economic indicators showed meaningful relationships with customer purchasing behaviour</br>
- The target variable was highly imbalanced (89% non-subscribers vs. 11% subscribers), motivating the development of a Balanced Logistic Regression model</br>

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
<summary><b>🤖 PREDICTIVE MODELING</b></summary></br>

| Modelling Workflow |
|------|
| 🧠 Business Problem </br> 📥 Data Preparation </br> 🔍 Feature Selection </br> 📏 Model 1: Standard Logistic Regression </br>❓Performance Evaluation </br> 🤔 Class Imbalance Identified </br> ⚖️ Model 2: Balanced Logistic Regression </br> ☯️ Model Comparison </br> 💡Business Recommendation |


**📏 Model 1: Standard Logistic Regression**</br>
**Purpose:** Establish a baseline classification model using the original dataset.</br>

**Approach:**</br>
- Trained using the original class distribution.</br>
- Assumes all observations have equal importance.</br>
- Serves as the benchmark for evaluating model improvements.</br>

**Evaluation Metrics:**</br>
- Accuracy</br>
- Precision</br>
- Recall</br>
- F1 Score</br>
- Confusion Matrix</br>

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
**Evaluation Metrics:**</br>
- Accuracy</br>
- Precision</br>
- Recall</br>
- F1 Score</br>
- Confusion Matrix</br>

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

---

**🏆 Best Performing Model**</br>

**<font color="green">⚖️ Balanced Logistic Regression**</font></br>

Despite a reduction in overall **accuracy (80%)** and **precision (31%)**, the Balanced Logistic Regression model delivered significantly stronger business value by **identifying nearly three times more potential subscribers** and r**educing missed opportunities by over 50%**.</br>

For customer acquisition campaigns, missing a potential subscriber is generally more costly than contacting a customer who ultimately does not subscribe. Therefore, the Balanced Logistic Regression model provides a more practical and effective solution for supporting targeted marketing decisions.</br>

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

**1. Previous Customer Engagement is the Strongest Predictor**</br>

Customers who previously subscribed to a campaign were significantly more likely to subscribe again. Likewise, customers with prior campaign interactions demonstrated higher conversion potential than first-time contacts.</br>

**💎 Business Impact**</br>

- Previous campaign outcome is the most influential predictive feature.</br>
- Existing customer engagement history provides valuable targeting opportunities.</br>

**2. Campaign Execution Significantly Influences Success**</br>

Campaign timing and communication channel had a measurable impact on subscription rates. Cellular contact consistently outperformed telephone outreach, while certain campaign months achieved higher response rates.</br>

**💎 Business Impact**</br>

- Optimising campaign timing can improve marketing effectiveness.</br>
- Prioritising higher-performing communication channels can increase conversion while improving resource utilisation.</br>


**3. Customer Demographics Influence Subscription Behaviour**</br>

Subscription rates varied across demographic segments. Retirees and students demonstrated stronger response rates, whereas blue-collar occupations and younger age groups generally showed lower conversion rates.</br>

Education level and marital status also exhibited meaningful behavioural differences.</br>

**💎 Business Impact**</br>

- Demographic segmentation enables more personalised and effective marketing campaigns.</br>
- Tailored messaging can improve customer engagement across different customer groups.</br>

**4. Economic Conditions Affect Customer Decisions**</br>

Macroeconomic indicators—including Euribor rates and the Consumer Confidence Index—showed meaningful relationships with subscription behaviour, indicating that external economic conditions influence customers' willingness to invest.</br>

**💎 Business Impact**</br>

- Marketing strategies should consider prevailing economic conditions.</br>
- Campaign planning can be adjusted according to market sentiment and customer confidence.</br>

**5. Balancing Business Cost and Sales Opportunity**</br>
The standard Logistic Regression model achieved higher overall accuracy (90%) but identified only 21% of actual subscribers.
After applying class balancing, recall increased to 62%, enabling the model to identify nearly three times more potential subscribers while reducing missed opportunities by over 50%.</br>

**💎 Business Impact**</br>

- The balanced model supports customer acquisition objectives.</br>
- The increase in marketing effort is justified by substantially improved sales opportunity identification.</br>

</details>

---

<details open>
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

**💰 Business Trade-Off**</br>

The two models optimize different business objectives.</br>

| Model                         | Business Goal                     | 
| ----------------------------- | ----------------------------------| 
| Standard Logistic Regression  | Reduce marketing costs            |
| Balanced Logistic Regression  | Maximize customer acquisition     |

For this project, the **Balanced Logistic Regression** is the preferred model because the primary objective is to **increase successful term deposit subscriptions**.</br>

Accepting additional marketing effort is justified by the substantial reduction in missed sales opportunities and the significant increase in correctly identified potential subscribers.</br>

---

**💡 Key Takeaways**

- Improved recall from 21% to 62%, identifying nearly three times more potential subscribers.
- Reduced false negatives by 52% (733 to 350), substantially lowering missed sales opportunities.
- Increased true positives from 195 to 578, enabling the bank to target significantly more customers likely to subscribe.
- Traded higher precision and overall accuracy for improved campaign effectiveness, resulting in more false positives and increased marketing costs.
- Selected the Balanced Logistic Regression model because maximizing customer acquisition aligns more closely with the bank's marketing objectives than minimizing operational costs.

</details>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

**1. Prioritise High-Probability Customer Segments**</br>

Develop targeted marketing lists using customers who:</br>
- Previously subscribed to campaigns (poutcome)</br>
- Have prior campaign engagement (previous)</br>
- Belong to high-converting demographic segments such as retirees and students</br>

**⬆️ Expected Benefit**</br>
- Higher conversion rates with improved marketing efficiency.</br>

**2. Optimise Campaign Strategy**</br>

Increase the use of high-performing communication channels and schedule campaigns during periods associated with stronger historical response rates.</br>
Focus on:</br>
- Cellular contact</br>
- High-performing campaign months</br>
- Customers requiring fewer contact attempts</br>

**⬆️ Expected Benefit**</br>
- Improved campaign effectiveness while reducing unnecessary operational effort.</br>

**3. Personalise Marketing by Customer Segment**</br>
Design tailored marketing messages based on customer characteristics, including:</br>
- Age group</br>
- Occupation</br>
- Education level</br>
- Marital status</br>
 
Different customer groups exhibit distinct subscription behaviours and should not receive identical marketing approaches.</br>

**⬆️ Expected Benefit**</br>
More relevant customer experiences and improved response rates.</br>

**4. Incorporate Economic Indicators into Campaign Planning**</br>
Use these macroeconomic variables to inform campaign scheduling and customer targeting strategies:</br>
- Euribor 3-Month Rate</br>
- Consumer Confidence Index</br>

**⬆️ Expected Benefit**</br>
Marketing decisions become more aligned with customer purchasing behaviour during different economic conditions.</br>

**5. Deploy the Balanced Logistic Regression Model**</br>

Although the Balanced Logistic Regression model generated more false positives, it substantially reduced false negatives and identified significantly more potential subscribers.</br>
This trade-off aligns with the bank's objective of maximising customer acquisition and term deposit subscriptions.</br>

**⬆️ Expected Benefit**</br>
- 52% fewer missed sales opportunities</br>
- Nearly three times more correctly identified subscribers</br>
- Greater overall campaign effectiveness</br>

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

**1. 🌲 Evaluate Advanced Machine Learning Models**</br>

Evaluate tree-based classification models such as Random Forest, XGBoost, and Gradient Boosting to compare predictive performance against Logistic Regression and identify the best-performing model.</br>

**Why it matters:**</br>

May improve Recall, F1 Score, and overall predictive performance by capturing complex, non-linear relationships.</br>

**2. 🔍 Improve Model Explainability with SHAP**</br>

Apply SHAP (SHapley Additive exPlanations) to explain how individual features influence prediction outcomes and improve model transparency.</br>

**Why it matters:**</br>

Provides interpretable insights into customer behaviour, helping business stakeholders understand the key drivers of subscription decisions.</br>

**3. 🌐 Deploy an Interactive Streamlit Application**</br>

Deploy the final predictive model as an interactive Streamlit web application, allowing users to input customer attributes and receive real-time subscription predictions.</br>

**Why it matters:**</br>

Demonstrates the practical application of machine learning by transforming a notebook into an accessible decision-support tool.</br>

</details>

---

**🤝 Let's Connect!**</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

</details>