# Data Dictionary & Schema Specification (Clean & Engineered Layers)

## 1. Architectural Overview
The project employs a multi-tiered data pipeline to preserve raw immutability, ensure clean data hygiene, and isolate derived analytical transformations:

1. **`data/raw/`**: Unaltered, historical baseline files (`f1_races_raw.csv`, `india_gp_raw.csv`, `india_gp_context_raw.csv`).
2. **`data/processed/`**: Validated, canonical, unit-standardized, and verified datasets (`f1_races_clean.csv`, `india_gp_clean.csv`, `india_gp_context_clean.csv`).
3. **`data/engineered/`**: Derived calculations, logarithmic transformations, financial models, and domain ratios (`f1_races_engineered.csv`, `india_gp_engineered.csv`).

---

## 2. Global F1 Dataset (`data/processed/f1_races_clean.csv`)

| Variable | Data Type | Units / Range | Value Type | Description / Provenance |
|---|---|---|---|---|
| `race_id` | String | `YYYY_RR` | Sourced | Unique identifier for each Grand Prix (e.g., `2011_17`). |
| `season` | Integer | `2010..2019` | Sourced | FIA Formula 1 World Championship season. |
| `round` | Integer | `1..21` | Sourced | Championship calendar round number. |
| `race_name` | String | Text | Sourced | Official Grand Prix name. |
| `circuit_id` | String | Slug / Key | Sourced | Canonical track identifier (`buddh`, `silverstone`, `monza`, etc.). |
| `circuit_name` | String | Text | Sourced | Full formal name of the racing facility. |
| `locality` | String | City / Town | Sourced | Host municipality. |
| `country` | String | Country Name | Sourced | Host sovereign nation. |
| `continent` | Categorical | 5 Regions | Sourced | Geographic classification (`Europe`, `Asia`, `Americas`, `Middle East`, `Oceania`). |
| `date` | Date | `YYYY-MM-DD` | Sourced | Sunday race date. |
| `circuit_type` | Categorical | `Permanent` / `Street` / `Hybrid` | Sourced | Track layout classification. |
| `circuit_length_km` | Float | Kilometres | Sourced | Single lap length (3.337 km in Monaco to 7.004 km at Spa). |
| `laps` | Integer | Lap Count | Sourced | Officially scheduled race lap count. |
| `race_distance_km` | Float | Kilometres | Sourced | Total scheduled race distance (`laps * circuit_length_km`). |
| `race_duration_min` | Float | Minutes | Sourced | Winning driver's race completion time. |
| `average_speed_kmh` | Float | km/h | Sourced | Mean race speed of the winning driver (`race_distance_km / duration`). |
| `fastest_lap_time_s` | Float | Seconds | Sourced | Fastest single lap time recorded during the Grand Prix. |
| `winner_driver` | String | Driver Name | Sourced | Race winner name. |
| `winning_constructor` | String | Team Name | Sourced | Winning constructor / team. |
| `winning_margin_s` | Float | Seconds | Sourced | Time margin between 1st and 2nd place finishers. |
| `finishers_count` | Integer | Count | Sourced | Number of officially classified finishers. |
| `dnf_count` | Integer | Count | Sourced | Number of classified Did Not Finish (DNF) retirements. |
| `total_pit_stops` | Integer | Count | Sourced | Total pit stops executed across the field during the race. |
| `attendance_race_day` | Integer | Spectators | Reported | Official / reported Sunday race-day gate attendance. |
| `attendance_weekend` | Integer | Spectators | Reported | Official 3-day aggregate weekend attendance figure. |
| `attendance_source` | String | Key | Sourced | Source tracking key (`SRC_02`, `SRC_03`, `SRC_05`). |
| `attendance_confidence` | Categorical | `High` / `Medium` / `Low` | Audited | Justified confidence level based on source audit. |
| `gdp_per_capita_usd` | Float | Current USD ($) | Sourced | Host nation annual GDP per capita (World Bank indicator `SRC_04`). |
| `event_tenure_years` | Integer | Years | Sourced | Cumulative number of years this event was held up to the race season. |

---

## 3. Indian Grand Prix Processed Dataset (`data/processed/india_gp_clean.csv`)

