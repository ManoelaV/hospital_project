def build_message(patient):
    try:
        # Ajuste para usar as colunas disponíveis no arquivo CSV
        id = patient['ID']
        solicitante = patient['SOLICITANTE']
        data = patient['DATA']
        telefone = patient['TEL']
        receita = patient['DS_RECEITA']
        
        message = (
            f"Olá {solicitante},\n"
            f"ID: {id}\n"
            f"Data: {data}\n"
            f"Telefone: {telefone}\n"
            f"Receita: {receita}\n"
            "Por favor, siga as instruções da receita."
        )
        return message
    except KeyError as e:
        logger.error(f"KeyError: {e}")
        return "Erro ao construir a mensagem."

# Example usage
if __name__ == "__main__":
    import pandas as pd
    from logger import logger

    # Exemplo de paciente
    patient = pd.Series({
        'ID': 9458,
        'DATA': '2020-04-25',
        'TEL': '1100009458',
        'CPF': '12345679458',
        'SOLICITANTE': 'Gustavo',
        'CD_TUSS': 40901114,
        'DS_RECEITA': 'Mamas'
    })

    message = build_message(patient)
    print(message)