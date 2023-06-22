<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Calculadora TMB</h1>

  <p>A Calculadora TMB é uma aplicação web simples desenvolvida em Python com Flask. Ela permite calcular a Taxa Metabólica Basal (TMB) de uma pessoa com base em seu peso, altura, idade e sexo.</p>

  <p>A aplicação possui um formulário onde o usuário pode inserir os dados necessários para o cálculo da TMB. Após o envio do formulário, a TMB é calculada e exibida na página, além de ser registrada em um arquivo CSV para fins de registro.</p>

  <h2>Funcionalidades</h2>
  <ul>
    <li>Calcula a TMB com base nos dados de peso, altura, idade e sexo.</li>
    <li>Registra os dados no arquivo CSV para registro e análise posterior.</li>
    <li>Interface web simples e fácil de usar.</li>
  </ul>

  <h2>Pré-requisitos</h2>
  <ul>
    <li>Python 3 instalado</li>
    <li>Flask instalado (você pode instalar executando o comando <code>pip install flask</code>)</li>
  </ul>

  <h2>Como executar o projeto</h2>
  <ol>
    <li>Clone o repositório para o seu ambiente local.</li>
    <li>Navegue até o diretório do projeto no terminal.</li>
    <li>Execute o seguinte comando para iniciar o servidor Flask:</li>
  </ol>
  <pre><code>python calculator.py</code></pre>
  <p>Acesse a aplicação no seu navegador em <a href="http://localhost:5000">http://localhost:5000</a>.</p>
  <p>Preencha o formulário com os dados solicitados e clique em "Calcular TMB".</p>
  <p>A TMB calculada será exibida na página, e os dados serão registrados no arquivo <code>calculations.csv</code> no mesmo diretório do projeto.</p>

  <h2>Personalização</h2>
  <p>Você pode personalizar a aparência da aplicação ajustando o arquivo CSS <code>styles.css</code> localizado na pasta <code>static</code>.</p>

  <h2>Contribuição</h2>
  <p>Sinta-se à vontade para contribuir com melhorias para este projeto! Se você tiver sugestões, correções de bugs ou novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.</p>
</body>
</html>
