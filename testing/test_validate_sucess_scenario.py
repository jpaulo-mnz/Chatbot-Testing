
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


df = pd.read_excel('data/success_data_table.xlsx')

def get_data(item, coluna):
    specific_data = df.loc[item, coluna]
    return specific_data

def assert_all_in(data, expected_values, description):
    missing_values = [value for value in expected_values if value not in data]
    assert not missing_values, f"{description}: Valores não encontrados: {missing_values}"

API_KEY = ''
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
    assert "De acordo" in response.text, description == "Pergunta do cliente não está de acordo com a pergunta do chatbot"
    
# 2 - Saudação e Levantamento de Necessidades
@pytest.mark.parametrize("description", ["Saudação e Levantamento de Necessidades"])
def test_client_interaction_2(description):
    response = model.generate_content(initial_client_prompt + get_data(2, chatbot_interaction) + intermediate_client_prompt + get_data(2, client_interaction) + final_client_prompt)
    assert "De acordo" in response.text, description == "Pergunta do cliente não está de acordo com a pergunta do chatbot"
    
# 3 - Detalhamento do Projeto
@pytest.mark.parametrize("description", ["Detalhamento do Projeto"])
def test_client_interaction_3(description):
    response = model.generate_content(initial_client_prompt + get_data(3, chatbot_interaction) + intermediate_client_prompt + get_data(3, client_interaction) + final_client_prompt)
    assert "De acordo" in response.text, description == "Pergunta do cliente não está de acordo com a pergunta do chatbot"
    
# 4 - Seleção e Personalização
@pytest.mark.parametrize("description", ["Seleção e Personalização"])
def test_client_interaction_4(description):
    response = model.generate_content(initial_client_prompt + get_data(4, chatbot_interaction) + intermediate_client_prompt + get_data(4, client_interaction) + final_client_prompt)
    assert "De acordo" in response.text, description == "Pergunta do cliente não está de acordo com a pergunta do chatbot"    

# 5 - Confirmação e Coleta de Informações Adicionais
@pytest.mark.parametrize("description", ["Confirmação e Coleta de Informações Adicionais"])
def test_client_interaction_6(description):
    response = model.generate_content(initial_client_prompt + get_data(5, chatbot_interaction) + intermediate_client_prompt + get_data(5, client_interaction) + final_client_prompt)
    print(response)
    assert "De acordo" in str(response.text), description == "Pergunta do cliente não está de acordo com a pergunta do chatbot"
    
# 6 - Revisão e Confirmação do Projeto (Chatbot)
@pytest.mark.parametrize("description", ["[Revisão e Confirmação do Projeto] - Valida pergunta/resposta do chatbot"])
def test_chatbot_interaction_6(description):
    data = get_data(6, chatbot_interaction)
    expected_values = ["Muito bem", "resumo", "solução", "IA", "implementação"]
    assert_all_in(data, expected_values, description)
    
# 7 - Finalização e Acompanhamento (Chatbot)
@pytest.mark.parametrize("description", ["[Finalização e Acompanhamento] - Valida pergunta/resposta do chatbot"])
def test_chatbot_interaction_7(description):
    data = get_data(7, chatbot_interaction)
    expected_values = ["obrigado", "entrar", "contato", "projeto", "passos"]
    assert_all_in(data, expected_values, description)
    
# 8 - Feedback e Agradecimento (Chatbot)
@pytest.mark.parametrize("description", ["[Feedback e Agradecimento] - Valida pergunta/resposta do chatbot"])
def test_chatbot_interaction_8(description):
    data = get_data(8, chatbot_interaction)
    expected_values = ["Peço", "avalie", "atendimento"]
    assert_all_in(data, expected_values, description)

# 8.1 - Feedback e Agradecimento (Cliente)
@pytest.mark.parametrize("description", ["[Feedback e Agradecimento] - Valida pergunta/resposta do cliente"])
def test_client_interaction_8(description):
    data = str(get_data(8, client_interaction))
    expected_values = ["excelente" or "ruim" or "regular"]
    assert_all_in(data, expected_values, description)
