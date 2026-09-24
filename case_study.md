# Case Study: Formula 1 and the Indian Grand Prix

## 1. Project Overview

### Working Title

**An Exploratory Data Analysis of the Commercial Sustainability of Formula 1 Events: A Case Study of the Indian Grand Prix**

### Core Idea

This project will investigate the commercial and event-level characteristics of Formula 1 races using a broad historical F1 dataset, and then use the **2011–2013 Indian Grand Prix** as a focused case study.

The project is **not** intended to answer the question "Why did F1 leave India?" using only historical/legal information.

Instead, the project will use data to investigate:

- How Formula 1 event characteristics relate to attendance and commercial sustainability.
- How the Indian Grand Prix compared with other F1 races.
- What changed across India's three F1 races.
- Whether the Indian Grand Prix displayed unusual patterns compared with the broader F1 dataset.
- How quantitative findings can be interpreted alongside the documented tax, contractual, regulatory and business context.

The final conclusion must distinguish between:
1. What the data directly shows.
2. What can reasonably be inferred from the data.
3. What is documented by legal, financial and historical sources.

---

# 2. Why We Are Using This Approach

A dataset containing only the three Indian races would be too small for the statistical requirements of the course.

Therefore, the project will use a **two-level structure**:

### Level 1 — Broad F1 Dataset

Collect approximately **190–200 Formula 1 races**, initially targeting the period **2010–2019**.

This provides enough observations for:

- descriptive statistics
- distributions
- skewness
- kurtosis
- outlier detection
- correlation analysis
- multidimensional visualization
- comparative analysis

### Level 2 — India Case Study

Create a separate detailed dataset for:

- 2011 Indian Grand Prix
- 2012 Indian Grand Prix
- 2013 Indian Grand Prix

This dataset will contain variables that are specifically relevant to the Indian event's commercial and regulatory situation.

The broad dataset provides the **comparison baseline**.

The India dataset provides the **case-study depth**.

---

# 3. Main Research Questions

The project will investigate the following questions.

## Primary Research Question

**How did the commercial and event characteristics of the Indian Grand Prix compare with broader Formula 1 events, and what data-driven patterns can help explain the challenges surrounding its sustainability in India?**

## Secondary Questions

### RQ1 — Attendance

How did attendance at the Indian Grand Prix change from 2011 to 2013?

### RQ2 — Comparative Position

How did Indian GP attendance compare with other Formula 1 races during the same period?

### RQ3 — Event Characteristics

What race/event characteristics are associated with higher or lower attendance?

### RQ4 — Commercial Pressure

What documented financial factors affected the economics of the Indian GP?

### RQ5 — Anomalies

Which variables or races behave unusually compared with the broader F1 dataset?

### RQ6 — Context

How do the quantitative findings relate to the documented taxation, contractual and regulatory issues surrounding the Indian GP?

---

# 4. Scope

## Included

- Formula 1 races approximately from 2010–2019.
- Indian Grand Prix 2011–2013.
- Race-level statistics.
- Circuit characteristics.
- Attendance where reliable data is available.
- Relevant financial information for the Indian GP.
- Relevant tax/legal/business events.
- Country-level contextual variables where useful.

## Excluded

- Speculation about motives of governments or companies.
- Unsupported claims about why individual organizations made decisions.
- Detailed legal analysis beyond what is necessary for the EDA.
- Attempting to calculate exact profitability where reliable financial data is unavailable.
- Fabricating or estimating missing financial values without explicitly labeling them as estimates.
- Treating the 2017 Supreme Court judgment as the direct reason F1 left India; the final Indian GP occurred in 2013.

---

# 5. Data Architecture

We will maintain three primary datasets.

## Dataset A — `f1_races.csv`

### Purpose

This is the main statistical dataset.

### Target size

Approximately:

**190–200 race observations**

with approximately:

**20–30 variables**

### Suggested variables

#### Event Information

- `season`
- `round`
- `race_name`
- `date`
- `country`
- `city`
- `circuit_name`

#### Race Characteristics

- `circuit_length_km`
- `race_distance_km`
- `laps`
- `race_duration`
- `average_speed`
- `fastest_lap`
- `pit_stops`

#### Competition

- `winner`
- `winning_constructor`
- `number_of_finishers`
- `number_of_drivers`
- `number_of_constructors`
- `winning_margin`

#### Attendance

- `attendance`
- `attendance_source`
- `attendance_confidence`

#### Circuit/Event Classification

- `circuit_type` (street/permanent/other where reliably obtainable)
- `new_or_established_event`
- `continent`

#### Country Context

Potential variables:

- `population`
- `gdp_per_capita`
- `exchange_rate`
- other relevant country-level variables

Only include contextual variables that can be obtained consistently for the selected period.

---

# 6. Dataset B — `india_gp.csv`

