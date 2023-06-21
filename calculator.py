from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        weight = float(request.form.get('weight', 0))
        height = float(request.form.get('height', 0))
        age = float(request.form.get('age', 0))
        sex = request.form.get('sex', '')

        if sex == 'female':
            result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        elif sex == 'male':
            result = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            result = 'Sexo inválido'

        # Usando a biblioteca pandas para manipular os dados se necessário
        df = pd.DataFrame({'Peso': [weight], 'Altura': [height], 'Idade': [age], 'Sexo': [sex], 'TMB': [result]})
        df.to_csv('calculations.csv', mode='a', header=not os.path.exists('calculations.csv'))

        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
