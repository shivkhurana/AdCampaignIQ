import sqlite3
import pandas as pd

# 1. Define the database name
DB_NAME = 'campaigns.db'

# 2. Connect to the database
# (If the file doesn't exist, this line creates it automatically!)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 3. Create the table
# We are telling the database: "Create a shelf called 'ads' with these specific slots."
create_table_query = """
CREATE TABLE IF NOT EXISTS ads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    campaign_name TEXT,
    platform TEXT,
    impressions INTEGER,
    clicks INTEGER,
    spend REAL
);
"""
cursor.execute(create_table_query)
print("Table 'ads' created successfully.")

# 4. Load the CSV data
# We use pandas to read the CSV, then tell it to dump everything into SQL.
df = pd.read_csv('ad_data.csv')

# 'if_exists="append"' means: "If the table is already there, just add these rows to it."
# 'index=False' means: "Don't save the row numbers (0, 1, 2...) from the CSV."
df.to_sql('ads', conn, if_exists='append', index=False)

print(f"Successfully loaded {len(df)} rows into the database!")

# 5. Commit (Save) and Close
conn.commit()
conn.close()