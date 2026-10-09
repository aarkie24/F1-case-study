# Research Findings & Exploratory Data Analysis Report
## Commercial Feasibility of Formula 1 & The Indian Grand Prix Case Study (2011–2013)

---

## 1. Executive Summary

This study presents a data-driven, empirical Exploratory Data Analysis (EDA) investigating the commercial sustainability of the Formula 1 Indian Grand Prix (2011–2013) held at the Buddh International Circuit (BIC) in Greater Noida, Uttar Pradesh. To establish a robust statistical foundation, the research benchmarks the three Indian Grand Prix editions against a **10-season historical baseline (2010–2019, $N=198$ races)** encompassing sporting performance, circuit engineering, spectator attendance, and macroeconomic indicators.

The analytical architecture strictly separates **three distinct levels of evidence**:
1. **Level 1 (Direct Empirical Data):** Sourced race results, verified turnstile attendance, and statutory financial figures.
2. **Level 2 (Statistical Inferences):** Distributional moments, non-parametric group comparisons, Spearman rank correlations, and OLS regression modeling.
3. **Level 3 (Documentary Context):** Judicial decisions, customs classifications, contractual terms, and promoter corporate disclosures.

### Key Empirical Findings:
- **Attendance Decay Curve:** After a near capacity debut of **95,000 Sunday spectators (87th percentile globally)** in 2011, attendance declined sharply by **-31.58%** to **65,000 (37th percentile)** in 2012 and **60,000 (27th percentile)** in 2013.
- **Compounding Commercial Squeeze:** The promoter's contractual hosting fee escalated by 5% annually in US Dollars (**$40.0M in 2011 $\rightarrow$ $44.1M in 2013**), while simultaneous depreciation of the Indian Rupee (**46.67 $\rightarrow$ 58.60 INR/USD**) expanded the domestic currency hosting fee burden by **+38.44%** (from **₹186.68 Crore to ₹258.43 Crore**).
- **Structural Operating Cashflow Deficit:** Estimated gate revenues (**$26.5M in 2011, $15.2M in 2012, $11.8M in 2013**) fell significantly below total event outlays (**$55.0M $\rightarrow$ $57.6M**), resulting in estimated operational deficits expanding from **-$28.5M in 2011** to **-$45.8M in 2013**.
- **Temporal Decoupling of Legal Timeline:** The event was discontinued operationally in **December 2013** (omitted from the 2014 FIA calendar) due to cumulative commercial, tax bonding, and scheduling factors. The landmark Supreme Court ruling (*FOWC vs CIT*) establishing Permanent Establishment tax liability occurred in **April 2017**, over three years after the race had exited the calendar.

---

## 2. Research Questions & Methodological Framing

| Research Question | Focus & Scope | Methodological Approach |
|---|---|---|
| **Primary RQ** | Commercial sustainability of Indian GP vs Global Baseline | Two-tier comparative EDA ($N=198$ baseline vs $N=3$ case study) |
| **RQ1 (Attendance Trajectory)** | Gate attendance evolution at BIC (2011–2013) | Time-series decay analysis; Sunday vs 3-day weekend turnouts |
| **RQ2 (Comparative Positioning)** | Global and regional benchmarking | Percentile ranking against 198 races; continental Kruskal-Wallis & Mann-Whitney U tests |
| **RQ3 (Attendance Drivers)** | Correlates of race attendance | Spearman rank correlation matrix; multivariate OLS regression |
| **RQ4 (Commercial Feasibility)** | Hosting fees, ticketing tariffs, and cashflow | Financial modeling of gate revenue vs escalating fees and FX depreciation |
| **RQ5 (Circuit Characteristics)** | Track speed, layout, and sporting dynamics | Circuit length vs speed benchmarking; outlier audits |
| **RQ6 (Documentary Integration)** | Regulatory, taxation, and judicial context | Chronological source-registry mapping; decoupling 2013 exit from 2017 ruling |

---

## 3. Data Architecture, Sourcing & Quality Assessment

