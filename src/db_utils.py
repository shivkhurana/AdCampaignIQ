import sqlite3

def get_underperforming_campaigns():
    # Connect to local DB
    conn = sqlite3.connect('ads.db')
    
    # COMPLEX SQL QUERY: Window Functions & Aggregations
    # This identifies campaigns where CTR is below 1% (0.01)
    query = """
    WITH CampaignStats AS (
        SELECT 
            campaign_id,
            SUM(spend) as total_spend,
            SUM(clicks) as total_clicks,
            SUM(impressions) as total_impressions
        FROM ad_events
        GROUP BY campaign_id
    ),
    Metrics AS (
        SELECT 
            *,
            (total_clicks * 1.0 / total_impressions) as ctr,
            (total_spend / NULLIF(total_clicks, 0)) as cpc
        FROM CampaignStats
    )
    SELECT * FROM Metrics WHERE ctr < 0.01; 
    """
    cursor = conn.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results