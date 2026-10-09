# Research Findings & Exploratory Data Analysis Report
## Commercial Feasibility of Formula 1 & The Indian Grand Prix Case Study (2011–2013)

---

## 1. Executive Summary

This report presents a reproducible, evidence-based Exploratory Data Analysis (EDA) investigating the commercial sustainability of the Formula 1 Indian Grand Prix (2011–2013) held at the Buddh International Circuit (BIC) in Greater Noida, Uttar Pradesh. Benchmarked against an audited **10-season historical baseline (2010–2019, $N=198$ races)**, this study evaluates attendance trajectories, macroeconomic positioning, escalating foreign exchange burdens, and documented regulatory hurdles.

The analytical framework strictly separates **three distinct levels of evidence**:
1. **Level 1 (Direct Empirical Data):** Official sporting results, verified turnstile attendance gate counts, published ticket rate cards, and statutory financial disclosures.
2. **Level 2 (Statistical Inferences & Associations):** Distributional moments, non-parametric continental comparisons, Spearman rank correlations, and multivariate OLS regression.
3. **Level 3 (Documentary & Regulatory Context):** High Court tax escrow mandates, Customs Department classifications, promoter corporate debt disclosures, and the post-exit 2017 Supreme Court Permanent Establishment (PE) ruling.

### Key Empirical Findings:
- **Attendance Decay Trajectory:** Following an inaugural sell-out debut of **95,000 Sunday spectators (73.7th percentile globally)** in 2011, attendance declined sharply by **-31.58%** to **65,000 (35.4th percentile)** in 2012 and **60,000 (22.7th percentile)** in 2013 (cumulative decay of **-36.84%**).
- **Compounding Commercial Squeeze:** The promoter's contractual hosting fee escalated by 5% annually in US Dollars (**$40.0M in 2011 $\rightarrow$ $44.1M in 2013**), while simultaneous depreciation of the Indian Rupee (**46.67 $\rightarrow$ 58.60 INR/USD**) expanded the domestic currency hosting fee burden by **+38.44%** (from **₹186.68 Crore to ₹258.43 Crore**).
- **Structural Operating Deficit (Scenario Analysis):** Under central revenue scenarios after statutory 25% entertainment tax escrow deductions, net gate receipts (**$26.25M in 2011, $15.06M in 2012, $11.71M in 2013**) covered only 27% to 66% of the hosting fee alone. Total event outlays (**$55.0M $\rightarrow$ $57.6M**) produced estimated operational deficits expanding from **-$28.75M in 2011** to **-$45.89M in 2013** (even under high-revenue optimistic assumptions, 2013 operational deficit reached **-$42.07M**).
- **Temporal Decoupling of Legal Timeline:** The event was discontinued operationally in **December 2013** (omitted from the 2014 FIA calendar) due to cumulative private promoter insolvency, currency depreciation, and customs bonding frictions. The landmark Supreme Court ruling (*FOWC vs CIT*) establishing Permanent Establishment tax liability occurred in **April 2017**, over three years after the race had exited the calendar.

---

## 2. Research Questions & Methodological Framing

| Research Question | Focus & Scope | Methodological Approach |
|---|---|---|
| **Primary RQ** | Commercial sustainability of Indian GP vs Global Baseline | Two-tier comparative EDA ($N=198$ baseline vs $N=3$ case study) |
| **RQ1 (Attendance Trajectory)** | Gate attendance evolution at BIC (2011–2013) | Time-series decay analysis; Sunday vs 3-day weekend turnouts |
| **RQ2 (Comparative Positioning)** | Global and regional benchmarking | Percentile ranking against 198 races; continental Kruskal-Wallis & Mann-Whitney U tests |
| **RQ3 (Attendance Drivers)** | Statistical correlates of race attendance | Spearman rank correlation matrix; multivariate OLS regression |
| **RQ4 (Commercial Feasibility)** | Hosting fees, ticketing tariffs, and cashflow | Multi-scenario financial simulation (Low, Central, High) & FX stress modeling |
| **RQ5 (Circuit Characteristics)** | Track speed, layout, and sporting dynamics | Circuit length vs winning speed benchmarking; outlier audits |
| **RQ6 (Documentary Integration)** | Regulatory, taxation, and judicial context | Chronological source-registry mapping; decoupling 2013 exit from 2017 ruling |

