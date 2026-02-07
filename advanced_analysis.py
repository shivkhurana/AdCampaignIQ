import sqlite3
import pandas as pd

conn = sqlite3.connect('campaigns.db')

# --- The Advanced SQL Query ---
# We use a CTE (Common Table Expression) named 'CampaignStats'.
# Think of a CTE as a temporary table that exists only for this one query.
sql_query = """
WITH CampaignStats AS (
    SELECT 
        campaign_name,
        platform,
        SUM(impressions) as total_impressions,
        SUM(clicks) as total_clicks,
        -- Calculate CTR for this specific campaign
        (SUM(clicks) * 1.0 / SUM(impressions)) * 100 as actual_ctr
    FROM ads
    GROUP BY campaign_name, platform
),
PlatformStats AS (
    SELECT 
        campaign_name,
        platform,
        actual_ctr,
        -- WINDOW FUNCTION: Calculate the average CTR for THIS platform
        -- 'PARTITION BY platform' means: "Calculate the average only looking at rows with the same platform"
        AVG(actual_ctr) OVER (PARTITION BY platform) as avg_platform_ctr
    FROM CampaignStats
)
SELECT 
    campaign_name,
    platform,
    ROUND(actual_ctr, 2) as actual_ctr,
    ROUND(avg_platform_ctr, 2) as platform_avg,
    -- Logic: If actual < average, label it 'Underperforming'
    CASE 
        WHEN actual_ctr < avg_platform_ctr THEN 'Underperforming'
        ELSE 'Good' 
    END as status
FROM PlatformStats
WHERE status = 'Underperforming'
ORDER BY platform, actual_ctr;
"""

print("--- Identifying Underperforming Campaigns (vs Platform Average) ---")
df = pd.read_sql(sql_query, conn)

# Display all rows (so we can see the results clearly)
pd.set_option('display.max_rows', None)
print(df)

conn.close()