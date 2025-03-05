# Hospital Project

Este projeto é uma aplicação para gerenciar dados de pacientes, processar informações e enviar mensagens via WhatsApp. Ele inclui APIs para entrada e saída de dados, um dashboard para visualização de dados e funcionalidades de comunicação.

## Estrutura do Projeto

hospital_project/
├── scr/
│   ├── api/
│   │   ├── input_api.py
│   │   ├── output_api.py
│   ├── communication/
│   │   ├── messenger.py
│   ├── logger.py
│   ├── data_input.py
│   ├── processing.py
│   ├── dashboard.py
│   ├── main.py
├── data/
│   ├── sample_estruturados.csv
│   ├── sample_nao_estruturados.csv
├── logs/
│   └── hospital_project.log

## Instalação

1. Clone o repositório:

sh
git clone https://github.com/seu-usuario/hospital_project.git
cd hospital_project

2.Crie um ambiente virtual e ative-o:

python -m venv venv
venv\Scripts\activate  # No Windows
source venv/bin/activate  # No Linux/Mac

3.Instale as dependências:
pip install -r requirements.txt

Configuração-
1.Configure as credenciais do Twilio no arquivo scr/communication/messenger.py:
# Configurações do Twilio
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'whatsapp:+14155238886'

2. Certifique-se de que os arquivos de dados sample_estruturados.csv e sample_nao_estruturados.csv estão no diretório data_sample

Uso-
1.Execute o arquivo main.py para iniciar o sistema:
python [main.py](http://_vscodecontentref_/1)
2. A API de entrada estará disponível em `http://0.0.0.0:5000/`.
3. A API de saída estará disponível em `http://0.0.0.0:5001/`.
4. O dashboard estará disponível em `http://127.0.0.1:8050/`.

## Estrutura dos Arquivos

### `scr/api/input_api.py`

API para receber dados estruturados e não estruturados via endpoints `/api/structured_data` e `/api/unstructured_data`.

### `scr/api/output_api.py`

API para fornecer o status dos envios de mensagens via endpoint `/api/message_status`.

### `scr/communication/messenger.py`

Módulo para enviar mensagens via WhatsApp utilizando a API do Twilio.

### `scr/logger.py`

Configuração do logger para registrar mensagens de log no arquivo `logs/hospital_project.log`.

### `scr/data_input.py`

Módulo para carregar dados estruturados e não estruturados a partir de arquivos CSV.

### `scr/processing.py`

Módulo para processar dados e determinar pacientes elegíveis para receber mensagens.

### `scr/dashboard.py`

Dashboard interativo para visualizar dados utilizando a biblioteca Dash do Plotly.

### `scr/main.py`

Ponto de entrada do sistema que integra todas as funcionalidades e coordena a execução.




