# 🌍 Nutrition Paradox: A Global View on Obesity and Malnutrition

An end-to-end data science and analytics project exploring the dual burden of malnutrition and obesity across global populations, integrated with a cloud-native TiDB database, interactive Power BI dashboards, and a live Streamlit analytics app.

---

## 🚀 Project Overview
The "Nutrition Paradox" project investigates the simultaneous presence of undernutrition and obesity within countries, regions, and populations. This project covers data ingestion, cloud database warehousing (TiDB), exploratory data analysis via Python/SQL, and business intelligence reporting.

---

## 🛠️ Tech Stack & Tools
* **Database & Cloud:** TiDB Cloud (MySQL compatible), SQLAlchemy, PyMySQL, `mysql-connector-python`
* **Data Processing & Analysis:** Python, Pandas, Jupyter Notebooks
* **Web Application:** Streamlit
* **Data Visualization & BI:** Power BI Desktop (`.pbix`)
* **Version Control:** Git & GitHub

---

## 📂 Project Directory Structure

```text
02_DS_NUTRITION PARADOX/
│
├── data/                       # Cleaned raw datasets (.csv)
│   ├── malnutrition.csv
│   └── obesity.csv
│
├── notebooks/                  # Jupyter notebooks for exploratory data analysis
│   └── Nutrition_Paradox.ipynb
│
├── reports/                    # Documentation and dashboards
│   ├── Nutrition Paradox_ A Global View on Obesity and Malnutrition.docx
│   └── Nutrition_Paradox.pbix
│
├── TiDB_security/              # SSL certificates for secure database connection
│   └── isrgrootx1.pem
│
├── app.py                      # Streamlit interactive dashboard application
├── main.py                     # Main ingestion and processing pipeline script
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