This is the detailed India-specific dataset.

### Target size

**3 rows**

One row for each:

- 2011
- 2012
- 2013

### Variables

#### Event

- `season`
- `date`
- `round`
- `circuit`
- `country`

#### Attendance

- `attendance`
- `attendance_source`
- `attendance_confidence`

#### Financial

Where reliable sources exist:

- `hosting_fee_usd`
- `ticket_revenue`
- `total_event_revenue`
- `operating_cost`
- `estimated_profit_or_loss`
- `ticket_price`
- `currency`
- `usd_conversion_method`

#### Tax/Regulatory

- `entertainment_tax_issue`
- `customs_issue`
- `tax_status`
- `major_regulatory_event`

#### Commercial

- `promoter`
- `sponsorship_context`
- `broadcasting_context`

### Important rule

If a financial number cannot be reliably established, it will be stored as:

`NA`

rather than invented.

If a number is reported by a source as an estimate, it will be explicitly marked:

`estimated = TRUE`

---

# 7. Dataset C — `india_gp_context.csv`

This dataset records important historical/legal/business events.

### Suggested structure

| Column | Purpose |
|---|---|
| `date` | Date/year of event |
| `event` | What happened |
| `category` | Tax / Legal / Business / Sporting |
| `description` | Short factual description |
| `source` | Source/reference |
| `impact_type` | Financial / Regulatory / Operational / Other |
| `confidence` | High / Medium / Low |

Examples include:

- 2011 first Indian GP.
- Entertainment-tax dispute.
- 2012 Indian GP.
- 2013 final Indian GP.
- 2014 absence from F1 calendar.
- Later tax litigation.
- 2017 Supreme Court judgment concerning FOWC's Permanent Establishment.

This dataset is primarily for **contextual interpretation**, not statistical modeling.

---

# 8. Data Sources

## F1 Race Data

Use a structured F1 data source/API such as **Jolpica F1**, the successor to the Ergast API.

Potential information:

- races
- circuits
- drivers
- constructors
- results
- lap information
- pit stops

## Attendance

Use reliable historical sources where available:

- Formula 1 official publications
- official race/event reports
- reputable motorsport publications
- historical sporting databases

Attendance sources must be recorded.

## Indian GP Financial Data

Potential sources:

- Supreme Court judgments
- government documents
- contemporary financial/news reporting
- reputable motorsport publications
- company reports where available

## Legal/Tax Context

Prioritize:

- Supreme Court of India
- government documents
- official tax/legal documents
- reputable legal databases/publications

---

# 9. Data Collection Strategy

## Phase 1 — Define Schema

Before collecting data, finalize:

- all columns
- data types
- units
- acceptable missing values
- source requirements
- confidence labels

Create a data dictionary.

Example:

```text
attendance:
Type: integer
Unit: spectators
Missing: allowed
Source required: yes
```

---

## Phase 2 — Collect Broad F1 Data

Collect the race-level dataset for approximately 2010–2019.

Priority order:

1. Race/event metadata
2. Race results
3. Circuit information
4. Pit stops/competition information
5. Attendance
6. Country context

Do not spend excessive time collecting variables that cannot be used analytically.

---

## Phase 3 — Collect India Data

Collect detailed information specifically for:

- 2011
- 2012
- 2013

Financial information should be cross-checked between sources.

Each important value should have a source attached.

---

## Phase 4 — Collect Legal/Business Context

Build the India context timeline.

Important concepts to document:

- Race Promotion Agreement
- hosting fee
- entertainment-tax dispute
- customs/regulatory issues
- Permanent Establishment dispute
- 2017 Supreme Court decision

This phase supports interpretation but should not replace quantitative analysis.

---

# 10. Data Cleaning Plan

The cleaning process will be deliberately rigorous to satisfy the rubric.

## Missing Data

First determine whether missingness is:

- genuinely unavailable
- not applicable
- not reported
- data collection failure

Do not automatically replace all missing values with zero.

Potential techniques:

- median imputation where statistically justified
- group-based imputation
- interpolation for appropriate time-series variables
- explicit `NA` for unavailable historical facts

Every imputation method must be documented.

---

## Outliers

Use:

- IQR method
- z-scores where appropriate
- distribution plots

Important:

An outlier will **not automatically be removed**.

It will first be investigated to determine whether it represents:

- a genuine unusual race
- a data error
- a special event
- a change in measurement

---

## Normalization

Potential transformations:

- currency normalization to USD
- distance normalization to km
- attendance scaling
- log transformation for heavily skewed financial variables

Original values should be retained where possible.

---

# 11. Exploratory Data Analysis

The EDA will be organized into several layers.

## A. Univariate Analysis

For important numerical variables:

- mean
- median
- standard deviation
- minimum
- maximum
- quartiles
- IQR
- skewness
- kurtosis