### 3.1. Sourced Datasets
1. **`data/processed/f1_races_clean.csv` ($N=198$ rows, 29 variables):** Global championship rounds (2010–2019) sourced from the Jolpica F1 API (`SRC_01`), official FOM attendance reports (`SRC_02`), and motorsport databases (`SRC_03`).
2. **`data/processed/india_gp_clean.csv` ($N=3$ rows, 24 variables):** Canonical promoter gate disclosures (`SRC_05`), contractual hosting fee schedules (`SRC_06`), BookMyShow rate cards (`SRC_07`), and RBI exchange rates (`SRC_12`).
3. **`data/processed/india_gp_context_clean.csv` ($N=15$ events, 10 fields):** Audited chronology of judicial rulings, customs bonding, and promoter balance sheet events (`SRC_08`, `SRC_09`, `SRC_10`, `SRC_11`).
4. **`sources/source_registry.csv` ($N=12$ primary entries):** Full citation metadata, URLs, publication dates, and confidence ratings.

### 3.2. Data Quality & Cleaning Actions
- **Key Integrity:** Verified 0 duplicate keys across `race_id` and composite keys `(season, round)`.
- **Discrepancy Resolution:** Resolved an initial multiplier artifact in raw weekend attendance files by synchronizing Indian GP records to official promoter disclosures (`SRC_05`):
  - 2011: 95,000 Race Day / 110,000 Weekend
  - 2012: 65,000 Race Day / 95,000 Weekend
  - 2013: 60,000 Race Day / 65,000 Weekend
- **Confidence Stratification:** Classified attendance into High Confidence (52.5%), Medium Confidence (39.4%), and Low Confidence (8.1%).

---

## 4. Exploratory Data Analysis & Statistical Findings

### 4.1. Baseline Descriptive Statistics ($N=198$)

| Variable | Mean | Median | Std Dev | Min | Max | IQR | Skewness | Kurtosis |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `attendance_race_day` | 74,482 | 70,000 | 25,607 | 25,000 | 141,000 | 36,750 | 0.63 | -0.16 |
| `attendance_weekend` | 179,338 | 165,000 | 73,431 | 50,000 | 351,000 | 100,500 | 0.44 | -0.66 |
| `average_speed_kmh` | 199.3 | 202.9 | 24.8 | 138.1 | 247.6 | 32.7 | -0.74 | 0.08 |
| `circuit_length_km` | 5.097 | 5.303 | 0.747 | 3.337 | 7.004 | 0.814 | -0.38 | 0.77 |
| `winning_margin_s` | 9.42 | 5.98 | 10.36 | 0.59 | 62.83 | 10.35 | 2.14 | 5.56 |
| `gdp_per_capita_usd` | $38,420 | $41,260 | $22,410 | $1,358 | $111,968 | $35,900 | 0.35 | -0.58 |
| `event_tenure_years` | 24.3 | 21.0 | 18.2 | 1.0 | 70.0 | 31.0 | 0.52 | -0.85 |

### 4.2. Normality & Distribution Testing
Formal normality testing demonstrates that race-day attendance, winning margin, and GDP per capita significantly deviate from normality:
- **`attendance_race_day`:** Shapiro-Wilk $W = 0.954$, $p = 6.47 \times 10^{-6}$ (Reject $H_0$).
- **`winning_margin_s`:** Shapiro-Wilk $W = 0.689$, $p = 1.12 \times 10^{-19}$ (Reject $H_0$; highly right-skewed).
- **`gdp_per_capita_usd`:** Shapiro-Wilk $W = 0.941$, $p = 3.91 \times 10^{-7}$ (Reject $H_0$).
- **Statistical Implication:** Non-parametric group tests (Kruskal-Wallis, Mann-Whitney U) and Spearman rank correlations are required for defensible inference.

### 4.3. Regional Attendance Differences
- **Kruskal-Wallis across Continents:** $H = 58.62$, $p = 5.64 \times 10^{-12}$ (Statistically significant regional variation).
- **Continental Medians:**
  - Oceania (Melbourne): 101,000 spectators
  - Americas (Austin, Montreal, Mexico, Brazil): 97,500 spectators
  - Europe (Silverstone, Spa, Monza, etc.): 75,000 spectators
  - Asia (Shanghai, Suzuka, Sepang, Yeongam, BIC): 55,000 spectators
  - Middle East (Bahrain, Abu Dhabi): 31,000 spectators
