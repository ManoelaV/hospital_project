import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from logger import logger

# Carregar dados
def load_data():
    structured_data = pd.read_csv('../data/sample_estruturados.csv')
    return structured_data

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Dashboard Hospital Project'),

    dcc.Graph(
        id='example-graph'
    ),

    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Atualizar a cada minuto
        n_intervals=0
    )
])

# Callback para atualizar o gráfico
@app.callback(
    Output('example-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    logger.info('Updating graph')
    data = load_data()
    fig = px.bar(data, x='status', y='count', title='Status dos Exames')
    return fig

# Executar o servidor
if __name__ == '__main__':
    logger.info('Starting dashboard')
    app.run_server(debug=True)