import streamlit as st
import requests
from typing import Optional, Dict, Any
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIGenerator:
    def __init__(self):
        # URL atualizada da API DeepSeek
        self.default_api_url = "https://api.deepseek.ai/v1/completions"
        self.max_tokens = 150
        self.temperature = 0.7
        self.model = "deepseek-chat"  # modelo padrão

    def generate_text(self, prompt: str, api_url: str, api_key: str) -> Optional[str]:
     
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        
        try:
            response = requests.post(api_url, json=data, headers=headers)
            
            # Verifica o status code primeiro
            if response.status_code == 404:
                st.error("❌ URL da API inválida. Verifique se a URL está correta nas configurações.")
                return None
            elif response.status_code == 401:
                st.error("❌ Chave da API inválida. Verifique suas credenciais.")
                return None
            
            # Só tenta processar a resposta se o status code for 200
            response.raise_for_status()
            result = response.json()
            
            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"].strip()
            
            st.error("❌ Resposta da API não contém o texto gerado.")
            return None
            
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Erro de conexão: {str(e)}")
            st.error("❌ Não foi possível conectar ao servidor. Verifique sua conexão com a internet.")
            return None
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout na requisição: {str(e)}")
            st.error("❌ A requisição excedeu o tempo limite. Tente novamente.")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição: {str(e)}")
            st.error(f"❌ Erro ao comunicar com a API: {str(e)}")
            return None
        except ValueError as e:
            logger.error(f"Erro ao decodificar JSON: {str(e)}")
            st.error("❌ Erro ao processar a resposta da API. Formato inválido.")
            return None
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
            st.error("❌ Ocorreu um erro inesperado. Tente novamente.")
            return None

def init_session_state():
    #Inicializa variáveis da sessão se não existirem
    if "api_url" not in st.session_state:
        st.session_state.api_url = ""
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""

def validate_api_settings(api_url: str, api_key: str) -> bool:
    #Valida as configurações da API
    if not api_url or not api_url.startswith(("http://", "https://")):
        st.error("❌ A URL da API não é válida. Configure corretamente na aba 'Configurações da API'.")
        return False
    if not api_key:
        st.error("❌ A chave de API não foi fornecida. Configure corretamente na aba 'Configurações da API'.")
        return False
    return True

def render_generation_tab(ai_generator: AIGenerator):
    #Renderiza a aba de geração de texto
    st.write("💭 Faça uma pergunta para que a IA generativa crie um texto personalizado para você.")
    
    user_prompt = st.text_area(
        "Digite aqui:",
        "",
        max_chars=500,
        placeholder="Digite seu prompt aqui...",
        help="Máximo de 500 caracteres"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        generate_button = st.button("🤖 Gerar Texto", use_container_width=True)
    
    if generate_button and user_prompt:
        with st.spinner("🔄 Gerando texto..."):
            if validate_api_settings(st.session_state.api_url, st.session_state.api_key):
                generated_text = ai_generator.generate_text(
                    user_prompt,
                    st.session_state.api_url,
                    st.session_state.api_key
                )
                if generated_text:
                    st.success("✨ Texto gerado com sucesso!")
                    st.write(generated_text)

def render_settings_tab(ai_generator: AIGenerator):
    #Renderiza a aba de configurações
    st.write("⚙️ Configurações da API do DeepSeek")
    
    
    
    api_url = st.text_input(
        "URL da API",
        value=st.session_state.get("api_url", ai_generator.default_api_url),
        placeholder="https://api.deepseek.ai/v1/completions"
    )
    
    api_key = st.text_input(
        "Chave da API",
        value=st.session_state.get("api_key", ""),
        type="password",
        placeholder="Insira sua chave de API"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("💾 Salvar", use_container_width=True):
            if api_url.startswith(("http://", "https://")):
                st.session_state.api_url = api_url.strip()
                st.session_state.api_key = api_key.strip()
                st.success("✅ Configurações salvas com sucesso!")
            else:
                st.error("❌ A URL da API não é válida. Certifique-se de que ela começa com 'http://' ou 'https://'.")

def main():
    st.set_page_config(
        page_title="@Prasds IA Generativa",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 @Prasds IA Generativa")
    
    init_session_state()
    ai_generator = AIGenerator()
    
    tab1, tab2 = st.tabs(["📝 Gerar Texto", "⚙️ Configurações da API"])
    
    with tab1:
        render_generation_tab(ai_generator)
    
    with tab2:
        render_settings_tab(ai_generator)
    
    st.markdown("---")
    #st.markdown("📫 Contato: [LinkedIn](https://www.linkedin.com/in/prasds)")
    st.markdown("📩 Linkedin:   https://www.linkedin.com/in/prasds")

if __name__ == "__main__":
    main()