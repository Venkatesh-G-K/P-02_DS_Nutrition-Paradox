from pathlib import Path
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Nutrition Paradox - TiDB Query Dashboard",
    layout="wide"
)

st.title("🌍 Nutrition Paradox: TiDB Analytics Dashboard")
st.write("Select an analysis query below to execute it directly against your TiDB database.")

# 2. Database Connection Setup (Cached for performance)
# 2. Database Connection Setup (Cached for performance)

from pathlib import Path
from sqlalchemy import create_engine
import urllib.parse

@st.cache_resource
def get_db_engine():

    USER = "3fCAZkkCNgfMxEa.root"
    PASSWORD = "h8F1E28rdnGOgobd"
    HOST = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"
    PORT = 4000
    DATABASE = "Nutrition_Paradox"

    # SSL certificate in the same folder as app.py
    ssl_cert = Path(__file__).resolve().parent / "isrgrootx1.pem"

    if not ssl_cert.exists():
        st.error(f"SSL Certificate not found:\n{ssl_cert}")
        st.stop()

    connection_url = (
        f"mysql+pymysql://{USER}:{urllib.parse.quote_plus(PASSWORD)}"
        f"@{HOST}:{PORT}/{DATABASE}"
    )

    engine = create_engine(
        connection_url,
        connect_args={
            "ssl": {
                "ca": str(ssl_cert)
            }
        },
        pool_pre_ping=True,
        pool_recycle=3600,
        echo=False,
    )

    return engine

engine = get_db_engine()

