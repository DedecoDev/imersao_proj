# app.py
from flask import Flask, render_template
from folhasp import raspador_folhasp
from oglobo import raspador_oglobo
from portal360 import raspador_portal360
from portal360anuncio import raspador_portal360anuncio
from policia_federal import raspador_pfederal
from camarasp import raspador_camarasp
from portal360governo import raspador_portal360gov  # Importe a função raspador_portal360gov

app = Flask(__name__)

@app.route('/')
def index():
    # Executar os raspadores
    html_folha, folha_id = raspador_folhasp()
    html_oglobo, oglobo_id = raspador_oglobo()
    html_portal360, portal360_id = raspador_portal360()
    html_portall360, portal360anuncio_id = raspador_portal360anuncio()
    html_pfederal, pfederal_id = raspador_pfederal()
    html_camarasp, camarasp_id = raspador_camarasp()

    # Adicionar a execução do raspador_portal360gov
    html_portal360gov, portal360gov_id = raspador_portal360gov()

    return render_template('index.html', 
                           folha=html_folha, folha_id=folha_id,
                           oglobo=html_oglobo, oglobo_id=oglobo_id,
                           portal360=html_portal360, portal360_id=portal360_id,
                           portall360=html_portall360, portall360_id=portal360anuncio_id,
                           pfederal=html_pfederal, pfederal_id=pfederal_id,
                           camarasp=html_camarasp, camarasp_id=camarasp_id,
                           portal360gov=html_portal360gov, portal360gov_id=portal360gov_id)

if __name__ == '__main__':
    app.run(debug=True)
