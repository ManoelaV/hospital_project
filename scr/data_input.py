import pandas as pd
from logger import logger

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

# Example usage
if __name__ == "__main__":
    structured_data = load_structured_data('c:/Users/Renan/Documents/GitHub/hospital_project/data_sample/sample_estruturados.csv')
    unstructured_data = load_unstructured_data('c:/Users/Renan/Documents/GitHub/hospital_project/data_sample/sample_nao_estruturados.csv')
    print(structured_data.head())
    print(unstructured_data.head())