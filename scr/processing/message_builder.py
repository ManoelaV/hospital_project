def build_message(patient):
    """
    Constrói uma mensagem personalizada para o paciente.
    
    Args:
        patient (pd.Series): Dados do paciente.
    
    Returns:
        str: Mensagem personalizada.
    """
    name = patient['name']
    message = f"Olá {name}, por favor agende seu exame."
    return message

# Example usage
if __name__ == "__main__":
    import pandas as pd

    # Exemplo de dados de paciente
    patient_data = {
        'name': 'João',
        'phone': '+5511999999999',
        'status': 'pending'
    }
    patient = pd.Series(patient_data)
    
    message = build_message(patient)
    print(message)