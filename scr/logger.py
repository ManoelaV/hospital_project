import logging
import os

# Define o caminho absoluto para o diretório de logs
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')

# Normaliza o caminho para garantir compatibilidade com Windows
log_dir = os.path.normpath(log_dir)

# Depuração: Verifique o caminho do diretório
print(f"Diretório de logs: {log_dir}")

# Cria o diretório logs se não existir
try:
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
except Exception as e:
    print(f"Erro ao criar o diretório de logs: {e}")

# Configura o logger
logging.basicConfig(
    filename=os.path.join(log_dir, 'hospital_project.log'), # Caminho do arquivo de log
    level=logging.DEBUG, # Nível de log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Formato da mensagem de log
    datefmt='%Y-%m-%d %H:%M:%S' # Formato da data e hora
)

# Cria um objeto logger
logger = logging.getLogger('hospital_project')

# Exemplo de uso
logger.info('Logger inicializado com sucesso')