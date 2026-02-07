from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Helper function to connect to DB
def get_db_connection():
    conn = sqlite3.connect('campaigns.db')
    conn.row_factory = sqlite3.Row # This lets us access columns by name (row['ctr']) instead of index (row[0])
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/metrics')
def get_metrics():
    conn = get_db_connection()
    
    # Run a simple query to get data for our dashboard
    query = """
    SELECT 
        campaign_name,
        SUM(impressions) as impressions,
        SUM(clicks) as clicks,
        SUM(spend) as spend,
        ROUND((SUM(clicks) * 1.0 / SUM(impressions)) * 100, 2) as ctr
    FROM ads
    GROUP BY campaign_name
    """
    metrics = conn.execute(query).fetchall()
    conn.close()
    
    # Convert the database rows into a list of dictionaries (JSON format)
    # This is what the frontend (JavaScript) will read.
    data = []
    for row in metrics:
        data.append({
            'campaign': row['campaign_name'],
            'impressions': row['impressions'],
            'clicks': row['clicks'],
            'spend': row['spend'],
            'ctr': row['ctr']
        })
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)