| Variable | Data Type | Units | Value Type | Description / Provenance |
|---|---|---|---|---|
| `season` | Integer | `2011`, `2012`, `2013` | Sourced | Indian GP edition year. |
| `round` | Integer | Round number | Sourced | Calendar round (17 in 2011/2012; 16 in 2013). |
| `date` | Date | `YYYY-MM-DD` | Sourced | Sunday race date. |
| `official_race_name` | String | Text | Sourced | Airtel Indian Grand Prix. |
| `circuit_name` | String | Text | Sourced | Buddh International Circuit. |
| `locality` | String | Greater Noida | Sourced | Host city. |
| `country` | String | India | Sourced | Host nation. |
| `promoter_entity` | String | Text | Sourced | Jaypee Sports International Ltd (JPSI). |
| `attendance_race_day` | Integer | Spectators | Reported | Sunday race day gate count (95k in 2011, 65k in 2012, 60k in 2013). |
| `attendance_weekend` | Integer | Spectators | Reported | 3-day aggregate weekend gate count (110k in 2011, 95k in 2012, 65k in 2013). |
| `attendance_type` | String | Text | Audit | Verified official promoter gate disclosure (`SRC_05`). |
| `hosting_fee_usd_m` | Float | USD ($ Millions) | Reported | Contractual fee paid to FOWC ($40.0M in 2011, $42.0M in 2012, $44.1M in 2013). |
| `hosting_fee_type` | String | Text | Audit | Contractual (RPA base + 5% annual compounding escalation). |
| `min_ticket_price_inr` | Float | INR (₹) | Reported | Lowest ticket tier (₹2,500 in 2011, ₹2,000 in 2012, ₹1,500 in 2013). |
| `max_ticket_price_inr` | Float | INR (₹) | Reported | Highest regular grandstand tier (₹35,000 in 2011, ₹30,000 in 2012, ₹25,000 in 2013). |
| `ticket_price_type` | String | Text | Audit | Official BookMyShow published tariff schedules (`SRC_07`). |
| `usd_inr_exchange_rate` | Float | INR per USD | Reported | Historical annual mean reference rate (46.67 in 2011, 53.44 in 2012, 58.60 in 2013). |
| `exchange_rate_source` | String | Text | Sourced | Reserve Bank of India (`SRC_12`). |
| `circuit_capex_usd_m` | Float | USD ($ Millions) | Reported | Buddh International Circuit initial construction capital expenditure (~$400M). |
| `capex_source` | String | Text | Sourced | Jaiprakash Associates Ltd corporate annual filings (`SRC_08`). |
| `entertainment_tax_status` | String | Text | Sourced | 25% tax dispute and High Court escrow deposit mandate (`SRC_10`). |
| `customs_duty_status` | String | Text | Sourced | Refusal of sports classification; ATA Carnet bank guarantee required (`SRC_11`). |
| `source_citation` | String | Keys | Sourced | Traceable keys mapping into `source_registry.csv`. |
| `data_confidence` | Categorical | `High` | Audit | Validated across judicial, corporate, and official records. |

---

## 4. Derived & Engineered Datasets (`data/engineered/`)

### 4.1. `f1_races_engineered.csv`
* `log_attendance_race_day`: $\ln(\text{attendance\_race\_day})$ to normalize heavily skewed attendance distribution.
* `log_attendance_weekend`: $\ln(\text{attendance\_weekend})$.
* `weekend_to_sunday_ratio`: $\frac{\text{attendance\_weekend}}{\text{attendance\_race\_day}}$ measuring multi-day fan engagement.
* `attendance_per_gdp_k`: $\frac{\text{attendance\_race\_day}}{\text{gdp\_per\_capita\_usd} / 1000}$ indexing crowd size relative to host nation economic wealth.
* `dnf_rate_pct`: $\frac{\text{dnf\_count}}{\text{finishers\_count} + \text{dnf\_count}} \times 100$.
* `speed_to_length_ratio`: $\frac{\text{average\_speed\_kmh}}{\text{circuit\_length\_km}}$.
* `is_indian_gp`: Binary dummy flag (`1` for Buddh International Circuit, `0` otherwise).

### 4.2. `india_gp_engineered.csv`
* `hosting_fee_inr_crore`: $\frac{\text{hosting\_fee\_usd\_m} \times 10^6 \times \text{usd\_inr\_exchange\_rate}}{10^7}$ (₹186.68 Cr in 2011 $\rightarrow$ ₹258.43 Cr in 2013).
* `min_ticket_price_usd`: Lowest ticket tier converted to USD.
* `max_ticket_price_usd`: Highest ticket tier converted to USD.
* `race_day_attendance_change_pct`: YoY percentage change in Sunday turnout (-31.58% in 2012, -7.69% in 2013).
* `weekend_attendance_change_pct`: YoY percentage change in weekend turnout (-13.64% in 2012, -31.58% in 2013).
* `estimated_ticket_revenue_usd_m`: Weighted gate model revenue ($26.5M in 2011, $15.2M in 2012, $11.8M in 2013).
* `estimated_operating_cost_usd_m`: Event logistics, security, and track maintenance ($15.0M in 2011, $14.0M in 2012, $13.5M in 2013).
* `estimated_total_event_cost_usd_m`: `hosting_fee_usd_m + estimated_operating_cost_usd_m` ($55.0M in 2011 $\rightarrow$ $57.6M in 2013).
* `estimated_net_operating_cashflow_usd_m`: Estimated ticket revenue minus total costs (-$28.5M in 2011 $\rightarrow$ -$45.8M in 2013).
* `revenue_to_hosting_fee_ratio`: Ratio of ticketing gate revenue to contractual hosting fee (0.66 in 2011 down to 0.27 in 2013).
