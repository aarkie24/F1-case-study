"""
Script to create notebooks/01_data_collection.ipynb using nbformat
"""

import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Title & Overview
cells.append(nbf.v4.new_markdown_cell("""# Phase 1: Data Acquisition & Sourcing
## Commercial Sustainability of Formula 1 & The Indian Grand Prix Case Study

### Notebook Objectives:
1. Load and verify raw datasets across all three tiers:
   - **Dataset A:** Global Formula 1 baseline races (2010–2019, ~198 races).
   - **Dataset B:** Detailed Indian Grand Prix event-level financials and attendance (2011–2013).
   - **Dataset C:** Contextual timeline of legal, regulatory, tax, and commercial milestones.
2. Verify provenance mappings against `sources/source_registry.csv`.
3. Perform structural integrity and initial schema validation checks.
"""))

# Cell: Imports
cells.append(nbf.v4.new_code_cell("""import os
import pandas as pd
import numpy as np

# Verify file existence
raw_files = {
    "f1_races": "data/raw/f1_races_raw.csv",
    "india_gp": "data/raw/india_gp_raw.csv",
    "india_gp_context": "data/raw/india_gp_context_raw.csv",
    "source_registry": "sources/source_registry.csv"
}

for name, path in raw_files.items():
    assert os.path.exists(path), f"Missing expected file: {path}"
    print(f"Verified: {path}")
"""))

# Cell: Load and Inspect Dataset A
cells.append(nbf.v4.new_markdown_cell("""### 1. Dataset A: Global F1 Races Baseline (2010–2019)"""))
cells.append(nbf.v4.new_code_cell("""df_f1 = pd.read_csv("data/raw/f1_races_raw.csv")
print(f"Shape: {df_f1.shape[0]} rows, {df_f1.shape[1]} columns")
print(f"Seasons covered: {df_f1['season'].min()} to {df_f1['season'].max()} ({df_f1['season'].nunique()} seasons)")
print(f"Unique circuits: {df_f1['circuit_name'].nunique()}")
print(f"Continents represented: {df_f1['continent'].value_counts().to_dict()}")
df_f1.head(5)
"""))

# Cell: Summary Statistics Dataset A
cells.append(nbf.v4.new_markdown_cell("""#### Summary Statistics of Baseline Sporting & Attendance Metrics"""))
cells.append(nbf.v4.new_code_cell("""numeric_cols = [
    "circuit_length_km", "race_distance_km", "race_duration_min", 
    "average_speed_kmh", "fastest_lap_time_s", "winning_margin_s", 
    "finishers_count", "dnf_count", "total_pit_stops", 
    "attendance_race_day", "attendance_weekend", "gdp_per_capita_usd"
]
df_f1[numeric_cols].describe().T
"""))

# Cell: Load and Inspect Dataset B
cells.append(nbf.v4.new_markdown_cell("""### 2. Dataset B: Indian Grand Prix Event Deep-Dive (2011–2013)"""))
cells.append(nbf.v4.new_code_cell("""df_india = pd.read_csv("data/raw/india_gp_raw.csv")
print(f"Shape: {df_india.shape[0]} rows, {df_india.shape[1]} columns")
df_india
"""))

# Cell: Load and Inspect Dataset C
cells.append(nbf.v4.new_markdown_cell("""### 3. Dataset C: Contextual Milestones Timeline"""))
cells.append(nbf.v4.new_code_cell("""df_context = pd.read_csv("data/raw/india_gp_context_raw.csv")
print(f"Total Context Milestones: {len(df_context)}")
print(f"Categories: {df_context['category'].value_counts().to_dict()}")
df_context[["event_id", "date", "phase", "category", "headline", "impact_dimension", "confidence"]]
"""))

# Cell: Load Source Registry
cells.append(nbf.v4.new_markdown_cell("""### 4. Source Registry & Provenance Verification"""))
cells.append(nbf.v4.new_code_cell("""df_sources = pd.read_csv("sources/source_registry.csv")
print(f"Total Registered Sources: {len(df_sources)}")
df_sources[["source_id", "dataset", "source_name", "source_type", "confidence"]]
"""))

# Cell: Phase 1 Summary
cells.append(nbf.v4.new_markdown_cell("""### Phase 1 Completion Summary
* **Global Dataset A:** 198 Formula 1 Grand Prix races collected across 10 seasons (2010–2019) covering 29 attributes.
* **India Deep-Dive Dataset B:** 3 races with 25 financial, ticketing, operational, and attendance metrics.
* **Contextual Dataset C:** 15 chronological regulatory, tax, judicial, and business milestones spanning 2007–2020.
* **Source Registry:** 12 primary and secondary reference sources cataloged with explicit confidence ratings.
"""))

nb.cells = cells

with open("notebooks/01_data_collection.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("Created notebooks/01_data_collection.ipynb successfully.")
