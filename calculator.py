from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        name = request.form.get('name', '')  # Obter o valor do nome
        weight = request.form.get('weight', 0)  # Obter o valor do peso sem conversão
        weight = float(weight.replace(',', '.'))  # Substituir a vírgula por ponto e converter para float
        height = float(request.form.get('height', 0))
        age = float(request.form.get('age', 0))
        sex = request.form.get('sex', '')

        if sex == 'feminino':
            result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        elif sex == 'masculino':
            result = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

        # Usando a biblioteca pandas para manipular os dados se necessário
        df = pd.DataFrame({'Nome': [name], 'Peso': [weight], 'Altura': [height], 'Idade': [age], 'Sexo': [sex], 'TMB': [result]})
        df['Peso'] = df['Peso'].apply(lambda x: int(x) if x.is_integer() else x)  # Converter para int se for um número inteiro
        df.to_csv('calculations.csv', mode='a', header=not os.path.exists('calculations.csv'), index=False, float_format='%.2f')

        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