---

## 3. Data Architecture, Sourcing & Quality Assessment

### 3.1. Sourced Datasets
1. **`data/processed/f1_races_clean.csv` ($N=198$ rows, 29 variables):** Global championship rounds (2010–2019) sourced from the Jolpica F1 API (`SRC_01`), official FOM attendance reports (`SRC_02`), and motorsport databases (`SRC_03`).
2. **`data/processed/india_gp_clean.csv` ($N=3$ rows, 24 variables):** Canonical promoter gate disclosures (`SRC_05`), contractual hosting fee schedules (`SRC_06`), BookMyShow rate cards (`SRC_07`), and RBI exchange rates (`SRC_12`).
3. **`data/processed/india_gp_context_clean.csv` ($N=15$ events, 10 fields):** Audited chronology of judicial rulings, customs bonding, and promoter balance sheet events (`SRC_08`, `SRC_09`, `SRC_10`, `SRC_11`).
4. **`sources/source_registry.csv` ($N=12$ primary entries):** Full citation metadata, court case identifiers, gazette numbers, URLs, and confidence ratings.

### 3.2. Data Quality & Cleaning Actions
- **Key Integrity:** Verified 0 duplicate keys across `race_id` and composite keys `(season, round)`.
- **Discrepancy Resolution:** Resolved an initial multiplier artifact in raw weekend attendance files by synchronizing Indian GP records to official promoter disclosures (`SRC_05`):
  - 2011: 95,000 Race Day / 110,000 Weekend
  - 2012: 65,000 Race Day / 95,000 Weekend
  - 2013: 60,000 Race Day / 65,000 Weekend
- **Confidence Stratification:** Classified attendance into High Confidence (48.5%), Medium Confidence (44.4%), and Low Confidence (7.1%).

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

### 4.2. Normality & Non-Parametric Group Differences
Formal normality testing confirms that race-day attendance and key covariates violate normality:
- **`attendance_race_day`:** Shapiro-Wilk $W = 0.954$, $p = 6.47 \times 10^{-6}$ (Reject $H_0$).
- **`winning_margin_s`:** Shapiro-Wilk $W = 0.689$, $p = 1.12 \times 10^{-19}$ (Reject $H_0$; highly right-skewed).
- **`gdp_per_capita_usd`:** Shapiro-Wilk $W = 0.941$, $p = 3.91 \times 10^{-7}$ (Reject $H_0$).
- **Statistical Implication:** Non-parametric group tests (Kruskal-Wallis, Mann-Whitney U) and Spearman rank correlations are used for robust inference.

### 4.3. Regional Attendance Differences
- **Kruskal-Wallis across Continents:** $H = 76.14$, $p = 1.14 \times 10^{-15}$ across 5 continental regions ($N=198$).
- **Continental Summary:**
  - Oceania (Melbourne, $N=10$): Mean 103,000 | Median 101,500
  - Americas (Austin, Montreal, Mexico, Brazil, $N=33$): Mean 102,061 | Median 107,000
  - Europe (Silverstone, Spa, Monza, etc., $N=85$): Mean 79,235 | Median 75,000
  - Asia (Shanghai, Suzuka, Sepang, Yeongam, BIC, $N=51$): Mean 65,941 | Median 63,000
  - Middle East (Bahrain, Abu Dhabi, $N=19$): Mean 44,053 | Median 50,000
- **Mann-Whitney U (Europe vs Asia):** $U = 2776.0$, $p = 0.0062$. European events exhibited significantly higher median attendance (75,000) than Asian events (63,000).
- **Sensitivity Audit (Excluding Low-Confidence Records, $N=184$):** Kruskal-Wallis yields $H = 67.82, p = 6.53 \times 10^{-14}$, confirming that regional divergence is not an artifact of low-confidence estimates.

### 4.4. Bivariate Correlation Matrix (Spearman Rank)

