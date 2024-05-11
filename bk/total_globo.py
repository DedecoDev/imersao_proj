# app.py
from flask import Flask, render_template
from oglobo_total import raspador_oglobo

app = Flask(__name__)

@app.route('/')
def index():
    # Executar os raspadores
    html_oglobo, oglobo_id = raspador_oglobo()

    return render_template('oglobo.html', 
                           oglobo=html_oglobo, oglobo_id=oglobo_id)

if __name__ == '__main__':
    app.run(debug=True)
