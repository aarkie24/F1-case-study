# F1 Indian Grand Prix: Commercial Sustainability & Exploratory Data Analysis

## Project Overview
This repository contains an Exploratory Data Analysis (EDA) and case study examining the commercial sustainability of Formula 1 events, with a focused investigation into the **2011–2013 Indian Grand Prix** held at the Buddh International Circuit (BIC) in Greater Noida, India.

The project employs a **two-tier data architecture**:
1. **Global Baseline Dataset (2010–2019):** ~198 Formula 1 races analyzing sporting performance, circuit parameters, geographic trends, and spectator attendance.
2. **Indian Grand Prix Deep-Dive (2011–2013):** Granular examination of gate attendance decay, ticketing structures, hosting fee burdens, capital expenditure, and operating economics.
3. **Contextual Timeline (2007–2017):** Documented trajectory of regulatory hurdles, customs bonding, entertainment tax disputes, and the subsequent Supreme Court permanent establishment ruling.

---

## Repository Structure

```text
├── case_study.md                 # Project assignment guidelines and evaluation rubric
├── plan.md                       # Master execution plan (Phases 0 to 9)
├── README.md                     # Project overview and navigation
│
├── data/
│   ├── raw/                      # Unaltered raw datasets
│   │   ├── f1_races_raw.csv
│   │   ├── india_gp_raw.csv
│   │   └── india_gp_context_raw.csv
│   │
│   └── processed/                # Validated, cleaned, and normalized datasets
│       ├── f1_races_clean.csv
│       ├── india_gp_clean.csv
│       ├── india_gp_context_clean.csv
│       └── data_dictionary.md    # Schema, types, units, and validation rules
│
├── notebooks/                    # Analytical and computational pipeline
│   ├── 01_data_collection.ipynb  # Phase 1: API harvesting & source compilation
│   ├── 02_data_cleaning.ipynb    # Phase 2: Missingness, imputation & normalization
│   ├── 03_eda.ipynb              # Phase 4: Univariate, bivariate & regional EDA
│   ├── 04_statistical_analysis.ipynb # Phase 5: Skewness, distributions & regressions
│   ├── 05_india_case_study.ipynb # Phase 6: India comparative deep dive
│   └── 06_visualizations.ipynb   # Phase 7: Master publication charts
│
├── reports/                      # Formal academic and findings reports
│   ├── data_quality_report.md    # Audit of missing values, outliers, and data health
│   ├── findings.md               # Synthesis of findings, patterns, and context
│   └── final_report.md           # Master final report mapped to grading rubric
│
└── sources/
    └── source_registry.csv       # Sourcing provenance, citations, and confidence scores
```

---

## Analytical Guardrails
- **Distinction of Evidence:** Distinguishes empirical data from statistical inference and documentary legal evidence.
- **Temporal Integrity:** Disentangles the race exit timeline (last race in 2013, dropped from 2014) from post-exit litigation (2017 Supreme Court ruling).
- **Zero Fabrication:** Rigorous missingness logging and justified imputation.
