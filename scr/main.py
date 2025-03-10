import sys
import os
import threading
from flask import Flask

# Adiciona o diretório 'scr' ao sys.path para que possamos importar os módulos corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.input_api import app as input_api_app
from api.output_api import app as output_api_app
from communication.messenger import send_whatsapp_message
from data_input import load_structured_data, load_unstructured_data
from processing.data_processing import process_data
from processing.message_builder import build_message
from dashboard import app as dashboard_app
from logger import logger

# Função para iniciar o Flask
def start_flask_app(app, port):
    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)

def main():
    logger.info('Starting main process')

    # começa a API de entrada em uma thread separada
    input_api_thread = threading.Thread(target=start_flask_app, args=(input_api_app, 5000))
    input_api_thread.start()

    # começa a API de saída em uma thread separada
    output_api_thread = threading.Thread(target=start_flask_app, args=(output_api_app, 5001))
    output_api_thread.start()

    # começa o dashboard em uma thread separada
    dashboard_thread = threading.Thread(target=start_flask_app, args=(dashboard_app, 8050))
    dashboard_thread.start()

    # Define o caminho base para os dados
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_sample'))

    # carrega os dados estruturados e não estruturados
    structured_data_path = os.path.join(base_path, 'sample_estruturados.csv')
    unstructured_data_path = os.path.join(base_path, 'sample_nao_estruturados.csv')

    structured_data = load_structured_data(structured_data_path)
    unstructured_data = load_unstructured_data(unstructured_data_path)

    # processa os dados e retorna os pacientes elegíveis e os dados não estruturados processados 
    eligible_patients, processed_unstructured_data = process_data(structured_data, unstructured_data)

    if eligible_patients is not None:
        # envia mensagens para os pacientes elegíveis utilizando a API do WhatsApp
        for index, patient in eligible_patients.iterrows():
            message = build_message(patient)
            send_whatsapp_message(patient['TEL'], message)

    logger.info('Main process completed')

if __name__ == "__main__":
    main()