Visualizations:

- histograms
- KDE/distribution plots
- box plots

---

## B. Time-Series Analysis

Investigate changes across seasons.

Examples:

- attendance over time
- average race speed over time
- pit stops over time
- number of races by region
- Indian GP attendance across 2011–2013

---

## C. Comparative Analysis

Compare:

- India vs other races
- Asia vs Europe vs Americas
- street vs permanent circuits
- newer vs established events

The comparison groups must be defined before analysis to avoid cherry-picking.

---

## D. Correlation Analysis

Potential relationships:

- attendance vs circuit characteristics
- attendance vs country GDP per capita
- attendance vs race duration
- attendance vs event age
- attendance vs competition variables

Correlation does **not** establish causation.

---

## E. Multidimensional Analysis

This is important for the visualization rubric.

Potential visualizations:

- pairplots
- correlation heatmaps
- faceted plots
- multi-variable scatter plots
- grouped distribution plots

The purpose of each plot must be explicitly stated.

---

# 12. Statistical Analysis

Potential techniques:

### Descriptive Statistics

- mean
- median
- variance
- standard deviation
- skewness
- kurtosis

### Distribution Analysis

Investigate whether important variables approximately follow:

- normal
- log-normal
- other suitable distributions

Do not force a distribution simply to satisfy the rubric.

### Relationship Analysis

- Pearson correlation where assumptions are appropriate
- Spearman correlation for monotonic/non-normal relationships

### Optional

If the dataset supports it:

- simple/multiple linear regression
- group comparison tests
- confidence intervals

Advanced statistical models are optional and should only be used if the data supports them.

---

# 13. India Case Study Analysis

After understanding the broad F1 dataset, return to India.

Questions:

### Attendance

Did Indian GP attendance decline across 2011–2013?

### Relative performance

Was the Indian GP attendance unusually low/high compared with similar races?

### Commercial structure

How large was the documented hosting fee relative to available revenue/cost information?

### Regulatory environment

What tax and regulatory issues occurred?

### Timeline

Did commercial problems appear before or after particular regulatory/legal events?

### Interpretation

Which conclusions are supported by data and which require external documentary evidence?

---

# 14. Important Chronology

The analysis must maintain the following distinction:

**2011–2013**

Indian Grand Prix takes place.

**2013**

Last Indian Grand Prix.

**2014**

Indian GP is absent from the F1 calendar.

**2017**

Supreme Court judgment concerning FOWC's Permanent Establishment in India.

Therefore:

> The 2017 judgment must NOT be presented as the event that directly caused F1 to leave India.

The project will explicitly separate the **event-exit timeline** from the **later tax litigation timeline**.

---

# 15. Rubric Mapping

## Problem Framing — 2 marks

We will demonstrate:

- multiple research questions
- justification for using a broad F1 dataset
- justification for the India case-study dataset
- distinction between correlation and causation

## Rigorous Data Cleaning — 2 marks

We will demonstrate:

- missing-data analysis
- justified imputation
- outlier investigation
- normalization
- unit/currency standardization
- duplicate detection
- source validation

## Statistical Depth — 2 marks

We will demonstrate:

- descriptive statistics
- skewness
- kurtosis
- distributions
- correlations
- potentially regression
- statistical interpretation

## Visualization Sophistication — 2 marks

We will use:

- time-series plots
- distributions
- box plots
- pairplots
- faceted comparisons
- correlation heatmap
- multidimensional scatter plots

Every visualization must answer a question.

## Insightful Interpretation — 2 marks

We will connect:

**Data → Pattern → Comparison → Context → Interpretation**

The final interpretation will combine quantitative findings with documented historical/legal/business evidence without claiming unsupported causation.

---

# 16. Project Phases

## Phase 0 — Research Design

**Goal:** Freeze the project scope.

Deliverables:

- final title
- research questions
- dataset schema
- data dictionary
- source strategy

---

## Phase 1 — Data Acquisition

**Goal:** Collect raw data.

Deliverables:

- raw F1 dataset
- raw India dataset
- legal/business context dataset
- source records

No heavy cleaning yet.

---

## Phase 2 — Data Cleaning

**Goal:** Produce reliable analysis-ready datasets.

Tasks:

- remove duplicates
- standardize columns
- handle missing values
- standardize units
- normalize currencies
- identify outliers
- validate records

Deliverable:

`f1_races_clean.csv`

`india_gp_clean.csv`

---

## Phase 3 — Data Validation

**Goal:** Make sure the cleaned data is trustworthy.

Checks:

- row counts
- duplicate records
- impossible values
- inconsistent dates
- inconsistent circuit names
- missingness
- source verification

Deliverable:

`data_quality_report.md`

---

## Phase 4 — Exploratory Analysis

