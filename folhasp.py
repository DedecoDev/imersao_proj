# -*- coding: utf-8 -*-
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def raspador_folhasp():
    # URL do site
    url = 'https://www1.folha.uol.com.br/poder/'

    # Requisição à página com especificação da codificação
    response = requests.get(url, headers={'Content-Type': 'text/html; charset=utf-8'})

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parse do conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

        # Encontrar as notícias na página
        folha_noticias = soup.find_all('h2', class_='c-headline__title')

        # Limite de 6 notícias
        folha_noticias = folha_noticias[:10]

        # Criar uma lista para armazenar os dados HTML formatados
        html_folha = []

        # Iterar sobre as notícias
        for noticia in folha_noticias:
            # Extrair título da notícia
            titulo = noticia.text.strip()

            # Extrair resumo se disponível
            resumo_tag = noticia.find_next('p', class_='c-headline__standfirst')
            resumo = resumo_tag.text.strip() if resumo_tag else ''

            # Obter a data e hora da atualização
            data_hora_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            # Extrair link da notícia
            link = noticia.find_parent('a')['href']

            # Formatar a string HTML e adicioná-la à lista
            html_noticia = f"""
                    <div class="LinhaDaNoticia">
                        <span>FOLHA DE SP</span>
                        <h3>{titulo}</h3>
                        <h4>{resumo}</h4>
                        <h5>{data_hora_atualizacao}</h5>
                        <div class="LinkLerMateria"><a href="{link}" target="_blank">Ler Matéria</a></div>
                    </div>
                  """
            
            html_folha.append(html_noticia)

        # Criar o HTML final unindo todas as notícias
        html_final = '\n'.join(html_folha)

        # Adicionar ao bloco da notícia com o ID específico
        html_folha = f"""
            <div class="BlocoLinhaDaNoticia" id="FolhaSP">
                <div class="LinhaDaNoticia ChamaBoxNoticia">FOLHA DE SP</div>
                {html_final}
            </div>
        """

        return html_folha, "FolhaSP"