# 3. Dictionary of all 25 Queries
queries = {
    "Query 1: Top 5 Regions by Avg Obesity (2022)": 
        "SELECT Region, AVG(Mean_Estimate) AS Avg_Obesity FROM obesity WHERE Year = 2022 GROUP BY Region ORDER BY Avg_Obesity DESC LIMIT 5",
    
    "Query 2: Top 5 Countries by Overall Avg Obesity": 
        "SELECT Country, AVG(Mean_Estimate) AS Avg_Obesity FROM obesity GROUP BY Country ORDER BY Avg_Obesity DESC LIMIT 5",
    
    "Query 3: India Obesity Trend by Year": 
        "SELECT Year, AVG(Mean_Estimate) AS Avg_Obesity FROM obesity WHERE Country = 'India' GROUP BY Year ORDER BY Year",
    
    "Query 4: Obesity by Gender": 
        "SELECT Gender, AVG(Mean_Estimate) AS Avg_Obesity FROM obesity GROUP BY Gender",
    
    "Query 5: Country Count by Obesity Level & Age Group": 
        "SELECT Obesity_Level, age_group, COUNT(DISTINCT Country) AS Country_Count FROM obesity GROUP BY Obesity_Level, age_group",
    
    "Query 6: Top 5 Countries by Highest CI Width (Obesity)": 
        "SELECT Country, AVG(CI_Width) AS Avg_CI_Width FROM obesity GROUP BY Country ORDER BY Avg_CI_Width DESC LIMIT 5",
    
    "Query 7: Obesity by Age Group": 
        "SELECT age_group, AVG(Mean_Estimate) AS Avg_Obesity FROM obesity GROUP BY age_group",
    
    "Query 8: Countries with Low Obesity (<10) and Low CI (<5)": 
        "SELECT Country, AVG(Mean_Estimate) AS Avg_Obesity, AVG(CI_Width) AS Avg_CI FROM obesity GROUP BY Country HAVING Avg_Obesity < 10 AND Avg_CI < 5 ORDER BY Avg_Obesity",
    
    "Query 9: Gender Obesity Difference (Female vs Male) by Country & Year": 
        "SELECT a.Country, a.Year, a.Mean_Estimate AS Female_Obesity, b.Mean_Estimate AS Male_Obesity, (a.Mean_Estimate - b.Mean_Estimate) AS Difference FROM obesity a JOIN obesity b ON a.Country = b.Country AND a.Year = b.Year WHERE a.Gender = 'Female' AND b.Gender = 'Male' ORDER BY Difference DESC",
    
    "Query 10: Global Obesity Trend by Year": 
        "SELECT Year, AVG(Mean_Estimate) AS Global_Obesity FROM obesity GROUP BY Year ORDER BY Year",
    
    "Query 11: Malnutrition by Age Group": 
        "SELECT age_group, AVG(Mean_Estimate) AS Avg_Malnutrition FROM malnutrition GROUP BY age_group",
    
    "Query 12: Top 5 Countries by Highest Avg Malnutrition": 
        "SELECT Country, AVG(Mean_Estimate) AS Avg_Malnutrition FROM malnutrition GROUP BY Country ORDER BY Avg_Malnutrition DESC LIMIT 5",
    
    "Query 13: Africa Malnutrition Trend by Year": 
        "SELECT Year, AVG(Mean_Estimate) AS Avg_Malnutrition FROM malnutrition WHERE Region = 'Africa' GROUP BY Year ORDER BY Year",
    
    "Query 14: Malnutrition by Gender": 
        "SELECT Gender, AVG(Mean_Estimate) AS Avg_Malnutrition FROM malnutrition GROUP BY Gender",
    
    "Query 15: Malnutrition Level & Age Group Average CI Width": 
        "SELECT Malnutrition_Level, age_group, AVG(CI_Width) AS Avg_CI_Width FROM malnutrition GROUP BY Malnutrition_Level, age_group",
    
    "Query 16: Malnutrition Trend for India, Nigeria, and Brazil": 
        "SELECT Country, Year, AVG(Mean_Estimate) AS Avg_Malnutrition FROM malnutrition WHERE Country IN ('India','Nigeria','Brazil') GROUP BY Country, Year ORDER BY Country, Year",
    
    "Query 17: Top 5 Regions with Lowest Avg Malnutrition": 
        "SELECT Region, AVG(Mean_Estimate) AS Avg_Malnutrition FROM malnutrition GROUP BY Region ORDER BY Avg_Malnutrition ASC LIMIT 5",
    
    "Query 18: Malnutrition Variance (Min to Max Spread) by Country": 
        "SELECT Country, MIN(Mean_Estimate) AS Early_Malnutrition, MAX(Mean_Estimate) AS Recent_Malnutrition, (MAX(Mean_Estimate) - MIN(Mean_Estimate)) AS Difference FROM malnutrition GROUP BY Country HAVING Difference > 0 ORDER BY Difference DESC",
    
    "Query 19: Global Min and Max Malnutrition by Year": 
        "SELECT Year, MIN(Mean_Estimate) AS Min_Malnutrition, MAX(Mean_Estimate) AS Max_Malnutrition FROM malnutrition GROUP BY Year ORDER BY Year",
    
    "Query 20: Records with High Malnutrition CI Width (>5)": 
        "SELECT Country, Year, CI_Width FROM malnutrition WHERE CI_Width > 5 ORDER BY CI_Width DESC",
    
    "Query 21: Obesity vs Malnutrition for Select Countries (India, USA, Brazil, Nigeria, China)": 
        "SELECT o.Country, AVG(o.Mean_Estimate) AS Avg_Obesity, AVG(m.Mean_Estimate) AS Avg_Malnutrition FROM obesity o JOIN malnutrition m ON o.Country = m.Country WHERE o.Country IN ('India','USA','Brazil','Nigeria','China') GROUP BY o.Country",
    
    "Query 22: Obesity vs Malnutrition Grouped by Gender": 
        "SELECT o.Gender, AVG(o.Mean_Estimate) AS Avg_Obesity, AVG(m.Mean_Estimate) AS Avg_Malnutrition FROM obesity o JOIN malnutrition m ON o.Gender = m.Gender GROUP BY o.Gender",
    
    "Query 23: Obesity vs Malnutrition for Africa & Americas Regions": 
        "SELECT o.Region, AVG(o.Mean_Estimate) AS Avg_Obesity, AVG(m.Mean_Estimate) AS Avg_Malnutrition FROM obesity o JOIN malnutrition m ON o.Region = m.Region WHERE o.Region IN ('Africa','Americas') GROUP BY o.Region",
    
    "Query 24: Paradox Filter (High Obesity > 20 & Low Malnutrition < 10) by Country": 
        "SELECT o.Country, AVG(o.Mean_Estimate) AS Avg_Obesity, AVG(m.Mean_Estimate) AS Avg_Malnutrition FROM obesity o JOIN malnutrition m ON o.Country = m.Country GROUP BY o.Country HAVING Avg_Obesity > 20 AND Avg_Malnutrition < 10",
    
    "Query 25: Obesity vs Malnutrition Grouped by Age Group": 
        "SELECT o.age_group, AVG(o.Mean_Estimate) AS Avg_Obesity, AVG(m.Mean_Estimate) AS Avg_Malnutrition FROM obesity o JOIN malnutrition m ON o.age_group = m.age_group GROUP BY o.age_group"
}

# 4. Streamlit UI Elements
selected_query_name = st.selectbox("Choose a Query to Run:", list(queries.keys()))
selected_sql = queries[selected_query_name]

st.markdown("### Executed SQL Statement:")
st.code(selected_sql, language="sql")

# 5. Run Query and Render Results
if st.button("🚀 Run Query"):
    try:
        with st.spinner("Executing query..."):
            with engine.connect() as connection:
                df_result = pd.read_sql(selected_sql, con=connection)

        st.success(f"✅ Query executed successfully! Rows returned: {len(df_result)}")

        # Display DataFrame
        st.dataframe(df_result, use_container_width=True)

        # Download CSV
        csv = df_result.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download CSV",
            csv,
            "query_results.csv",
            "text/csv"
        )

        # Quick Visualization
        numeric_cols = [c for c in df_result.select_dtypes(include="number").columns if c != df_result.columns[0]]

        if len(df_result) > 1 and len(df_result.columns) > 1 and len(df_result) <= 100 and numeric_cols:
            st.markdown("### 📊 Quick Visual Chart")
            st.bar_chart(
                data=df_result,
                x=df_result.columns[0],
                y=numeric_cols[0]
            )

    except Exception as e:
        st.error(f"❌ Error executing query: {e}")
