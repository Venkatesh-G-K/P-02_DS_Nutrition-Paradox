# 🌍 Nutrition Paradox: A Global View on Obesity and Malnutrition

An end-to-end data science and analytics project investigating the dual burden of malnutrition and obesity across global populations. Integrated with a cloud-native TiDB database, interactive Power BI dashboards, and a live Streamlit analytics web application.

---

## 🛠️ Tech Stack & Tools
* **Database & Cloud:** TiDB Cloud (MySQL compatible), SQLAlchemy, PyMySQL
* **Data Processing & Analysis:** Python, Pandas, Jupyter Notebooks
* **Web Application:** Streamlit
* **Data Visualization & BI:** Power BI Desktop (`.pbix`)
* **Version Control:** Git & GitHub

---

## 📂 Project Directory Structure

```text
02_DS_NUTRITION PARADOX/
│
├── data/                       # Raw dataset files (CSV)
│   ├── malnutrition.csv
│   └── obesity.csv
│
├── notebooks/                  # Jupyter notebooks for exploratory analysis
│   └── Nutrition_Paradox.ipynb
│
├── requirements/               # Project documentation and specifications
│   └── Nutrition Paradox_ A Global View on Obesity and Malnutrition.docx
│
├── TiDB_security/              # Secure SSL database certificates
│   └── isrgrootx1.pem
│
├── app.py                      # Streamlit interactive dashboard application
├── Nutrition_Paradox.pbix      # Power BI business intelligence file
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python package dependencies
└── README.md                   # Project documentation


📊 Key Features & Analytics
The project executes 25 specialized SQL analytical queries against the TiDB cloud database, covering:

Regional and global trend comparisons for obesity and malnutrition.

Country-specific timelines (India, USA, Brazil, Nigeria, China).

Gender disparities and multi-variable filters capturing the "Nutrition Paradox" profile.

⚙️ Setup and Installation Guide
Follow these steps to set up and run the project locally on your machine.

Step 1: Clone the Repository
Open your terminal or command prompt and run the following command to clone the project:

Bash
git clone [https://github.com/Venkatesh-G-K/P-02_DS_Nutrition-Paradox.git](https://github.com/Venkatesh-G-K/P-02_DS_Nutrition-Paradox.git)
cd P-02_DS_Nutrition-Paradox
Step 2: Set Up a Virtual Environment
It is recommended to create an isolated Python virtual environment:

Bash
python -m venv .venv
Activate the virtual environment:

On Windows (Command Prompt / PowerShell):

Bash
.venv\Scripts\activate
On macOS / Linux:

Bash
source .venv/bin/activate
Step 3: Install Dependencies
Install all the required Python libraries using the requirements.txt file:

Bash
pip install -r requirements.txt
Step 4: Configure Database and Security Credentials
Ensure your cloud database connection parameters (User, Password, Host, Port, Database name) are properly supplied in your code scripts.

Confirm that your SSL certificate file (isrgrootx1.pem) is placed inside the TiDB_security/ folder so the application can authenticate securely with TiDB Cloud.

🚀 Running the Application
Option A: Run the Streamlit Web App Locally
To launch the interactive dashboard application in your web browser:

Bash
streamlit run app.py
This will automatically open a local web page (typically at http://localhost:8501) where you can interact with the data metrics, charts, and queries.

Option B: Explore via Jupyter Notebooks
If you want to view the data pipeline, data cleaning steps, and analysis queries:

Open VS Code in the project folder.

Open the notebooks/Nutrition_Paradox.ipynb file.

Select your .venv kernel and run the cells.

Option C: View the Power BI Dashboard
Open the Nutrition_Paradox.pbix file using Power BI Desktop to view the rich visual reports and data models built for this project.

👤 Author
Venkatesh G K
