import json
import os
import sys
import nbformat
from nbclient import NotebookClient

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOK_PATH = os.path.join(BASE_DIR, 'notebooks', 'Online_Food_Delivery_DAP_Final.ipynb')

def execute_notebook():
    # First build the notebook structure
    from build_master_notebook import build_master_notebook
    build_master_notebook()

    print("Executing master notebook from top to bottom...")
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    client = NotebookClient(nb, timeout=600, kernel_name='python3', resources={'metadata': {'path': os.path.join(BASE_DIR, 'notebooks')}})
    client.execute()

    with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"[OK] Successfully executed all cells in master notebook: {NOTEBOOK_PATH}")
    print(f"Total cells executed: {len(nb.cells)}")

if __name__ == '__main__':
    execute_notebook()
