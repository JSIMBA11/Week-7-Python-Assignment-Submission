# Analyzing Iris and Bank Marketing Data

This project demonstrates how to analyze and visualize data using **Pandas**, **Matplotlib**, and **Seaborn**.  
Two datasets are used:

1. **Iris Dataset** (from scikit-learn) → A classic dataset for classification and data visualization tasks.  
2. **Bank Marketing Dataset** (UCI Machine Learning Repository) → Data on direct marketing campaigns of a Portuguese bank.  

---

## 📂 Files in This Project
- `analysis.ipynb` → Jupyter Notebook containing the code, visualizations, and findings.  
- `analysis.py` → (Optional) Python script version of the notebook.  
- `requirements.txt` → List of dependencies to install.  
- `bank.csv` → Bank marketing dataset (10% sample, 4521 rows).  
- `README.md` → Project documentation (this file).  

---

## ⚙️ Setup Instructions

1. Place all files (`analysis.ipynb`, `requirements.txt`, and `bank.csv`) in the same folder.  
   - For Iris, no external file is needed (it is loaded from scikit-learn).  
   - For Bank Marketing, download `bank.csv` from the UCI dataset and put it in the folder (or adjust the file path in the script).  

2. Install dependencies:

```bash
pip install -r requirements.txt
Run the project:

Option A: Run in VS Code
Install the Python and Jupyter extensions.

Open analysis.ipynb and run the cells.

Option B: Run in Jupyter Notebook
bash
Copy code
jupyter notebook analysis.ipynb
📊 Features Demonstrated
Iris Dataset
Data loading, inspection, and cleaning.

Descriptive statistics.

Grouping by species.

Visualizations: line chart, bar chart, histogram, scatter plot.

Bank Marketing Dataset
Data loading and inspection.

https://archive.ics.uci.edu/dataset/222/bank+marketing

Descriptive statistics (numeric + categorical).

Target variable analysis (y: whether a client subscribed to a term deposit).

✅ Findings
Iris Dataset: Iris-virginica generally has the largest petals; species are separable by petal dimensions.

Bank Dataset: Provides insights into customer behavior and campaign effectiveness, with the target column (y) being imbalanced.

📌 Dataset Sources
Iris Dataset: Built into scikit-learn.

Bank Marketing Dataset:
Moro et al., 2011. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology.
Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal. EUROSIS.
Available: UCI Repository 
[bank-names](https://archive.ics.uci.edu/dataset/222/bank+marketing)


📌 Requirements
Python 3.8+

Libraries: pandas, matplotlib, seaborn, scikit-learn

📝 Author
Jerald 
