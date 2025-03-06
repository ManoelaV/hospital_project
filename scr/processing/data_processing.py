from logger import logger
import re
import pandas as pd

def process_data(structured_data, unstructured_data):
    try:
        logger.info('Processing data')
        
        # Exemplo de regra de negócio: Filtrar pacientes com CD_TUSS específico
        eligible_patients = structured_data[structured_data['CD_TUSS'] == 40901114]
        
        # Processamento de dados não estruturados
        unstructured_data['exame'] = unstructured_data['DS_RECEITA'].apply(extract_exam)
        
        logger.info(f'Found {len(eligible_patients)} eligible patients')
        return eligible_patients, unstructured_data
    except Exception as e:
        logger.error(f'Error processing data: {e}')
        return None, None

def extract_exam(text):
    if pd.isna(text):
        return 'Desconhecido'
    # Exemplo de expressão regular para extrair tipo de exame
    match = re.search(r'\b(US|RM|TC|RX)\b', str(text))
    if match:
        return match.group(0)
    return 'Desconhecido'

# Example usage
if __name__ == "__main__":
    from data_input import load_structured_data, load_unstructured_data
    
    structured_data = load_structured_data('c:/Users/Renan/Documents/GitHub/hospital_project/data_sample/sample_estruturados.csv')
    unstructured_data = load_unstructured_data('c:/Users/Renan/Documents/GitHub/hospital_project/data_sample/sample_nao_estruturados.csv')
    eligible_patients, processed_unstructured_data = process_data(structured_data, unstructured_data)
    print(eligible_patients.head())
    print(processed_unstructured_data.head())