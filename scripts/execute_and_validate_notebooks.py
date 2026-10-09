"""
Execute and Validate All Notebooks
Runs all 6 notebooks via nbclient / nbconvert to verify reproducibility,
populates all execution outputs, and asserts 0 runtime errors.
"""

import os
import glob
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

notebooks = sorted(glob.glob("notebooks/*.ipynb"))
print(f"Found {len(notebooks)} notebooks to execute and validate:")
for nb_path in notebooks:
    print(f" - {nb_path}")

ep = ExecutePreprocessor(timeout=120, kernel_name='python3')

for nb_path in notebooks:
    print(f"\nExecuting {nb_path}...")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    try:
        ep.preprocess(nb, {'metadata': {'path': '.'}})
        with open(nb_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"✓ {nb_path} executed and saved successfully with outputs.")
    except Exception as e:
        print(f"✗ Error executing {nb_path}: {e}")
        raise e

print("\nAll notebooks executed cleanly without errors!")
