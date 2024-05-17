# Estrutura de testes do AI Chatbot: validando a precisão e a relevância contextual
Esse desafio técnico consiste em desenvolver um conjunto de perguntas e respostas para a prospecção de projetos de software com AI. para isso, deve-se elaborar testes que incluam perguntas e respostas, verificando a validade das respostas (identificando respostas fora do tópico ou sem sentido). As informações sobre a validade das respostas podem ser simuladas (fornecidas como saída esperada). A partir desses dados, deve-se propor um método para testar as respostas de forma automática ou manual. 

## 🤖 Simulação de chatbot

Nesse desafio foi preciso criar uma simulação de interações entre o chatbot e um cliente, para facilitar o processo de montagem dessa estrutura de simulação eu segui a recomendação do desafio e criei 2 tabelas com perguntas e respostas para usar como bases de dados e simular diferentes interações para cada tipo de validação, sendo uma base com um cenários de sucesso e outra base com um cenários de falha.

- **Cenários de sucesso**
Na base de dados de sucesso, temos uma interação com um cliente do setor da saúde interessado em implementar uma inteligência artificial generativa para minimizar erros em diagnósticos de doenças crônicas em sua rede de clínicas e hospitais através da análise de dados clínicos pela IA.

- **Cenários de falha**
Na base de dados de erro, temos uma interação com cliente que responde às perguntas do chatbot de maneira totalmente aleatória e isso faz com que o chatbot não consiga evoluir a conversa para passar uma proposta.

## ⚡Automação de testes

O grande objetivo dessa automação de testes é identificar, dentro de uma simulação de interação de uma pessoa com um chatbot, se as perguntas e respostas estão fora do escopo da conversa não possuem sentido. Para desenvolver e executar os testes nessa simulação de chatbot foi usada 2 estratégias diferentes, sendo elas:

**Testando uma validação por meio de “tokens”**

Essa é uma validação muito simples que consiste em definir uma lista de palavras chave “tokens” que são esperadas a cada etapa de uma interação e depois, comparar se no decorrer de uma interação essas palavras foram usadas, caso sim o teste passa e caso não o teste reprova.

**Usando uma inteligência artificial generativa para testar um Chatbot**

Esse é um tipo de validação mais complexa que envolve usar uma inteligência artificial para analisar a qualidade das perguntas e respostas durante uma interação, para isso, é feito um prompt que pede uma IA, nesse caso o Gemini para que avalia se a resposta humana está de acordo com a pergunta do chatbot e vice versa, após fazer essa avaliação essa IA retorna um valor "De acordo" caso não haja nenhum erro aparente e neste caso, o teste passa, mas se a IA retornar "Resposta fora do contexto".

## 📚Embasamento técnico

Nesse projeto, foi usado como embasamento técnico os materiais do ISTQB, “Conselho Internacional de Qualificações em Testes de Software”, sendo usado especificamente materiais de CT-AI, Certified Tester - Artificial Intelligence Testing.

## ⚙️Tecnologias usadas

- **Python** -Linguagem de programação

- **Pip** - Gerenciador de pacotes do Python

- **Pytest** - Framework de testes

- **Pandas** - Biblioteca de extração de dados

- **Gemini** - IA generativa do google

## 📋Pré-requisitos

- Python instalado na versão v3.12.3 ou superior
- Pip instalado na versão 24.0 ou superior
- Acesso a uma API KEY do Gemini

## 🚩Processos de instalação 
Faça o clone do projeto em sua máquina ou caso prefira, baixe os arquivos do projeto em sua máquina e extraia eles e depois, com o terminal aberto na pasta raiz do projeto, execute os comandos abaixo:

`pip install pytest`
`pip install pandas`
`pip install -q -U google-generativeai`

## 🚀Passos para executar

Na pasta raiz do projeto, abra o terminal e execute dos comandos abaixo, sendo o primeiro para executar a automação de testes dos cenarios de sucesso e o segundo para executar os cenarios de falha:

`pytest -W ignore testing/test_validate_sucess_scenario.py`
`pytest -W ignore testing/test_validate_failure_scenario.py`

## 📊 Resultados

