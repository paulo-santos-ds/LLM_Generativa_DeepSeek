import streamlit as st
import requests

# Interface do Streamlit
st.title("@Prasds IA Generativa")

# Abas para separar a geração de texto e as configurações da API
tab1, tab2 = st.tabs(["Gerar Texto", "Configurações da API"])

# Função para gerar texto com a IA do DeepSeek-R1
def generate_text(prompt, api_url, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("text", "").strip()
    else:
        st.error("Erro ao gerar texto. Verifique sua chave de API e tente novamente.")
        return ""

# Aba 1: Geração de Texto
with tab1:
    st.write("Faça uma pergunta para que a IA generativa crie um texto personalizado para você .")

    # Entrada do usuário
    user_prompt = st.text_area("Digite aqui:", "Escreva algo...")

    # Botão para gerar texto
    if st.button("Gerar Texto"):
        with st.spinner("Gerando texto..."):
            # Recupera as configurações da API da sessão
            api_url = st.session_state.get("api_url", "https://api.deepseek.com/v1/generate")
            api_key = st.session_state.get("api_key", "sua_chave_api_aqui")
            generated_text = generate_text(user_prompt, api_url, api_key)
            st.write(generated_text)

st.markdown("Linkedin:  https://www.linkedin.com/in/prasds")

# Aba 2: Configurações da API
with tab2:
    st.write("Configurações da API do DeepSeek-R1")

    # Campos para configurar a URL da API e a chave de API
    api_url = st.text_input("URL da API", "https://api.deepseek.com/v1/generate")
    api_key = st.text_input("Chave da API", "sua_chave_api_aqui", type="password")

    # Botão para salvar as configurações
    if st.button("Salvar Configurações"):
        st.session_state["api_url"] = api_url
        st.session_state["api_key"] = api_key
        st.success("Configurações salvas com sucesso!")