- **Mann-Whitney U (Europe vs Asia):** $U = 4692.5$, $p = 4.21 \times 10^{-7}$. European events exhibited substantially higher median attendance than Asian events.

### 4.4. Bivariate Correlation Matrix (Spearman Rank)

| Relationship | Sample Size | Spearman $\rho$ | $p$-value | Practical Interpretation |
|---|:---:|:---:|:---:|---|
| Attendance vs GDP per Capita | $N=198$ | $+0.24$ | $0.0006$ | Weak-to-moderate positive correlation with host nation economic affluence. |
| Attendance vs Event Tenure | $N=198$ | $+0.38$ | $3.8 \times 10^{-8}$ | Established heritage events draw larger crowds than newly added circuits. |
| Speed vs Circuit Length | $N=198$ | $+0.46$ | $1.2 \times 10^{-11}$ | Longer permanent tracks feature longer straights and higher average speeds. |
| Attendance vs Average Speed | $N=198$ | $+0.08$ | $0.262$ | No statistically significant relationship between track speed and gate attendance. |
| Winning Margin vs Finishers | $N=198$ | $-0.18$ | $0.011$ | Modest inverse correlation; higher attrition correlates with larger winning gaps. |

### 4.5. Multivariate OLS Regression Analysis
To evaluate whether host economic indicators and track tenure predict race-day attendance, an OLS model was estimated:

$$\text{Attendance} = \beta_0 + \beta_1 \ln(\text{GDP per Capita}) + \beta_2 \text{Tenure} + \beta_3 \mathbb{I}_{\text{Permanent}} + \beta_4 \text{Race Distance} + \epsilon$$

- **Model Fit:** $R^2 = 0.178$, Adjusted $R^2 = 0.161$, $F(4, 193) = 10.45$, $p = 8.7 \times 10^{-8}$.
- **Key Predictors:**
  - **$\ln(\text{GDP per Capita})$:** $\beta = 4,874.2$ ($t = 2.76, p = 0.006$). A 10% increase in host GDP per capita is associated with ~487 additional Sunday spectators.
  - **`event_tenure_years`:** $\beta = 362.5$ ($t = 3.84, p = 0.0002$). Each additional decade of Grand Prix hosting history adds ~3,625 spectators.
- **Model Limitations:** Macroeconomic and tenure factors explain ~18% of global attendance variance. Local ticketing strategies, national sporting culture, and promoter marketing drive the remaining unobserved variance.

---

## 5. Indian Grand Prix Case Study Deep-Dive

### 5.1. Gate Attendance Trajectory at Buddh International Circuit

| Edition | Sunday Attendance | YoY Change | Baseline Percentile | Weekend Attendance | YoY Change | Weekend-to-Sunday Ratio |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **2011** | 95,000 | — | 87.4th | 110,000 | — | 1.16 |
| **2012** | 65,000 | -31.58% | 37.4th | 95,000 | -13.64% | 1.46 |
| **2013** | 60,000 | -7.69% | 27.3rd | 65,000 | -31.58% | 1.08 |

- **Observation:** The inaugural 2011 race benefited from massive novelty interest. By 2013, Sunday attendance had fallen by **-36.84%** from its debut, placing BIC in the lower quartile of global Grand Prix attendances.

### 5.2. Compounding Commercial Pressures: Hosting Fees & FX Depreciation

| Season | Contractual Hosting Fee ($M USD) | RBI Mean USD/INR Rate | Hosting Fee Burden (₹ Crore) | Effective INR Fee Growth vs 2011 |
|:---:|:---:|:---:|:---:|:---:|
| **2011** | $40.0M | 46.67 | ₹186.68 Cr | Baseline |
| **2012** | $42.0M | 53.44 | ₹224.45 Cr | +20.23% |
| **2013** | $44.1M | 58.60 | ₹258.43 Cr | +38.44% |

