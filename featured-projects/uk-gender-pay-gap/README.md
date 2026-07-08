### 🇬🇧👩👱🏻‍♂️ UK Gender Pay Gap Analysis
**<font color="teal">SQL | Data Storytelling | Business Intelligence | Workforce Analytics** </font>

A business intelligence project analysing gender pay disparities across more than 10,000 UK employers to uncover workforce representation patterns and identify opportunities for greater pay equity.

<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

🇬🇧 Analysed **10,174 UK employers** across multiple industries from the UK Government Gender Pay Gap dataset </br>

💷 Identified a **typical median pay gap of 9.8%**

👬 Found **workforce representation**, not organisation size, to be the strongest driver

💡 Produced **executive-ready recommendations** for government policy </br>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>


| Category | Details |
|------|--------|
| SQL Analytics Workflow | 🧠 Business Analysis </br> 🔍 Exploratory SQL Analysis </br> 📈 Business Insights </br> 📊 Data Storytelling </br> 💡 Recommendations</br>|
| Technology Stack | ![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=sqlite&logoColor=white) • ![Canva](https://img.shields.io/badge/Canva-00C4CC?style=flat&logo=canva&logoColor=white) • ![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=flat&logo=microsoftpowerpoint&logoColor=white)  |
| Project Artefacts | 🔍 [SQL Analysis](sql/UK_Gender_Pay_Gap_Analysis_SQL.pdf) </br> 📄 [Technical Report](report/UK_Gender_Pay_Gap_Analysis_Report.pdf) </br> 🎤 [Presentation Slides](presentation/UK_Gender_Pay_Gap_Analysis_Presentation.pdf) </br>|


</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM AND BUSINESS VALUE</b></summary></br>

**Business Problem**</br>

Gender pay reporting provides valuable **transparency into workforce equality**, but interpreting the results and identifying the underlying drivers of pay disparities remain challenging.</br>

Using publicly available UK Gender Pay Gap data from over 10,000 employers, this project **investigates the organisational factors associated with gender pay inequality** by answering the following business questions:</br>

- Which industries exhibit the largest gender pay gaps?
- Does organisation size influence pay inequality?
- How does workforce representation across pay quartiles affect the gender pay gap?
- What patterns exist in bonus pay disparities?
- Which organisations demonstrate unusually high or low gender pay gaps?

---

**Business Value**</br>

The insights generated from this analysis can help organisations and policymakers:</br>

- **Identify structural workforce patterns** contributing to gender pay disparities.</br>
- Support evidence-based workforce planning and talent development strategies.</br>
- **Strengthen Diversity, Equity & Inclusion (DEI) initiatives** through data-driven decision-making.</br>
- Enhance ESG and regulatory reporting with meaningful workforce insights.</br>
- **Improve organisational transparency** and monitor progress towards pay equity.</br>

</details>

---

<details open>
<summary><b>💻 SQL SKILLS DEMONSTRATED </b></summary></br>

| Category             | SQL Techniques                   |
| -------------------- | -------------------------------- |
| Data Exploration     | SELECT, DISTINCT, WHERE          |
| Data Aggregation     | GROUP BY, HAVING                 |
| Conditional Logic    | CASE WHEN                        |
| Joins                | INNER JOIN                       |
| Ranking              | ORDER BY                         |
| Statistical Analysis | MEDIAN using `PERCENTILE_CONT()` |
| Text Processing      | Regular Expressions              |
| Data Validation      | NULL Handling, Checking for Duplicate Records        |
| Business Analysis    | CTEs                             |


</details>

---

<details open>
<summary><b>🛠 TECHNICAL CHALLENGES SOLVED</b></summary></br>

- Determined the appropriate statistical measure (Median vs Mean)</br>
- Used PERCENTILE_CONT()</br>
- Derived London regions from postcode regex</br>
- Mapped SIC codes</br>
- Validated missing values</br>
- Identified and explained statistical outliers</br>

---

<details open>
<summary><b>🧩 SAMPLE SQL TECHNIQUES</b></summary></br>

1. Compute the mean, median, min and max of gender pay gap.</br>
   
```bash
SELECT
    AVG(diffmedianhourlypercent) AS mean_across_companies,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY diffmedianhourlypercent) AS median_across_companies,
    MIN(diffmedianhourlypercent) AS min_diffmedianhourlypercent,
    MAX(diffmedianhourlypercent) AS max_diffmedianhourlypercent
FROM gender_pay_gap_21_22;
```

2. Select the 10 Most Significant Companies with large pay gaps.</br>

```bash
SELECT 
    employername,
    companynumber,
    employerid,
    employersize,
    diffmedianhourlypercent,
    maletopquartile,
    femaletopquartile,
    maleuppermiddlequartile,
    femaleuppermiddlequartile
FROM gender_pay_gap_21_22
WHERE diffmedianhourlypercent BETWEEN 9.8 AND 80 --more than the median and excluded extreme or anomalous values
    AND employersize IN ('5,000 to 19,999', '20,000 or more') --larger organisations, more impact
    AND maletopquartile >= 60 --Focus on structural imbalance where men dominate higher-paying roles
    AND femaletopquartile > 0 --Ensure both genders are present
    AND maleuppermiddlequartile >= 60 --Progression pipeline to senior level 
ORDER BY diffmedianhourlypercent DESC
LIMIT 10;

```

3. Compute the median gender pay gap within banks.</br>


```bash

SELECT
    COUNT(*) AS number_of_companies,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY diffmedianhourlypercent) AS median_hourlypay,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY maletopquartile) AS median_maletopquartile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY femaletopquartile) AS median_femaletopquartile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY maleuppermiddlequartile) AS median_maleuppermiddlequartile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY femaleuppermiddlequartile) AS median_femaleuppermiddlequartile
FROM gender_pay_gap_21_22
WHERE LEFT(siccodes, 4) ILIKE '64%' OR LEFT(siccodes, 4) ILIKE '66%'
AND diffmedianhourlypercent IS NOT NULL
AND maletopquartile IS NOT NULL
AND femaletopquartile IS NOT NULL
AND maleuppermiddlequartile IS NOT NULL
AND femaleuppermiddlequartile IS NOT NULL;

```

4. Compute the median pay gap in London versus Birmingham. </br>

```bash

WITH location_indicator AS (
    SELECT
        employername,
        postcode,
        diffmedianhourlypercent,
        maletopquartile,
        femaletopquartile,
        maleuppermiddlequartile,
        femaleuppermiddlequartile,
        CASE 
            WHEN postcode ~* '^(E|EC|N|NW|SE|SW|W|WC)' THEN 'London'
            WHEN postcode ~* '^B' THEN 'Birmingham'
            ELSE 'Other'
        END AS region
    FROM gender_pay_gap_21_22
    WHERE diffmedianhourlypercent IS NOT NULL
    AND maletopquartile IS NOT NULL
    AND femaletopquartile IS NOT NULL
    AND maleuppermiddlequartile IS NOT NULL
    AND femaleuppermiddlequartile IS NOT NULL
)
SELECT
    region,
    COUNT(*) AS number_of_companies,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY diffmedianhourlypercent) AS median_gap, --median per region
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY maletopquartile) AS median_maletopquartile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY femaletopquartile) AS median_femaletopquartile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY maleuppermiddlequartile) AS median_maleuppermiddlequartile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY femaleuppermiddlequartile) AS median_femaleuppermiddlequartile
FROM location_indicator
WHERE region IN ('London', 'Birmingham')
GROUP BY region
ORDER BY region DESC;

```

---

<details open>
<summary><b>📈 KEY INSIGHTS FROM SQL ANALYSIS</b></summary></br>

**1. Overall Gender Pay Gap Distribution**

**🔍 Key Finding:**</br>

The median gender pay gap across UK employers is **9.8%**, with substantial variation and several extreme outliers. 
This means that **women earn approximately 10% less than men** across organisations.</br>

**💡 Business Insight:**</br>

Gender pay disparities are widespread, but the largest gaps are concentrated among a relatively small number of organisations.</br>

![Chart1](charts/01_distribution_of_pay_gap.png)

**2. Company Size Analysis**

**🔍 Key Finding:**</br>

Median pay gaps remain consistent across employer sizes, ranging from **7.2% to 10.8%**.</br>

**💡 Business Insight:**</br>

Organisation size alone does not explain gender pay inequality.

![Chart2](charts/02_pay_gap_by_employer_size.png)


**3. Regional Analysis**

**🔍 Key Finding:**</br>
London reports a **slightly higher median pay gap of 11%** compared to other regions.</br>

**💡 Business Insight:**</br>
Regional differences appear to reflect workforce composition rather than geography itself.</br>

![Chart3](charts/03_pay_gap_across_regions.png)

**4. Industry Analysis**

**🔍 Key Finding:**</br>
Education and Finance & Insurance both exhibit **relatively large gender pay gaps** despite having very different workforce compositions.</br>

**💡 Business Insight:**</br>

Gender pay gaps are **influenced more by occupational representation** than by whether an industry is male- or female-dominated.</br>

![Chart4](charts/04_pay_gap_in_sectors.png)

---

**❗️KEY IMPLICATIONS**</br>

**<font color="red">Gender Pay Gap ≠ Unlawful Pay Discrimination**</font>
Instead, it reflects broader structural factors such as the **distribution of men and women across different roles and levels within organisations**.</br>

The gender pay gap is **primarily driven by differences in representation across roles and levels**, rather than unequal pay for the same work. Men are more likely to be represented in higher-paying roles.</br>

</details>

---

<details open>
<summary><b>⚠️ DATA LIMITATIONS & CONSIDERATIONS </b></summary></br>

**1. Dataset Coverage**</br>
These limitations affect which organisations and employees are represented in the analysis.</br>
- Only companies with **250 or more employees** are legally required to submit data, meaning the entire small-employer population is absent from this dataset</br>

- Only includes **full-pay relevant employees**, excluding those on leave such as
such as maternity, paternity, sick, sabbatical, or other forms of leave</br>

**2. Data Granularity**</br>
These limitations restrict the level of analysis that can be performed.</br>

- The analysis is based on **employer-level reporting** rather than workforce-weighted measures.</br>
- The dataset does **not include role-level or job-specific information**, limiting the ability to assess equal pay for equal work.</br>
- The dataset represents **a single reporting period**, preventing trend analysis over time.</br>



**3. Data Quality & Consistency**
These limitations may affect the accuracy and comparability of the findings.</br>

- The data is **self-reported by employers**, which may introduce reporting inconsistencies.</br>
- Some organisations report **multiple or inconsistent SIC (industry) classifications**, reducing comparability across sectors.</br>
- **Regional analysis is based on employer postal codes**, which may not reflect employees' actual work locations.</br>

**4. Structural Dataset Constraints**
- The dataset contains structural limitations, including the **absence of workforce headcount**, **limited contextual information** (such as working patterns and role distribution), and instances where **missing values are represented as zeros**.</br>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

**1. Improve Data Quality & Reporting**</br>

Strengthen the quality and consistency of gender pay reporting to enable more accurate and meaningful analysis.</br>

- **Enhance data granularity** by collecting additional information such as job roles and levels, career progression and promotions, and tenure and experience.</br>
- **Improve consistency and clarity in reporting** by standardising reporting definitions and submission practices.</br>
- **Capture more precise workforce measures**, including actual employee counts, to support more representative and workforce-weighted analysis.</br>

**2. Strengthen Workforce Progression**</br>

Address the structural factors contributing to the gender pay gap by improving representation in higher-paying roles.</br>

- **Encourage organisations to strengthen career progression pathways**, ensuring equitable access to promotions, leadership opportunities, and higher-paying roles.</br>

---

<details>
<summary><b>🗂 DATASET</b></summary></br>

 Source | Description | Link |
|---------|-------------|-----|
| UK Government Gender Pay Gap Reporting Service | Annual employer-reported gender pay statistics | • [View Dataset](data/gender_pay_gap_21_22.csv) </br> • [View Data Source](https://gender-pay-gap.service.gov.uk) |

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

<details>
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

⭐ **This project demonstrates my ability to:**</br>
🧠 Translate business questions into SQL analysis</br>

✅ Validate and interpret complex datasets</br>

💡 Produce executive-ready insights</br>

📊 Communicate technical findings clearly</br>

🔍 Recommend evidence-based actions</br>

**Connect with me.**</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

---