### 🇬🇧👩👱🏻‍♂️ UK Gender Pay Gap Analysis
**<font color="green">SQL | Data Storytelling | Business Intelligence | Workforce Analytics**</font>

A business intelligence project analysing **gender pay gap across more than 10,000 UK employers** to uncover workforce representation patterns and identify opportunities for greater pay equity.

<details open>
<summary><b>👓 EXECUTIVE SUMMARY</b></summary></br>

🇬🇧 Analysed **10,174 UK employers using [official UK Government gender pay reporting data](https://gender-pay-gap.service.gov.uk)**</br>

💷 Identified a **typical median pay gap of 9.8%**

👬 Found **workforce representation**, not organisation size, to be the strongest driver

💡 Produced **evidence-based recommendations** to support workforce planning, DEI initiatives, and public policy</br>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>


| Category | Details |
|------|--------|
| SQL Analytics Workflow | 🧠 Business Analysis </br> 🔍 Exploratory SQL Analysis </br> 📈 Statistical Analysis </br> 📊 Data Storytelling </br> 📋 Executive Reporting </br> 💡 Evidence-based Recommendations</br>|
| Technology Stack | ![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=sqlite&logoColor=white) • ![Canva](https://img.shields.io/badge/Canva-00C4CC?style=flat&logo=canva&logoColor=white) • ![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=flat&logo=microsoftpowerpoint&logoColor=white)  |
| Project Artefacts | 🔍 [SQL Analysis](sql/UK_Gender_Pay_Gap_Analysis_SQL.pdf) </br> 📄 [Technical Report](report/UK_Gender_Pay_Gap_Analysis_Report.pdf) </br> 🎤 [Presentation Slides](presentation/UK_Gender_Pay_Gap_Analysis_Presentation.pdf) </br>|


</details>

---

<details open>
<summary><b>💻 SQL SKILLS DEMONSTRATED </b></summary></br>

| Category             | SQL Techniques                   |
| -------------------- | -------------------------------- |
| Data Exploration     | SELECT, DISTINCT, WHERE          |
| Data Aggregation     | GROUP BY, HAVING                 |
| Feature Engineering  | CASE WHEN                        |
| Joins                | INNER JOIN                       |
| Sorting              | ORDER BY                         |
| Statistical Analysis | PERCENTILE_CONT                  |
| Pattern Matching     | ILIKE, Regular Expressions (regex)       |
| Data Validation      | NULL Handling, Checking for Duplicate Records        |
| Analytical Query Design    | CTEs                             |

</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM AND BUSINESS VALUE</b></summary></br>

**Business Problem**</br>

Gender pay reporting provides valuable **transparency into workforce equality**, but interpreting the results and identifying the underlying drivers of pay gap remain challenging.</br>

Using publicly available [UK Gender Pay Gap data](https://gender-pay-gap.service.gov.uk) from over 10,000 employers, this project **investigates the organisational factors associated with gender pay gap** by answering the following business questions:</br>

- Which industries exhibit the largest gender pay gaps?
- Does organisation size influence the gender pay gap?
- How does workforce representation across pay quartiles affect the gender pay gap?
- Do regional differences influence the gender pay gap?
- Which organisations demonstrate unusually high or low gender pay gaps?

---

**Business Value**</br>

The insights generated from this analysis can help organisations and policymakers:</br>

- **Identify structural workforce patterns** contributing to gender pay gaps.</br>
- **Support workforce planning** and talent development strategies.</br>
- **Strengthen Diversity, Equity & Inclusion (DEI) initiatives** through data-driven decision-making.</br>
- **Improve ESG reporting** with meaningful workforce insights.</br>
- **Increase organisational transparency** and monitor progress towards pay equity.</br>

</details>

---

<details open>
<summary><b>🛠 ANALYTICS CHALLENGES SOLVED</b></summary></br>

- Determined the appropriate statistical measure (Median vs Mean)</br>
- Used PERCENTILE_CONT()</br>
- Derived London and Birmingham regions from postcode via regex</br>
- Mapped Standard Industrial Classification (SIC) codes</br>
- Validated missing values</br>
- Identified and explained statistical outliers</br>

---

<details open>
<summary><b>🧩 SAMPLE SQL TECHNIQUES</b></summary></br>

The following SQL snippets demonstrate the techniques used to answer the project's business questions.</br>

**1. Compute the mean, median, min and max of gender pay gap.**</br>
   
```bash
SELECT
    AVG(diffmedianhourlypercent) AS mean_across_companies,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY diffmedianhourlypercent) AS median_across_companies,
    MIN(diffmedianhourlypercent) AS min_diffmedianhourlypercent,
    MAX(diffmedianhourlypercent) AS max_diffmedianhourlypercent
FROM gender_pay_gap_21_22;
```

**2. Compute the median gender pay gap within banks.**</br>

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

**3. Compute the median pay gap in London versus Birmingham.**</br>

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

**1. Overall Gender Pay Gap Distribution**</br>

<p align="center">
  <img src="charts/01_distribution_of_pay_gap.png" width="50%"></br>
  Figure 1. Overall Gender Pay Gap Distribution
</p>

**🔍 Key Finding:**</br>

The median gender pay gap across UK employers is **9.8%**, with substantial variation and several extreme outliers. 
This means that **women earn approximately 10% less than men** across organisations.</br>

**💡 Business Insight:**</br>

Gender pay gaps are widespread, but the largest gaps are concentrated among a relatively small number of organisations.</br>

---

**2. Company Size Analysis**</br>

<p align="center">
  <img src="charts/02_pay_gap_by_employer_size.png" width="50%"></br>
  Figure 2. Median gender pay gap across employer size categories
</p>

**🔍 Key Finding:**</br>

Median pay gaps remain consistent across employer sizes, ranging from **7.2% to 10.8%**.</br>

**💡 Business Insight:**</br>

Organisation size alone does not explain gender pay gap.

---

**3. Regional Analysis**</br>

<p align="center">
  <img src="charts/03_pay_gap_across_regions.png" width="50%"></br>
  Figure 3. Median gender pay gap across regions
</p>

**🔍 Key Finding:**</br>
London reports a **slightly higher median pay gap of 11%** compared to other regions.</br>

**💡 Business Insight:**</br>
Regional differences appear to reflect workforce composition rather than geography itself.</br>

---

**4. Industry Analysis**</br>

<p align="center">
  <img src="charts/04_pay_gap_in_sectors.png" width="50%"></br>
  Figure 4. Median gender pay gap across industries
</p>

**🔍 Key Finding:**</br>
Education and Finance & Insurance both exhibit **relatively large gender pay gaps** despite having very different workforce compositions.</br>

**💡 Business Insight:**</br>

Gender pay gaps are **influenced more by occupational representation** than by whether an industry is male- or female-dominated.</br>

---

**❗️KEY IMPLICATION**</br>

**<font color="red">Gender Pay Gap ≠ Unlawful Pay Discrimination**</font></br>

Instead, it reflects broader structural factors such as the distribution of men and women across different roles and levels within organisations.</br>

The gender pay gap is primarily driven by differences in representation across roles and levels, rather than unequal pay for the same work. Men are more likely to be represented in higher-paying roles.</br>

</details>

---

<details open>
<summary><b>⚠️ DATA LIMITATIONS & CONSIDERATIONS </b></summary></br>

**1. Dataset Coverage**</br>
These limitations affect which organisations and employees are represented in the analysis.</br>
- Only companies with **250 or more employees** are legally required to submit data, meaning the entire small-employer population is absent from this dataset.</br>

- Only includes full-pay relevant employees, excluding those on leave such as
such as maternity, paternity, sick, sabbatical, or other forms of leave.</br>

**2. Data Granularity**</br>
These limitations restrict the level of analysis that can be performed.</br>

- The analysis is based on **employer-level reporting** rather than workforce-weighted measures.</br>
- The dataset does not include role-level or job-specific information, limiting the ability to assess equal pay for equal work.</br>
- The dataset represents a single reporting period, preventing trend analysis over time.</br>

**3. Data Quality & Consistency**</br>
These limitations may affect the accuracy and comparability of the findings.</br>

- The data is **self-reported by employers**, which may introduce reporting inconsistencies.</br>
- Some organisations report multiple or inconsistent SIC (industry) classifications, reducing comparability across sectors.</br>
- Regional analysis is based on employer postal codes, which may not reflect employees' actual work locations.</br>

**4. Structural Dataset Constraints**
- The dataset contains structural limitations, including the **absence of workforce headcount**, **limited contextual information** (such as working patterns and role distribution), and instances where **missing values are represented as zeros**.</br>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

**1. Improve Reporting Quality**</br>

Strengthen the quality and consistency of gender pay reporting to enable more accurate and meaningful analysis.</br>

- **Enhance data granularity** by collecting additional information such as job roles and levels, career progression and promotions, and tenure and experience.</br>
- **Improve consistency and clarity in reporting** by standardising reporting definitions and submission practices.</br>
- **Capture more precise workforce measures**, including actual employee counts, to support more representative and workforce-weighted analysis.</br>

**2. Improve Career Progression**</br>

Address the structural factors contributing to the gender pay gap by improving representation in higher-paying roles.</br>

- **Encourage organisations to strengthen career progression pathways**, ensuring equitable access to promotions, leadership opportunities, and higher-paying roles.</br>

</details>

---

<details open>
<summary><b>🏆 PROJECT OUTCOMES</b></summary></br>

✅ Analysed **10,174 UK employers**</br>
✅ Answered **5 business questions**</br>
✅ Produced **4 executive recommendations**</br>
✅ Built **4 business visualisations**</br>
✅ Applied **advanced SQL techniques** including window functions, CTEs, regex and statistical aggregation</br>
✅ Delivered **technical report + presentation**</br>

</details>

---

<details>
<summary><b>🗂 DATASET</b></summary></br>

 Source | Description | Link |
|---------|-------------|-----|
| UK Government Gender Pay Gap Reporting Service | Annual employer-reported gender pay statistics | • [View Dataset](data/gender_pay_gap_21_22.zip) </br> • [View Data Source](https://gender-pay-gap.service.gov.uk) |

Key Variables:</br>
- Mean & Median Hourly Pay Gap</br>
- Bonus Pay Gap & Participation</br>
- Workforce Pay Quartiles</br>
- Employer Size</br>
- Industry Classification (SIC)</br>
- Reporting Compliance</br>

</details>

---

<details>
<summary><b>🗂️ REPOSITORY STRUCTURE</b></summary></br>

| Folder        | Description              |
| ------------- | ------------------------ |
| 📁 charts     | Visualisations |
| 📁 data       | Gender Pay Gap Dataset |
| 📁 sql  | End-to-end SQL Analysis |
| 📁 report    | Technical Report | 
| 📁 presentation    | Presentation Slides |

</details>

---

⭐ **This project demonstrates my ability to:**</br>

🧠 Translate business questions into SQL analysis</br>

🔍 Validate and interpret complex datasets</br>

💡 Produce executive-ready insights</br>

📊 Communicate technical findings clearly</br>

🔍 Recommend evidence-based actions</br>

**Let's Connect**</br>

📧 [Email](mariaemilysy@gmail.com)</br>
💼 [LinkedIn](https://www.linkedin.com/in/emilysy/)</br>
💻 [Data Analytics Portfolio](https://github.com/thedataanalyst-ylime/data-analytics-portfolio)</br>

---