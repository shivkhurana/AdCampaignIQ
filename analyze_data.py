import sqlite3
import pandas as pd

# 1. Connect to the database
conn = sqlite3.connect('campaigns.db')

# 2. Basic Sanity Check
# Query: "Count how many rows are in the 'ads' table"
print("--- Check 1: Row Count ---")
query = "SELECT count(*) FROM ads;"
df = pd.read_sql(query, conn)
print(df)

# 3. The "Resume" Query (Aggregated Metrics)
# This calculates Total Impressions, Clicks, and Spend for each Campaign.
# Then it calculates CTR and CPC.
print("\n--- Check 2: Campaign Performance ---")

sql_query = """
SELECT 
    campaign_name,
    SUM(impressions) as total_impressions,
    SUM(clicks) as total_clicks,
    SUM(spend) as total_spend,
    
    -- Calculate CTR: (Clicks / Impressions) * 100
    -- We multiply by 1.0 to force 'floating point' math (so 5/100 doesn't become 0)
    ROUND((SUM(clicks) * 1.0 / SUM(impressions)) * 100, 2) as ctr_percentage,
    
    -- Calculate CPC: Spend / Clicks
    ROUND(SUM(spend) / SUM(clicks), 2) as cpc_dollars

FROM ads
GROUP BY campaign_name
ORDER BY ctr_percentage DESC;
"""

# Run the query and load it into a nice Pandas table
results = pd.read_sql(sql_query, conn)

print(results)

conn.close()