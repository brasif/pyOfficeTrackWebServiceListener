from flask import Flask, request
from xml.etree import ElementTree as ET
import logging
from datetime import datetime

app = Flask(__name__)

# Configuração do logger
logging.basicConfig(filename='teste.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/', methods=['POST'])
def feed_data():
    # Verifica se a requisição é do tipo POST
    if request.method == 'POST':
        # Verifica se o tipo de conteúdo é application/x-www-form-urlencoded
        if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            # Obtem o conteúdo da requisição
            request_string = request.form['RequestString']
            
            # Grava o request_string no arquivo de log com a data e hora de acesso
            logging.info(f'RequestString: {request_string}')
            
            # Parseia o XML
            root = ET.fromstring(request_string)
            
            # Extraindo dados do XML
            event_type = root.find('EventType').text
            entry_type = root.find('EntryType').text
            entry_source = root.find('EntrySource').text
            #print(root)
            # Continue com os outros campos conforme necessário
            
            # Aqui você pode realizar a lógica de processamento dos dados recebidos
            
            # Retorna uma resposta (pode ser um XML ou qualquer outra coisa conforme sua necessidade)
            return '_OK_'
        else:
            return 'Erro: Tipo de conteúdo inválido. Esperado application/x-www-form-urlencoded.'
    else:
        return 'Erro: Apenas requisições POST são aceitas neste endpoint.'

if __name__ == '__main__':
    app.run(debug=True)
