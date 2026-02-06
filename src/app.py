from flask import Flask, jsonify
import db_utils

app = Flask(__name__)

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    # Fetch underperforming campaigns from SQL logic
    data = db_utils.get_underperforming_campaigns()
    return jsonify({"underperforming_campaigns": data, "status": "alert_active"})

if __name__ == '__main__':
    app.run(debug=True)