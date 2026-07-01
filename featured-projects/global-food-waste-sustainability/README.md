### 🌍 Global Food Waste & Sustainability Analysis

<details open>
<summary><b>PROJECT AT A GLANCE</b></summary></br>

| Item | Details |
|---------|------|
| Duration | 4 weeks |
| Role | End-to-End Data Analyst |
| Datasets | 233 countries, 40+ features |
| Tools | Python, Pandas, Scikit-learn, Tableau, Streamlit, Git, GitHub |
| Deliverables | Python Notebook, Tableau Interactive Dashboards, Predictive Model, Streamlit App, Technical Report and Project Presentation |

</details>

---

<details open>
<summary><b>📌 PROJECT OVERVIEW</b></summary></br>

Food waste is a global sustainability challenge with significant environmental, economic, and social consequences. According to the UNEP Food Waste Index Report, over one billion tonnes of food are wasted annually, yet the key factors influencing food waste across countries remain poorly understood.

This project combines multiple international datasets to investigate global food waste patterns, identify the strongest drivers of food waste, and develop a predictive model capable of estimating household food waste using country-level indicators.

The project follows a complete analytics workflow — from data acquisition and preparation through exploratory analysis, dashboard development, statistical validation, predictive modelling, and business recommendations.

</details>

---

<details open>
<summary><b>🎯 BUSINESS PROBLEM</b></summary></br>

Governments, sustainability organisations, NGOs, and policymakers require reliable evidence to determine where interventions will have the greatest impact.

This project answers key business questions:

- Which countries generate the most food waste?
- Does economic wealth influence food waste?
- Is food waste primarily driven by population or climate?
- Which countries should be prioritised for intervention?
- Can household food waste be predicted using publicly available country indicators?

</details>

---

<details open>
<summary><b>🗂 DATASETS</b></summary></br>

