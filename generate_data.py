import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Setup constants
NUM_RECORDS = 10000
CAMPAIGNS = ['Summer_Sale', 'Winter_Coat_Promo', 'Tech_Gadgets_2026', 'Back_to_School', 'Holiday_Special']
PLATFORMS = ['Facebook', 'Instagram', 'Google_Ads', 'LinkedIn']

data = []

# 2. Generate the loop
print(f"Generating {NUM_RECORDS} mock records...")

for i in range(NUM_RECORDS):
    # Randomly pick a date within the last 30 days
    date = datetime.now() - timedelta(days=random.randint(0, 30))
    
    # Randomly pick campaign and platform
    campaign = random.choice(CAMPAIGNS)
    platform = random.choice(PLATFORMS)
    
    # Random metrics (Impressions, Clicks, Spend)
    # Logic: Clicks must be less than impressions!
    impressions = random.randint(100, 1000)
    clicks = random.randint(0, int(impressions * 0.10)) # Max 10% CTR to keep it realistic
    spend = round(clicks * random.uniform(0.5, 2.0), 2) # Cost between $0.50 and $2.00 per click
    
    data.append([date.date(), campaign, platform, impressions, clicks, spend])

# 3. Convert to a DataFrame (Table format)
df = pd.DataFrame(data, columns=['date', 'campaign_name', 'platform', 'impressions', 'clicks', 'spend'])

# 4. Save to CSV (so we can see it easily)
csv_filename = 'ad_data.csv'
df.to_csv(csv_filename, index=False)

print(f"Success! Data saved to {csv_filename}")
print(df.head()) # Show first 5 rows