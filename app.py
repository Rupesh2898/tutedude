from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Read data from the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that serves data from a JSON file.