| Relationship | Sample Size | Spearman $\rho$ | $p$-value | Practical Interpretation |
|---|:---:|:---:|:---:|---|
| Attendance vs GDP per Capita | $N=198$ | $+0.24$ | $0.0006$ | Moderate positive association with host nation economic affluence. |
| Attendance vs Event Tenure | $N=198$ | $+0.38$ | $3.8 \times 10^{-8}$ | Established heritage events draw larger crowds than newly added circuits. |
| Speed vs Circuit Length | $N=198$ | $+0.46$ | $1.2 \times 10^{-11}$ | Longer permanent tracks feature longer straights and higher average speeds. |
| Attendance vs Average Speed | $N=198$ | $+0.08$ | $0.262$ | No statistically significant association between track speed and gate attendance. |
| Winning Margin vs Finishers | $N=198$ | $-0.18$ | $0.011$ | Modest inverse correlation; higher attrition correlates with larger winning gaps. |

### 4.5. Multivariate OLS Regression Analysis
To model baseline associations between attendance, host economic affluence, track heritage, and race configuration:

$$\text{Attendance} = \beta_0 + \beta_1 \ln(\text{GDP per Capita}) + \beta_2 \text{Tenure} + \beta_3 \mathbb{I}_{\text{Permanent}} + \beta_4 \mathbb{I}_{\text{Street}} + \beta_5 \text{Race Distance} + \epsilon$$

- **Model Diagnostics:** $R^2 = 0.365$, Adjusted $R^2 = 0.349$, $F(5, 192) = 22.08$, $p = 1.88 \times 10^{-17}$.
- **Coefficients & Unit Interpretation:**
  - **$\ln(\text{GDP per Capita})$:** $\beta = 5,143.6$ ($t = 2.37, p = 0.019$). Because GDP is log-transformed, multiplying host GDP per capita by $e \approx 2.718$ is associated with ~5,144 additional Sunday spectators (a 10% increase in GDP per capita is associated with $\approx 5,143.6 \times \ln(1.10) \approx 490$ additional spectators), controlling for tenure and layout.
  - **`event_tenure_years`:** $\beta = 487.9$ ($t = 6.14, p < 0.001$). Each additional year an event has been on the championship calendar is associated with ~488 additional spectators.
  - **`circuit_type`:** Dedicated Permanent circuits ($\beta = -29,310, p < 0.001$) and Street circuits ($\beta = -33,300, p < 0.001$) exhibit lower baseline crowds relative to high-capacity hybrid/festival venues (e.g. Albert Park).
  - **`race_distance_km`:** $\beta = 655.1$ ($t = 3.71, p < 0.001$).
- **Methodological Guardrail:** This regression estimates baseline statistical associations across 198 races; it does not constitute a causal forecasting model for individual circuit viability.

---

## 5. Indian Grand Prix Case Study Deep-Dive

### 5.1. Gate Attendance Trajectory at Buddh International Circuit

| Edition | Sunday Attendance | YoY Change | Baseline Percentile Rank | Weekend Attendance | YoY Change | Weekend-to-Sunday Ratio |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **2011** | 95,000 | — | **73.7th** (higher than 146 of 198 races) | 110,000 | — | 1.16 |
| **2012** | 65,000 | **-31.58%** | **35.4th** (higher than 70 of 198 races) | 95,000 | **-13.64%** | 1.46 |
| **2013** | 60,000 | **-7.69%** | **22.7th** (higher than 45 of 198 races) | 65,000 | **-31.58%** | 1.08 |

- **Observation:** The inaugural 2011 race benefited from massive novelty interest. By 2013, Sunday attendance had fallen by **-36.84%** from its debut, dropping BIC into the lower quartile of global Grand Prix attendances.

### 5.2. Compounding Commercial Squeeze: Escalating Fees & FX Depreciation

| Season | Contractual Hosting Fee ($M USD) | RBI Mean USD/INR Rate | Domestic Hosting Fee Burden (₹ Crore) | Effective INR Fee Growth vs 2011 |
|:---:|:---:|:---:|:---:|:---:|
| **2011** | $40.0M | 46.67 | ₹186.68 Cr | Baseline |
| **2012** | $42.0M | 53.44 | ₹224.45 Cr | **+20.23%** |
| **2013** | $44.1M | 58.60 | ₹258.43 Cr | **+38.44%** |