**Goal:** Understand the dataset before making conclusions.

Tasks:

- descriptive statistics
- distributions
- trends
- outliers
- correlations
- comparisons

Deliverable:

EDA notebook.

---

## Phase 5 — Statistical Analysis

**Goal:** Add the statistical depth required by the rubric.

Tasks:

- skewness
- kurtosis
- distribution analysis
- correlation analysis
- optional regression
- group comparisons

Deliverable:

statistical analysis notebook/report.

---

## Phase 6 — India Deep Dive

**Goal:** Apply the broader findings to the Indian GP.

Tasks:

- 2011–2013 attendance analysis
- comparison with other races
- commercial data analysis
- financial structure
- tax/legal timeline
- anomaly/context analysis

Deliverable:

India case-study section.

---

## Phase 7 — Visualization

**Goal:** Build the final analytical visualizations.

Every chart must have:

- clear question
- appropriate chart type
- labels
- units
- interpretation

---

## Phase 8 — Insights & Conclusions

**Goal:** Answer the research questions.

Structure:

1. Finding
2. Evidence
3. Interpretation
4. Limitation
5. Broader implication

Avoid unsupported statements such as:

> "Taxation caused F1 to leave India."

Instead:

> "The data shows X, while contemporary/legal sources document Y. Together, these indicate Z, although the available data does not establish a single causal factor."

---

## Phase 9 — Final Presentation

Final output:

### 1. Problem Statement

### 2. Research Questions

### 3. Data Sources

### 4. Data Collection

### 5. Data Cleaning

### 6. Statistical Analysis

### 7. Visualizations

### 8. India Case Study

### 9. Key Findings

### 10. Limitations

### 11. Conclusion

---

# 17. Expected Final Data Size

Target:

| Dataset | Target |
|---|---:|
| F1 race dataset | ~190–200 rows |
| F1 variables | ~20–30 |
| India GP dataset | 3 rows |
| India variables | ~15–20 |
| Context timeline | ~10–20 events |

The exact numbers may change based on data availability.

**Data quality is more important than hitting an arbitrary row/column target.**

---

# 18. Data Quality Rules

These rules apply throughout the project.

### Rule 1
Never fabricate a value.

### Rule 2
Every externally sourced financial/legal number must have a source.

### Rule 3
Keep raw and cleaned datasets separate.

### Rule 4
Do not silently delete outliers.

### Rule 5
Do not silently impute missing values.

### Rule 6
Do not mix currencies without conversion.

### Rule 7
Record the source and confidence of difficult historical data.

### Rule 8
Do not claim causation from correlation.

### Rule 9
Do not use the 2017 Supreme Court judgment as the direct explanation for the 2013 exit.

### Rule 10
Prefer fewer reliable variables over many unreliable variables.

---

# 19. Proposed Project Folder

```text
F1_India_Case_Study/
│
├── data/
│   ├── raw/
│   │   ├── f1_races_raw.csv
│   │   ├── india_gp_raw.csv
│   │   └── india_gp_context_raw.csv
│   │
│   └── processed/
│       ├── f1_races_clean.csv
│       ├── india_gp_clean.csv
│       └── india_gp_context_clean.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   ├── 05_india_case_study.ipynb
│   └── 06_final_visualizations.ipynb
│
├── reports/
│   ├── data_quality_report.md
│   ├── findings.md
│   └── final_report.md
│
├── sources/
│   └── source_registry.csv
│
├── README.md
└── case_study.md
```

---

# 20. Source Registry

Maintain a source registry throughout the project.

Suggested columns:

```text
source_id
dataset
variable
source_name
source_url
publication_date
access_date
source_type
confidence
notes
```

This prevents the common problem of reaching the end of the project and no longer knowing where individual numbers came from.

---

# 21. Success Criteria

The project is considered successful if we have:

- ~190–200 usable F1 race observations.
- A separate detailed India dataset.
- Reliable source tracking.
- Documented data-cleaning decisions.
- Meaningful missing-data/outlier treatment.
- Skewness and kurtosis analysis.
- Distribution analysis.
- Multidimensional visualization.
- Comparative analysis of India against other races.
- A documented India business/tax/legal timeline.
- Clear separation between data-driven findings and contextual interpretation.
- Answers to the research questions supported by evidence.

---

# 22. Final Project Philosophy

The project should **not start with the conclusion**:

> "Taxes caused F1 to leave India."

Instead, the workflow is:

**Collect data**

↓

**Clean and validate**

↓

**Explore the broader F1 dataset**

↓

**Find patterns**

↓

**Compare India against the broader population**

↓

**Investigate the Indian GP in detail**

↓

**Add documented financial/legal/business context**

↓

**Determine what the evidence supports**

↓

**State limitations**

This keeps the project genuinely exploratory and aligned with the EDA rubric.
