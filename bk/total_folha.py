# app.py
from flask import Flask, render_template
from folhasp_total import raspador_folhasp

app = Flask(__name__)

@app.route('/')
def index():
    # Executar os raspadores
    html_folha, folha_id = raspador_folhasp()

    return render_template('folhasp.html', 
                           folha=html_folha, folha_id=folha_id)

if __name__ == '__main__':
    app.run(debug=True)
