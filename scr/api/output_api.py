from flask import Flask, jsonify
import pandas as pd
from logger import logger

app = Flask(__name__)

# Endpoint para obter o status dos envios de mensagens
@app.route('/api/message_status', methods=['GET'])
def get_message_status():
    try:
        # Carregar dados estruturados e não estruturados
        structured_data = pd.read_csv('../data_sample/sample_estruturados.csv')
        unstructured_data = pd.read_csv('../data_sample/sample_nao_estruturados.csv')
        
        # Combinar os dados
        combined_data = pd.concat([structured_data, unstructured_data], ignore_index=True)
        
        # Selecionar colunas relevantes
        status_data = combined_data[['phone', 'status']]
        
        # Converter para JSON
        status_json = status_data.to_dict(orient='records')
        
        logger.info('Message status data retrieved successfully')
        return jsonify(status_json), 200
    except Exception as e:
        logger.error(f'Error retrieving message status data: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info('Starting output API')
    app.run(debug=True, host='0.0.0.0', port=5001)