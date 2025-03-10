import pandas as pd
import os
from logger import logger

# Função para carregar dados estruturados
def load_structured_data(filepath):
    try:
        logger.info(f'Loading structured data from {filepath}')
        data = pd.read_csv(filepath)
        logger.info('Structured data loaded successfully')
        return data
    except FileNotFoundError:
        logger.error(f'File not found: {filepath}')
        return pd.DataFrame()  # Retorna um DataFrame vazio
    except Exception as e:
        logger.error(f'Error loading structured data: {e}')
        return pd.DataFrame()  # Retorna um DataFrame vazio

# Função para carregar dados não estruturados
def load_unstructured_data(filepath):
    try:
        logger.info(f'Loading unstructured data from {filepath}')
        data = pd.read_csv(filepath)
        logger.info('Unstructured data loaded successfully')
        return data
    except FileNotFoundError:
        logger.error(f'File not found: {filepath}')
        return pd.DataFrame()  # Retorna um DataFrame vazio
    except Exception as e:
        logger.error(f'Error loading unstructured data: {e}')
        return pd.DataFrame()  # Retorna um DataFrame vazio

# exemplo de uso
if __name__ == "__main__":
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_sample'))
    structured_data_path = os.path.join(base_path, 'sample_estruturados.csv')
    unstructured_data_path = os.path.join(base_path, 'sample_nao_estruturados.csv')

    structured_data = load_structured_data(structured_data_path)
    unstructured_data = load_unstructured_data(unstructured_data_path)
    
    print(structured_data.head())
    print(unstructured_data.head())