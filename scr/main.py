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

def start_flask_app(app, port):
    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)

def main():
    logger.info('Starting main process')

    # Start the input API in a separate thread
    input_api_thread = threading.Thread(target=start_flask_app, args=(input_api_app, 5000))
    input_api_thread.start()

    # Start the output API in a separate thread
    output_api_thread = threading.Thread(target=start_flask_app, args=(output_api_app, 5001))
    output_api_thread.start()

    # Start the dashboard in a separate thread
    dashboard_thread = threading.Thread(target=start_flask_app, args=(dashboard_app, 8050))
    dashboard_thread.start()

    # Load data
    structured_data = load_structured_data('../data/sample_estruturados.csv')
    unstructured_data = load_unstructured_data('../data/sample_nao_estruturados.csv')

    # Process data to find eligible patients
    eligible_patients, processed_unstructured_data = process_data(structured_data, unstructured_data)

    if eligible_patients is not None:
        # Send messages via WhatsApp to eligible patients
        for index, patient in eligible_patients.iterrows():
            message = build_message(patient)
            send_whatsapp_message(patient['phone'], message)

    logger.info('Main process completed')

if __name__ == "__main__":
    main()