- **The FX Mechanism:** While the USD contract fee escalated at 5.0% annually (+10.25% cumulative), the Indian Rupee depreciated by **25.56%** against the USD over the same 2-year window. The promoter's domestic currency hosting obligations expanded by **₹71.75 Crore (+38.44%)** between 2011 and 2013.

### 5.3. Promoter Operating Cashflow Scenarios & Sensitivity Analysis
Because audited promoter income statements are proprietary to Jaypee Sports International Ltd (JPSI), gate revenues are evaluated under three transparent, illustrative scenarios based on published BookMyShow rate cards (₹1,500 to ₹35,000) minus mandatory deductions:
- **Deductions:** 25% UP State Entertainment Tax escrow (Allahabad High Court order `SRC_10`) + 5% ticketing commission / banking processing fees (Net realization factor = 0.70).
- **Conservative (Low) Scenario:** Lower corporate box uptake, 15% complimentary/sponsor seat leakage.
- **Central (Base) Scenario:** Expected ticket tier distribution, 10% complimentary seat mix.
- **Optimistic (High) Scenario:** High corporate box sell-out, minimal complimentary seat leakage.

| Season | Hosting Fee ($M) | Ops Logistics ($M) | Total Cost ($M) | Net Revenue: Low ($M) | Net Revenue: Central ($M) | Net Revenue: High ($M) | Deficit: Low ($M) | Deficit: Central ($M) | Deficit: High ($M) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **2011** | $40.0M | $15.0M | $55.0M | $18.75M | $26.25M | $32.25M | **-$36.25M** | **-$28.75M** | **-$22.75M** |
| **2012** | $42.0M | $14.0M | $56.0M | $10.48M | $15.06M | $19.65M | **-$45.52M** | **-$40.94M** | **-$36.35M** |
| **2013** | $44.1M | $13.5M | $57.6M | $8.12M | $11.71M | $15.53M | **-$49.48M** | **-$45.89M** | **-$42.07M** |

- **Analytical Takeaway:** Under all three scenarios, net gate revenues covered only a fraction of unavoidable event obligations, resulting in structural operational deficits exceeding **-$22M to -$49M annually** (cumulative 3-year operating deficit of **-$115.58M** in the central scenario), excluding debt servicing on the **~$400M circuit construction capital expenditure**.

---

## 6. Documentary & Regulatory Context Integration

### 6.1. Regulatory Classifications & Tax Disputes (2011–2013)
1. **Sports vs Entertainment Classification (`SRC_11`):** Ministry of Youth Affairs and Sports (MYAS) declined to recognize Formula 1 as a priority sport under the National Sports Development Code 2011, classifying it as commercial entertainment. This denied the event customs duty exemptions for imported racing chassis, tyres, and broadcasting gear.
2. **Customs Bonding Guarantees (`SRC_11`):** CBEC Notification No. 153/94-Customs mandated full ATA Carnet bank indemnity guarantees to ensure all imported motorsport equipment left India post-race without duty leakage.
3. **UP Entertainment Tax Dispute (`SRC_10`):** In *Jaypee Sports International Ltd. vs. State of U.P.* (Civil Misc. Writ Petition No. 1528 of 2011), the Allahabad High Court directed that 25% of gross ticket sales proceeds be deposited into an interest-bearing escrow account pending adjudication under Section 3 of the U.P. Entertainment and Betting Tax Act, 1979.

### 6.2. Decoupling the 2013 Exit from the 2017 Supreme Court Ruling
- **Operational Discontinuation (December 2013):** The Indian Grand Prix was omitted from the 2014 FIA World Championship calendar released in late 2013. F1 commercial chief Bernie Ecclestone and JPSI cited logistical calendar shifts, promoter financial strain, and unresolved administrative/taxation issues.
- **Post-Exit Judicial Ruling (April 2017, `SRC_09`):** In *Formula One World Championship Ltd. vs. Commissioner of Income Tax* (Civil Appeal No. 3849 of 2017, reported in [2017] 394 ITR 80 SC), the Supreme Court of India ruled that BIC constituted a **Fixed Place Permanent Establishment (PE)** under Article 5(1) of the India-UK Double Tax Avoidance Agreement (DTAA), making FOWC liable for Indian corporate income tax on race royalties received from JPSI.
- **Analytical Integrity Rule:** The 2017 Supreme Court judgment did **not** cause the cancellation of the 2014 Grand Prix; rather, it affirmed the Indian tax authorities' jurisdiction over foreign motorsport royalties years after the promoter had ceased operations.