| Source | Description | Link |
|---------|-------------|-----|
| United Nations Environment Program (UNEP) Food Waste Index Report 2024 | Household, Food Service and Retail Food Waste Estimates | [View Source](https://www.unep.org/resources/publication/food-waste-index-report-2024) |
| World Bank Open Data | GDP per Capita, Income Group, Total Population, Population Density, Tourism Arrivals, Electricity Access, CO2 Emissions | [View Source](https://data.worldbank.org) |
| Trading Economics | Average Annual Temperature by Country | [View Source](https://tradingeconomics.com/country-list/temperature) |

</details>

---

<details open>
<summary><b>ANALYTICS WORKFLOW</b></summary></br>

Business Understanding
    ⬇️
Data Collection
    ⬇️
Data Cleaning & Validation
    ⬇️
Feature Engineering
    ⬇️
Exploratory Data Analysis
    ⬇️
Dashboard Development
    ⬇️
Statistical Analysis
    ⬇️
Predictive Modelling
    ⬇️
Business Recommendations

</details>

---

<details open>
<summary><b>🛠 TECHNOLOGY STACK</b></summary></br>

| Category | Tools |
|----------|------|
| Programming | Python |
| Data Cleaning | Pandas |
| Statistical Analysis | NumPy, SciPy |
| Data Visualisation | Tableau |
| Machine Learning | Scikit-learn |
| Development | Jupyter Notebook |
| App Deployment | Streamlit |
| Version Control | Git & GitHub |
| Presentation | Canva & Powerpoint |

</details>

---

<details open>
<summary><b>📈 KEY INSIGHTS</b></summary></br>

 **1. Population is the strongest driver of total food waste.**

Countries with larger populations generate substantially higher food waste volumes than smaller nations.

---

 **2. Temperature shows a stronger relationship with food waste than GDP.**

Warmer countries generally experience higher household food waste per capita, while GDP shows only a weak relationship.

---

 **3. Higher-income countries are not automatically the biggest food wasters.**

Food waste occurs across all income groups, suggesting that behavioural and environmental factors matter more than economic wealth alone.

</details>

---

<details open>
<summary><b>INTERACTIVE DASHBOARD</b></summary></br>

The Tableau dashboard enables users to:

- Explore food waste by country
- Compare income groups
- Analyse relationships between climate, GDP and population
- Identify high-risk countries
- Interactively filter countries and income categories

**Dashboard Highlights**

- Global Overview
- Food Waste Drivers
- Risk & Opportunity Profile
- Global Priority Intervention Map

🔗 **[View Interactive Tableau Dashboard](https://us-east-1.online.tableau.com/#/site/gaenterpriselicenses/collections/999465e4-5105-4936-987f-7c60e14b640e?:origin=card_share_link)**

</details>

---

<details open>
<summary><b>PREDICTIVE MODELING</b></summary></br>

**Objective:** To predict household food waste (kg per capita per year).

**Models Evaluated**

- Baseline Model
- Linear Regression
- Random Forest Regression

**Best Performing Model**

✅ Random Forest Regression

Features used:

- Average Temperature
- GDP per Capita (log)
- Population Density (log)
- Income Group
- Food Service Waste per Capita 

Evaluation metrics included:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-Squared of Coeffiecient of Determination (R²)

The Random Forest model demonstrated the strongest predictive performance and captured the complex non-linear relationships between environmental and socio-economic variables.

</details>

---

<details open>
<summary><b>REPOSITORY STRUCTURE</b></summary></br>

global-food-waste-sustainability/

│
├── app/
│   └── Streamlit prediction app
│
├── charts/
│   └── Exploratory data analysis visualisations (Tableau)
│
├── dashboards/
│   └── Tableau dashboards
│
├── data/
│   ├── Raw datasets
│   ├── Clean datasets
|   ├── Audit country matching
│   └── Data model
│
├── notebooks/
│   └── End-to-end Python analysis
│
├── reports/
│   ├── Technical paper
│   └── Presentation slides
│
└── README.md

</details>

---

<details open>
<summary><b>INTERACTIVE STREAMLIT DEMO</b></summary></br>


![Streamlit Demo Screenshot](assets/streamlit-demo.png)

</details>

---

<details open>
<summary><b>HOW TO RUN THE STREAMLIT DEMO</b></summary></br>

This project includes a Streamlit demo app that predicts household food waste using the Random Forest model.

**1. Clone the repository**

```bash
git clone https://github.com/thedataanalyst-ylime/data-analytics-portfolio/tree/main/featured-projects/global-food-waste-sustainability
```

**2. Navigate to the project folder**

```bash
cd data-analytics-portfolio/featured-projects/global-food-waste-sustainability
```

**3. Create a virtual environment**

For Mac:
```bash
python -m venv venv
```

For Windows:
```bash
venv\Scripts\activate
```

**4. Activate the virtual environment**

```bash
source venv/bin/activate
```

**5. Install the required libraries**

```bash
pip install -r app/requirements.txt
```

**6. Run the Streamlit app**

```bash
streamlit run app/predict_household_foodwaste_demo.py
```

**7. Open the app in your browser**

After running the command, Streamlit will show a local URL such as:
```bash
http://localhost:8501
```
Open this link in your browser to use the demo.

</details>

---

<details open>
<summary><b>💡 BUSINESS RECOMMENDATIONS</b></summary></br>

- Prioritise interventions in countries with high population-driven food waste.
- Focus awareness campaigns in warmer climates where household waste tends to be higher.
- Develop country-specific food waste reduction strategies instead of relying solely on income classifications.
- Use predictive analytics to identify regions requiring early intervention.

</details>

---

<details open>
<summary><b>FUTURE IMPROVEMENTS</b></summary></br>

TBD

</details>

---

⭐ If you found this project interesting, feel free to connect or explore my other analytics projects

💼 Connect with me on LinkedIn: https://www.linkedin.com/in/emilysy/
💻 View my Data Analytics Portfolio: https://github.com/thedataanalyst-ylime/data-analytics-portfolio </br>

---