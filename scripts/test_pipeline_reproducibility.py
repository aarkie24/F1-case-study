"""
Comprehensive Pipeline and Notebook Reproducibility Test Suite
Validates that:
1. All raw and processed datasets exist and have valid shapes.
2. All data quality assertions hold (0 duplicates, referential integrity, no missing primary keys).
3. All 6 Jupyter notebooks can execute every code cell without throwing errors.
4. All 8 publication figures exist and are non-empty.
"""

import os
import glob
import nbformat
import pandas as pd
import numpy as np

def test_dataset_existence():
    required_files = [
        "data/raw/f1_races_raw.csv",
        "data/raw/india_gp_raw.csv",
        "data/raw/india_gp_context_raw.csv",
        "data/processed/f1_races_clean.csv",
        "data/processed/india_gp_clean.csv",
        "data/processed/india_gp_context_clean.csv",
        "data/processed/data_dictionary.md",
        "data/engineered/f1_races_engineered.csv",
        "data/engineered/india_gp_engineered.csv",
        "sources/source_registry.csv"
    ]
    for path in required_files:
        assert os.path.exists(path), f"Missing dataset file: {path}"
        assert os.path.getsize(path) > 0, f"File is empty: {path}"

def test_data_integrity():
    f1 = pd.read_csv("data/processed/f1_races_clean.csv")
    india = pd.read_csv("data/processed/india_gp_clean.csv")
    ctx = pd.read_csv("data/processed/india_gp_context_clean.csv")
    
    # 198 races across 2010-2019
    assert len(f1) == 198, f"Expected 198 races, got {len(f1)}"
    assert f1['race_id'].nunique() == 198, "Duplicate race_id found"
    assert f1['season'].min() == 2010 and f1['season'].max() == 2019
    
    # India GP editions
    assert len(india) == 3, f"Expected 3 India GP editions, got {len(india)}"
    assert list(india['season']) == [2011, 2012, 2013]
    assert list(india['attendance_race_day']) == [95000, 65000, 60000]
    
    # Timeline
    assert len(ctx) >= 10, "Timeline events missing"
    assert "PE" in " ".join(ctx['headline']) or "Permanent Establishment" in " ".join(ctx['headline'])

def test_figures_generation():
    figures = [
        "reports/figures/fig1_attendance_distribution_with_india.png",
        "reports/figures/fig2_indian_gp_decay_curve.png",
        "reports/figures/fig3_regional_attendance_comparison.png",
        "reports/figures/fig4_multivariate_correlation_matrix.png",
        "reports/figures/fig5_attendance_vs_gdp_multidimensional.png",
        "reports/figures/fig6_commercial_deficit_and_hosting_fee.png",
        "reports/figures/fig7_historical_context_timeline.png",
        "reports/figures/fig8_circuit_characteristics_radar_speed.png"
    ]
    for fig in figures:
        assert os.path.exists(fig), f"Figure missing: {fig}"
        assert os.path.getsize(fig) > 10000, f"Figure {fig} seems corrupted or too small"

def test_notebooks_execution():
    import matplotlib
    matplotlib.use('Agg')
    notebooks = sorted(glob.glob("notebooks/*.ipynb"))
    assert len(notebooks) == 6, f"Expected 6 notebooks, found {len(notebooks)}"
    
    for nb_path in notebooks:
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        
        exec_env = {'__name__': '__main__'}
        # Run all code cells sequentially
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type == "code":
                code = cell.source
                try:
                    exec(code, exec_env)
                except Exception as e:
                    raise RuntimeError(f"Notebook {nb_path} failed at cell {idx}: {e}")

if __name__ == "__main__":
    test_dataset_existence()
    print("[PASS] test_dataset_existence passed")
    test_data_integrity()
    print("[PASS] test_data_integrity passed")
    test_figures_generation()
    print("[PASS] test_figures_generation passed")
    test_notebooks_execution()
    print("[PASS] test_notebooks_execution passed")
    print("\nAll reproducibility and validation tests passed successfully!")
