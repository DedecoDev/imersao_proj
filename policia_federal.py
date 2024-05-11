# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def raspador_pfederal():
    # URL da página
    url = 'https://www.gov.br/pf/pt-br/assuntos/noticias/ultimas-noticias'

    # Requisição à página
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parse do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

        # Encontrar as notícias na página
        pfederal = soup.find_all('h2', class_='tileHeadline')

        # Limite de 6 notícias
        pfederal = pfederal[:10]

        # Criar uma lista para armazenar os dados HTML formatados
        html_pfederal = []

        # Iterar sobre as notícias
        for noticia in pfederal:
            # Extrair título e link da notícia
            titulo = noticia.find('a').text.strip()
            link = noticia.find('a')['href']

            # Obter a data e hora da atualização
            data_hora_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            # Formatar a string HTML e adicioná-la à lista
            html_noticia = f"""
                    <div class="LinhaDaNoticia">
                        <span>Polícia Federal</span>
                        <h3>{titulo}</h3>
                        <h4></h4>
                        <h5>{data_hora_atualizacao}</h5>
                        <div class="LinkLerMateria"><a href="{link}" target="_blank">Ler Matéria</a></div>
                    </div>
                  """
            
            html_pfederal.append(html_noticia)

        # Criar o HTML final unindo todas as notícias
        html_final = '\n'.join(html_pfederal)

        # Adicionar ao bloco da notícia com o ID específico
        html_pfederal = f"""
            <div class="BlocoLinhaDaNoticia" id="PoliciaFederal">
                <div class="LinhaDaNoticia ChamaBoxNoticia">Polícia Federal</div>
                {html_final}
            </div>
        """

        return html_pfederal, "PoliciaFederal"
