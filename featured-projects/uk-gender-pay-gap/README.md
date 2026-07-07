### 🇬🇧👩👱🏻‍♂️ UK Gender Pay Gap Analysis
**<font color="teal">SQL | Data Storytelling | Business Intelligence | Workforce Analytics** </font>

A business intelligence project analysing gender pay disparities across more than 10,000 UK employers to uncover workforce representation patterns and identify opportunities for greater pay equity.

<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

🇬🇧 Analysed the UK Government Gender Pay Gap dataset covering over **10,000 employers** across multiple industries</br>
📈 End-to-end **SQL analytics workflow** from data exploration and analysis</br>
💡 Proposed recommendations for the UK government for improvements in both data collection and organisational practices to better understand and address the gender pay gap </br>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>


| Category | Details |
|------|--------|
| **Analytics Capabilities** | 🧠 Business Analysis </br> 🔍 Exploratory SQL Analysis </br> 📈 Business Insights </br> 📊 Data Storytelling </br> 💡 Recommendations</br>|
| **Technology Stack** | ![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=sqlite&logoColor=white) • ![Canva](https://img.shields.io/badge/Canva-00C4CC?style=flat&logo=canva&logoColor=white) • ![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=flat&logo=microsoftpowerpoint&logoColor=white)  |
| **Project Artefacts** | 🔍 [SQL Analysis](sql/UK_Gender_Pay_Gap_Analysis_SQL.pdf) </br> 📄 [Technical Report](report/UK_Gender_Pay_Gap_Analysis_Report.pdf) </br> 🎤 [Presentation Slides](presentation/UK_Gender_Pay_Gap_Analysis_Presentation.pdf) </br>|


</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM AND IMPACT</b></summary></br>

**Business Problem**</br>

Many organisations monitor gender pay gaps, but identifying where inequality exists and what organisational characteristics contribute to it remains challenging.</br>

Using publicly available UK reporting data, this project investigates:</br>
- Which industries experience the largest gender pay gaps?</br>
- Does organisation size influence pay inequality?</br>
- How does workforce representation affect pay gaps?</br>
- What patterns exist across bonus payments?</br>
- Which organisations appear to be outliers?</br>

---

**Business Impact**</br>

Understanding gender pay inequality enables organisations to:</br>
- Improve workforce planning</br>
- Strengthen diversity initiatives</br>
- Support ESG reporting</br>
- Improve transparency</br>
- Identify structural pay disparities</br>

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

**On average, women earn approximately 10% less than men across organisations.**

The distribution of the gender pay gap across companies is wide and skewed with most companies clustered around the median of approximately 10% but with a number of companies with extreme high pay gaps.

![Chart1](charts/01_distribution_of_pay_gap.png)


**The gender pay gap is primarily driven by differences in representation across roles and levels**, rather than unequal pay for the same work. Men are more likely to be represented in higher-paying roles.</br>


The Education sector is a female-dominated and Finance & Insurance is a high-paying sector both show notably higher pay gaps.</br>

![Chart4](charts/04_pay_gap_in_sectors.png)


**Gender pay gap is a widespread issue across all regions.**</br>
Pay differences are slightly more pronounced among London-based
organisations where the concentration of high-paying industries and roles,
and where men are more likely to be represented in senior positions.</br>

![Chart3](charts/03_pay_gap_across_regions.png)

**There is no strong relationship between company size and the gender pay gap,**
Suggesting that organisational scale alone does not explain the differences.</br>

![Chart2](charts/02_pay_gap_by_employer_size.png)


**Gender Pay Gap ≠ Unlawful Pay Discrimination**
Instead, it reflects broader structural factors such as the distribution of men and women across different roles and levels within organisations.</br>

</details>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

- Enhance data granularity to better understand drivers such as job roles and levels, career progression and promotions, and tenure and experience.</br>

- Improve consistency and clarity in reporting.</br>

- Capture more precise workforce measures such as actual employee counts.</br>

- Encourage organisations to address progression pathways.</br>

---

<details open>
<summary><b>⚠️ DATA LIMITATIONS & KEY CAVEATS </b></summary></br>

- Analysis is based on employer-level reporting rather than workforce-weighted
measures</br>

- Only includes full-pay relevant employees, excluding those on leave such as
such as maternity, paternity, sick, sabbatical, or other forms of leave</br>

- Does not include role-level or job-specific information</br>

- Data represents a single reporting period and does not allow for trend analysis
over time</br>

- Self-reported by employers</br>

- Region analysis is based on employer postal code</br>

- Inconsistent or multiple industry classifications (SIC codes)</br>

- Structural limitations in the dataset</br>

- Only companies with 250 or more employees are legally required to submit data, meaning the entire small-employer population is absent from this dataset

---

<details open>
<summary><b>🗂 DATASET</b></summary></br>

 Source | Description | Link |
|---------|-------------|-----|
| UK Government Gender Pay Gap Reporting Service | Annual employer-reported gender pay statistics | [View Data](data/gender_pay_gap_21_22.csv) |

Dataset includes:</br>
- Mean hourly pay gap</br>
- Median hourly pay gap</br>
- Bonus pay gap</br>
- Bonus participation</br>
- Workforce pay quartiles</br>
- Employer size</br>
- Industry classification</br>
- Reporting compliance</br>

</details>

---

<details open>
<summary><b>🗂️ REPOSITORY STRUCTURE</b></summary></br>

| Folder        | Description              |
| ------------- | ------------------------ |
| 📁 charts     | Visualisations |
| 📁 data       | Gender Pay Gap Dataset |
| 📁 sql  | End-to-end SQL analysis |
| 📁 report    | Technical Report | 
| 📁 presentation    | Presentation Slides |

</details>

---


⭐ **Thank you for exploring this project.**
This demonstrates how data analytics can transform datasets into meaningful insights and actionable recommendations. </br>

If you'd like to discuss data analytics, employee engagement, or opportunities to collaborate, I'd be happy to connect.
</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

---