- **The FX Squeeze:** While the USD contract fee escalated at 5.0% annually, the Indian Rupee depreciated by **25.56%** against the USD over the same 2-year window. The promoter's domestic currency hosting obligations expanded by **₹71.75 Crore (+38.44%)** between 2011 and 2013.

### 5.3. Promoter Operating Cashflow Model (Gate Revenue vs Event Outlays)

| Season | Est. Gate Revenue ($M USD) | Hosting Fee ($M USD) | Est. Event Ops ($M USD) | Est. Total Event Cost ($M USD) | Est. Net Cashflow Deficit ($M USD) | Gate Revenue / Hosting Fee Ratio |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **2011** | $26.5M | $40.0M | $15.0M | $55.0M | **-$28.5M** | 0.66 |
| **2012** | $15.2M | $42.0M | $14.0M | $56.0M | **-$40.8M** | 0.36 |
| **2013** | $11.8M | $44.1M | $13.5M | $57.6M | **-$45.8M** | 0.27 |

- **Commercial Reality:** Under standard F1 promoter agreements, Formula One Group retained all global broadcasting rights, trackside advertising, and title sponsorship revenues. The promoter (JPSI) was solely reliant on local gate receipts and concessions, covering only 27% to 66% of the contractual hosting fee alone.

---

## 6. Documentary & Regulatory Context Integration

### 6.1. Regulatory Classifications & Tax Disputes (2011–2013)
1. **Sports vs Entertainment Classification (`SRC_11`):** The Ministry of Youth Affairs and Sports declined to recognize Formula 1 as a priority sport, classifying it as commercial entertainment. This denied the event customs duty exemptions for imported racing chassis, tyres, and broadcasting gear.
2. **Customs Bonding Guarantees (`SRC_11`):** The Central Board of Excise and Customs (CBEC) mandated full ATA Carnet bank guarantees to ensure all imported motorsport equipment left India post-race.
3. **UP Entertainment Tax Dispute (`SRC_10`):** The Government of Uttar Pradesh levied state entertainment tax on ticket sales. In October 2011, the Allahabad High Court directed that 25% of ticket sale proceeds be deposited into an escrow account pending legal resolution.

### 6.2. Decoupling the 2013 Exit from the 2017 Supreme Court Ruling
- **Operational Discontinuation (December 2013):** The Indian Grand Prix was omitted from the 2014 FIA World Championship calendar released in late 2013. F1 commercial chief Bernie Ecclestone and JPSI cited logistical calendar shifts and unresolved administrative/taxation issues.
- **Post-Exit Judicial Ruling (April 2017, `SRC_09`):** In *Formula One World Championship Ltd vs Commissioner of Income Tax* (Civil Appeal No. 3849/2017), the Supreme Court of India ruled that BIC constituted a **Fixed Place Permanent Establishment (PE)** under Article 5(1) of the India-UK Double Tax Avoidance Agreement (DTAA), making FOWC liable for Indian corporate income tax on race royalties.
- **Analytical Integrity Rule:** The 2017 Supreme Court judgment did **not** cause the cancellation of the 2014 Grand Prix; rather, it affirmed the Indian tax authorities' jurisdiction over foreign motorsport income years after the promoter had ceased operations.

---

## 7. Master Figure Inventory & Exhibits

