# 🏎️ Formula 1 & the Indian Grand Prix
### Exploring the Commercial Sustainability of F1 Events Through Data

**Why did Formula 1's Indian Grand Prix last only three seasons?**

This project investigates the commercial sustainability of Formula 1 events, using the **2011–2013 Indian Grand Prix at Buddh International Circuit** as a focused case study.

By combining historical Formula 1 race data, exploratory data analysis, statistical comparisons, and documented financial and regulatory context, the project aims to understand how the Indian Grand Prix compared with other F1 events and what factors may have contributed to the challenges surrounding its continuation.

The objective is not to assign a single cause to the event's discontinuation, but to distinguish what the data demonstrates from what historical and documentary evidence suggests.

> **Core question:** What can historical Formula 1 data tell us about the commercial sustainability of the Indian Grand Prix?

## 🎯 Research Objectives

The analysis is organized around six research questions:

1. **Attendance trends:** How did Indian GP attendance change between 2011 and 2013?
2. **Global comparison:** How did attendance at the Indian GP compare with other Formula 1 events during the same period?
3. **Event characteristics:** Which sporting, circuit, geographic, and economic characteristics are associated with attendance?
4. **Commercial pressures:** What documented hosting fees, revenue indicators, and operating costs help explain the event's financial challenges?
5. **Statistical anomalies:** Which races or variables exhibit unusual patterns relative to the broader F1 dataset?
6. **Historical context:** How do the quantitative findings relate to documented taxation, contractual, and regulatory issues?

## 📊 Data Strategy

The project uses three complementary datasets.

| Dataset | Scope | Purpose |
|---|---|---|
| Global F1 baseline | 2010–2019 | Compare race characteristics and identify broader patterns |
| Indian GP deep dive | 2011–2013 | Examine attendance trends and available commercial indicators |
| Historical context timeline | 2007–2017 | Document relevant sporting, financial, tax, and legal events |

The global dataset is intended to contain approximately 190–200 race observations, subject to data availability and validation.

### Data sources

Potential sources include:

- **Jolpica F1 API:** Historical race schedules, circuits, results, and sporting statistics.
- **Formula 1 publications and motorsport reporting:** Historical attendance and event information.
- **Official legal and government documents:** Taxation, regulatory, and judicial context.
- **Historical financial reporting:** Available hosting-fee, ticketing, revenue, and cost information.
- **World Bank and other recognized economic sources:** Country-level economic indicators where relevant.

Every important value should be traceable to its source. Unavailable financial figures will remain missing rather than being presented as established facts.

## 🔬 Analytical Methodology

The project follows a structured data-analysis workflow.

### 1. Data acquisition
Collect historical race records, attendance figures, available financial information, and relevant documentary evidence.

### 2. Data cleaning and validation
- Inspect missing values and inconsistent records.
- Detect duplicates and validate dataset keys.
- Standardize units and currencies where appropriate.
- Investigate outliers rather than removing them automatically.
- Record source reliability and document any imputation.

### 3. Exploratory data analysis
- Descriptive statistics: mean, median, variance, and standard deviation.
- Distribution analysis: histograms, box plots, skewness, and kurtosis.
- Temporal analysis: season-level and Indian GP attendance trends.
- Comparative analysis: regions, circuit types, and event tenure.
- Relationship analysis: correlations between attendance and available explanatory variables.

### 4. Statistical analysis
Where the available data and assumptions support it, the project will investigate correlations, group differences, confidence intervals, and regression-based relationships.

### 5. Indian GP case study
Compare the three Indian races against relevant historical F1 events, then interpret the observed patterns alongside documented commercial and regulatory context.

### 6. Findings and interpretation
Connect each important finding to supporting evidence, possible explanations, alternative interpretations, and limitations.

## 📈 Planned Visualizations

The analysis aims to produce clear, question-driven visualizations, including:

- Attendance distributions with Indian GP observations highlighted.
- Attendance trends across the three Indian Grand Prix races.
- Comparisons between regions and circuit types.
- Correlation heatmaps for relevant numerical variables.
- Multivariable plots exploring attendance and economic context.
- A historical timeline integrating sporting, commercial, and regulatory events.

Final visualizations will be added as the analysis is completed.

## 🧰 Technology Stack

The planned analytical workflow uses:

- **Python** — Data processing and analysis.
- **Pandas & NumPy** — Data manipulation and numerical computation.
- **Matplotlib & Seaborn** — Data visualization.
- **SciPy** — Statistical tests and distribution analysis.
- **Jupyter Notebook** — Exploratory analysis and documentation.

The final dependency list and execution instructions will be documented alongside the implemented notebooks and scripts.

## 📁 Repository Structure

```text
F1-case-study/
├── data/
│   ├── raw/                 # Original collected datasets
│   └── processed/           # Cleaned, validated datasets
├── notebooks/               # Data collection, cleaning and analysis
├── reports/                 # Data quality, findings and final report
├── scripts/                 # Reusable processing scripts, if applicable
├── sources/                 # Source registry and references
├── case_study.md            # Project brief and evaluation rubric
├── plan.md                  # Research and execution plan
└── README.md
```

*The directory layout and deliverables may evolve as implementation progresses.*

## ⚖️ Research Integrity

This project follows several analytical principles:

- **Correlation is not causation.** Statistical relationships alone cannot establish why an event was discontinued.
- **Missing data is not zero.** Unavailable historical figures will be identified explicitly.
- **Outliers require investigation.** Unusual observations may be genuine rather than errors.
- **Sources matter.** Important financial, attendance, and legal claims should be independently traceable.
- **Historical chronology matters.** The last Indian GP in 2013 and the subsequent 2017 Supreme Court judgment are distinct events; the latter will not be presented as the direct cause of F1's departure.

## 🚧 Project Status

**Status: In progress — research design and data-analysis workflow.**

The research plan defines the questions, intended datasets, analytical methods, and documentation requirements. The next milestones are to validate the collected data, complete the cleaning pipeline, perform the analysis, and publish evidence-backed findings.

Results, charts, and conclusions will be added as they are verified.

## 📚 Project Documentation

- [Research brief and evaluation rubric](case_study.md)
- [Master execution plan](plan.md)

## 👨‍💻 About

An exploratory data analysis project investigating the intersection of motorsport, economics, and historical context.

The goal is to go beyond race results and use data to understand the commercial challenges behind one of India's most ambitious motorsport events.

---

*This is an independent educational research project and is not affiliated with Formula 1 or the FIA.*
