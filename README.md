# AdCampaignIQ 📊

**Real-Time Ads Analytics Dashboard**
A full-stack analytical tool designed to ingest, process, and visualize ad impression data. This project simulates a high-volume Ad Tech reporting environment to calculate critical business metrics like **CTR (Click-Through Rate)**, **CPC (Cost Per Click)**, and **ROAS (Return on Ad Spend)**.

## 🚀 Key Features
* **ETL Pipeline:** Ingests 10,000+ raw ad impression records into a SQLite warehouse.
* **Advanced SQL:** Utilizes Window Functions and CTEs to identify underperforming campaigns.
* **API Layer:** Flask-based REST API serving JSON data for frontend dashboards.
* **Business Logic:** Automated alerting for campaigns with "overpacing" budgets.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Database:** SQLite (for portability), SQL
* **API:** Flask
* **Data Processing:** Pandas

## ⚙️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Generate mock data: `python src/generate_data.py`
3. Start the API: `python src/app.py`