---

## 7. Master Figure Inventory & Exhibits

| Exhibit | Figure Filename | Focus & Research Question | Key Takeaway |
|:---:|---|---|---|
| **Fig 1** | `reports/figures/fig1_attendance_distribution_with_india.png` | Global Distribution Overlay (RQ1, RQ2) | India 2011 was 73.7th percentile; by 2013, it dropped to the bottom 22.7th percentile. |
| **Fig 2** | `reports/figures/fig2_indian_gp_decay_curve.png` | Indian GP Attendance Decay (RQ1) | Sunday attendance experienced a rapid 36.8% decay across 3 editions. |
| **Fig 3** | `reports/figures/fig3_regional_attendance_comparison.png` | Regional Continental Benchmarks (RQ2) | Asian Grand Prix events exhibit lower median attendance than European and American rounds. |
| **Fig 4** | `reports/figures/fig4_multivariate_correlation_matrix.png` | Spearman Correlation Matrix (RQ3) | Event tenure ($\rho=0.38$) and GDP per capita ($\rho=0.24$) correlate positively with attendance. |
| **Fig 5** | `reports/figures/fig5_attendance_vs_gdp_multidimensional.png` | Multidimensional Attendance vs GDP (RQ3, RQ5) | India sits as a low-GDP per capita outlier with high initial attendance capacity. |
| **Fig 6** | `reports/figures/fig6_commercial_deficit_and_hosting_fee.png` | Financial Squeeze & Cashflow Deficit (RQ4) | Compounding USD fee growth (+10.25%) and INR depreciation (+38.44%) widened cash deficits. |
| **Fig 7** | `reports/figures/fig7_historical_context_timeline.png` | Chronological Timeline (RQ6) | Distinguishes the 2013 operational exit from the 2017 Supreme Court Permanent Establishment ruling. |
| **Fig 8** | `reports/figures/fig8_circuit_characteristics_radar_speed.png` | Track Speed Benchmark (RQ5) | BIC was among the fastest permanent circuits on the calendar (207.7 km/h mean speed). |

---

## 8. Limitations & Methodological Guardrails

1. **Small Sample Size for Indian GP ($N=3$):** Statistical models cannot establish causal causality from 3 event observations. The global baseline ($N=198$) provides comparative context, while financial and legal records provide explanatory mechanisms.
2. **Attendance as a Commercial Proxy:** Gate attendance does not equal profitability; events with modest crowds (e.g. Monaco, Bahrain) remain commercially viable through government subsidies or premium corporate hospitality.
3. **Absence of Fully Disclosed Promoter Balance Sheets:** Financial cashflows represent modeled scenarios based on published ticket tier tariffs, disclosed capex, and contractual hosting fee structures.

---

## 9. Conclusion

The discontinuation of the Indian Grand Prix resulted from a structural convergence of:
1. **Attendance Decay:** A 36.8% collapse in gate turnout following inaugural novelty.
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
- `[SRC_06]` Forbes / Formula Money (Christian Sylt, 13 March 2015). *The Cost of Hosting Formula One*.
- `[SRC_07]` BookMyShow / JPSI (2011–2013). *Official Indian Grand Prix Ticketing Tariff Cards*.
- `[SRC_08]` Jaiprakash Associates Limited (2012). *33rd Annual Report FY 2011–12 (Note 29: Consolidated Balance Sheet Capex)*.
- `[SRC_09]` Supreme Court of India (2017). *Formula One World Championship Ltd. vs. CIT (Civil Appeal No. 3849/2017, [2017] 394 ITR 80 SC)*.
- `[SRC_10]` Allahabad High Court (2011). *Jaypee Sports International Ltd. vs. State of U.P. (Civil Misc. Writ Petition No. 1528/2011)*.
- `[SRC_11]` Central Board of Excise and Customs & MYAS (2011). *CBEC Notification No. 153/94-Cus & Sports Classification*.
- `[SRC_12]` Reserve Bank of India (2024). *Handbook of Statistics on the Indian Economy (Table 149: INR/USD Reference Rates)*.
