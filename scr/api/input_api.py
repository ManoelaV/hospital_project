from flask import Flask, request, jsonify
import pandas as pd
from logger import logger

app = Flask(__name__)

# Endpoint para receber dados estruturados
@app.route('/api/structured_data', methods=['POST'])
def receive_structured_data():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        df.to_csv('../data/sample_estruturados.csv', index=False)
        logger.info('Structured data received and saved successfully')
        return jsonify({'message': 'Structured data received successfully'}), 200
    except Exception as e:
        logger.error(f'Error receiving structured data: {e}')
        return jsonify({'error': str(e)}), 500

# Endpoint para receber dados não estruturados
@app.route('/api/unstructured_data', methods=['POST'])
def receive_unstructured_data():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        df.to_csv('../data/sample_nao_estruturados.csv', index=False)
        logger.info('Unstructured data received and saved successfully')
        return jsonify({'message': 'Unstructured data received successfully'}), 200
    except Exception as e:
        logger.error(f'Error receiving unstructured data: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info('Starting input API')
    app.run(debug=True, host='0.0.0.0', port=5000)