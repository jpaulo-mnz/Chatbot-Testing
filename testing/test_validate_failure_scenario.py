
import google.generativeai as genai # type: ignore
import pandas as pd # type: ignore
import pytest # type: ignore
import json

client_interaction = 'PERGUNTAS/RESPOSTAS DO CLIENTE'
chatbot_interaction = 'PERGUNTAS/RESPOSTAS DA INTELIGENCIA ARTIFICIAL'

with open('prompt/client_interaction.json', 'r') as file:
    data = json.load(file)
    
initial_client_prompt = data['initial_client_prompt']
intermediate_client_prompt = data['intermediate_client_prompt']
final_client_prompt = data['final_client_prompt']


df = pd.read_excel('data/failure_data_table.xlsx')

def get_data(item, coluna):
    specific_data = df.loc[item, coluna]
    return specific_data

def assert_all_in(data, expected_values, description):
    missing_values = [value for value in expected_values if value not in data]
    assert not missing_values, f"{description}: Valores não encontrados: {missing_values}"

API_KEY = 'AIzaSyATPMuqiLscY3t-W0ZKL4Xj9mOUtok9tI0'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 0 - Mensagem inicial do cliente    
@pytest.mark.parametrize("description", ["Mensagem inicial do cliente"]) 
def test_client_interaction_1(description):
    assert get_data(0, client_interaction) is not None, description == "Os dados retornados estão nulos ou vazios"

# 1 - Início da Interação
@pytest.mark.parametrize("description", ["Início da Interação"]) 
def test_client_interaction_1(description):
    response = model.generate_content(initial_client_prompt + get_data(1, chatbot_interaction) + intermediate_client_prompt + get_data(1, client_interaction) + final_client_prompt)
    assert "Resposta fora do contexto" in response.text, description == "Pergunta do cliente não está Resposta fora do contexto com a pergunta do chatbot"
    
# 2 - Saudação e Levantamento de Necessidades
@pytest.mark.parametrize("description", ["Saudação e Levantamento de Necessidades"])
def test_client_interaction_2(description):
    response = model.generate_content(initial_client_prompt + get_data(2, chatbot_interaction) + intermediate_client_prompt + get_data(2, client_interaction) + final_client_prompt)
    assert "Resposta fora do contexto" in response.text, description == "Pergunta do cliente não está Resposta fora do contexto com a pergunta do chatbot"
    
# 3 - Detalhamento do Projeto
@pytest.mark.parametrize("description", ["Detalhamento do Projeto"])
def test_client_interaction_3(description):
    response = model.generate_content(initial_client_prompt + get_data(3, chatbot_interaction) + intermediate_client_prompt + get_data(3, client_interaction) + final_client_prompt)
    assert "Resposta fora do contexto" in response.text, description == "Pergunta do cliente não está Resposta fora do contexto com a pergunta do chatbot"
    
# 4 - Seleção e Personalização
@pytest.mark.parametrize("description", ["Seleção e Personalização"])
def test_client_interaction_4(description):
    response = model.generate_content(initial_client_prompt + get_data(4, chatbot_interaction) + intermediate_client_prompt + get_data(4, client_interaction) + final_client_prompt)
    assert "Resposta fora do contexto" in response.text, description == "Pergunta do cliente não está Resposta fora do contexto com a pergunta do chatbot"    