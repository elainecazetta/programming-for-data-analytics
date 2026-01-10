# Housing, Population, and Immigration Trends in Ireland (Census Analysis)

## 1) What this repository contains
This repository contains a Jupyter Notebook project that analyses Irish Census-related data to explore:

- **Population trends** by county over time (with a focus on major counties such as Dublin, Cork, Galway, and Limerick)
- **Housing trends** using private household counts and growth rates
- **Immigration patterns** by citizenship (grouped into Irish vs Non-Irish for clearer comparison)
- A **combined analysis** that merges population, housing, and immigration metrics and creates a simple housing pressure indicator (e.g., households per 1,000 people), plus correlation visuals for 2022.

### Main file
- `census_analysis.ipynb` (the notebook with all analysis, cleaning, and plots)

### Data files
The following CSV files were utilised in this project and they are inside the `data/` folder:

- `data/FY001-population.csv`  (Population by county and Census year)
- `data/FY004B-housing.csv`    (Housing / private households related data by county and Census year)
- `data/F5002-immigration.csv` (Population by citizenship by county and Census year)

These datasets are based on CSO Ireland tables:
- FY001: https://data.cso.ie/table/FY001  
- FY004B: https://data.cso.ie/table/FY004B  
- F5002: https://data.cso.ie/table/F5002  

---

## 2) Imports / requirements
The notebook uses the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

### Install (pip)
From your repository folder, run:

```bash
pip install pandas numpy matplotlib seaborn
```
---  

## 3) How to use the code  

### Run in Jupyter Notebook
1. Open Jupyter Notebook:
```
jupyter notebook
```

2. Open `census_analysis.ipynb` and run all cells in order.

### Run in VS Code
1. Install the Python and Jupyter extensions
2. Open the project folder in VS Code
3. Open `census_analysis.ipynb`
4. Select a Python interpreter with the required libraries installed
5. Click **Run All**

---