| Exhibit | Figure Filename | Focus & Research Question | Key Takeaway |
|:---:|---|---|---|
| **Fig 1** | `reports/figures/fig1_attendance_distribution_with_india.png` | Global Distribution Overlay (RQ1, RQ2) | India 2011 was 87th percentile; by 2013, it dropped to the bottom 27th percentile. |
| **Fig 2** | `reports/figures/fig2_indian_gp_decay_curve.png` | Indian GP Attendance Decay (RQ1) | Sunday attendance experienced a rapid 36.8% decay across 3 editions. |
| **Fig 3** | `reports/figures/fig3_regional_attendance_comparison.png` | Regional Continental Benchmarks (RQ2) | Asian Grand Prix events exhibit lower median attendance than European and American rounds. |
| **Fig 4** | `reports/figures/fig4_multivariate_correlation_matrix.png` | Spearman Correlation Matrix (RQ3) | Event tenure ($\rho=0.38$) and GDP per capita ($\rho=0.24$) correlate positively with attendance. |
| **Fig 5** | `reports/figures/fig5_attendance_vs_gdp_multidimensional.png` | Multidimensional Attendance vs GDP (RQ3, RQ5) | India sits as a low-GDP per capita outlier with high initial attendance capacity. |
| **Fig 6** | `reports/figures/fig6_commercial_deficit_and_hosting_fee.png` | Financial Squeeze & Cashflow Deficit (RQ4) | Compounding USD fee growth (+10.2%) and INR depreciation (+38.4%) widened cash deficits. |
| **Fig 7** | `reports/figures/fig7_historical_context_timeline.png` | Chronological Timeline (RQ6) | Distinguishes the 2013 operational exit from the 2017 Supreme Court Permanent Establishment ruling. |
| **Fig 8** | `reports/figures/fig8_circuit_characteristics_radar_speed.png` | Track Speed Benchmark (RQ5) | BIC was among the fastest permanent circuits on the calendar (207.7 km/h mean speed). |

---

## 8. Limitations & Methodological Guardrails

1. **Small Sample Size for Indian GP ($N=3$):** Statistical models cannot establish causal causality from 3 event observations. The global baseline ($N=198$) provides comparative context, while financial and legal records provide explanatory mechanisms.
2. **Attendance Opacity in Select Emerging Markets:** Attendance figures for certain Asian and Middle Eastern events are self-reported by promoters without independent ticket turnstile audits.
3. **Absence of Fully Disclosed Promoter Balance Sheets:** Financial cashflows represent modeled estimates based on published ticket tier tariffs, disclosed capex, and contractual hosting fee structures.

---

## 9. Conclusion

The discontinuation of the Indian Grand Prix was not caused by a single isolated event, but by the convergence of:
1. **Rapid Attendance Decay:** A 36.8% collapse in gate turnout from inaugural excitement.
2. **Severe Commercial Imbalance:** Compounding USD hosting fees combined with sharp INR currency depreciation in an unsubsidized, private promoter model.
3. **Administrative & Taxation Friction:** Lack of sports status, customs duty bonding demands, and state entertainment tax escrow requirements.
4. **Corporate Distress of Promoter:** Over-leveraged balance sheets of the parent conglomerate (Jaiprakash Associates Ltd) amidst massive circuit capital expenditures (~$400M).

---

## 10. References & Source Registry Mapping

- `[SRC_01]` Jolpica F1 API / Ergast Database (2024). *Historical Formula 1 World Championship Results (2010–2019)*.
- `[SRC_02]` Formula One Management (2017). *Formula 1 Annual Global Attendance Disclosures*.
- `[SRC_03]` RaceFans Motorsport Database (2019). *Grand Prix Spectator Attendance Archive*.
- `[SRC_04]` World Bank Open Data (2024). *GDP per Capita (Current US$) Series NY.GDP.PCAP.CD*.
- `[SRC_05]` Jaypee Sports International & Autosport (2013). *Official Airtel Indian Grand Prix Attendance Gate Disclosures*.
- `[SRC_06]` Forbes / Formula Money (2015). *The Cost of Hosting Formula One*.
- `[SRC_07]` BookMyShow / JPSI (2011–2013). *Official Indian Grand Prix Ticketing Tariff Cards*.
- `[SRC_08]` Jaiprakash Associates Limited (2012). *Annual Corporate Financial Disclosures & Circuit Capex Notes*.
- `[SRC_09]` Supreme Court of India (2017). *Formula One World Championship Ltd vs CIT (Civil Appeal No. 3849/2017)*.
- `[SRC_10]` Allahabad High Court (2011). *Jaypee Sports International Ltd vs State of Uttar Pradesh*.
- `[SRC_11]` Central Board of Excise and Customs (2011). *Customs Tariff & Bonding Notifications for Motorsport Cargo*.
- `[SRC_12]` Reserve Bank of India (2024). *Historical INR/USD Annual Reference Exchange Rates*.
