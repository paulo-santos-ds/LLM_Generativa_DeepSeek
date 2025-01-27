
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa as variáveis de ambiente
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

# Verifica se as variáveis foram carregadas corretamente
if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
    raise ValueError("Chave da API ou URL não configuradas no arquivo .env")
   
