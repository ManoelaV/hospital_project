import sys
import os
import re
import pandas as pd

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from logger import logger

# Função para processar dados
def process_data(structured_data, unstructured_data):
    try:
        logger.info('Processing data')
        
        # Exemplo de regra de negócio: Filtrar pacientes com CD_TUSS específico
        eligible_patients = structured_data[structured_data['CD_TUSS'] == 40901114]
        
        # Processamento de dados não estruturados
        unstructured_data['exame'] = unstructured_data['DS_RECEITA'].apply(extract_exam)
        # Exemplo de processamento de dados não estruturados: Filtrar exames de RM
        logger.info(f'Found {len(eligible_patients)} eligible patients')
        return eligible_patients, unstructured_data
    except Exception as e:
        logger.error(f'Error processing data: {e}')
        return None, None

# Função para extrair tipo de exame
def extract_exam(text):
    if pd.isna(text):
        return 'Desconhecido'
    # Exemplo de expressão regular para extrair tipo de exame
    match = re.search(r'\b(US|RM|TC|RX)\b', str(text))
    if match:
        return match.group(0)
    return 'Desconhecido'

# Exemplo de uso
if __name__ == "__main__":    
    from data_input import load_structured_data, load_unstructured_data
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_sample'))
    structured_data_path = os.path.join(base_path, 'sample_estruturados.csv')
    unstructured_data_path = os.path.join(base_path, 'sample_nao_estruturados.csv')

    structured_data = load_structured_data(structured_data_path)
    unstructured_data = load_unstructured_data(unstructured_data_path)
    
    eligible_patients, processed_unstructured_data = process_data(structured_data, unstructured_data)
    print(eligible_patients.head())
    print(processed_unstructured_data.head())