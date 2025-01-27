# @Prasds IA Generativa
Este projeto é uma aplicação web desenvolvida utilizando a biblioteca Streamlit em Python, que permite a geração de texto através de uma IA generativa, especificamente a DeepSeek-R1. A aplicação é dividida em duas abas principais: uma para a geração de texto e outra para a configuração da API necessária para a comunicação com o serviço de IA. O Streamlit simplifica o desenvolvimento de interfaces web, permitindo que o foco seja direcionado para a lógica de negócio e a integração com a API da IA. A aplicação é altamente customizável, permitindo que os usuários ajustem as configurações da API conforme necessário.

## Estrutura Organizada
```bash
LLM_GENERATIVA_DEEPSEEK
│
├── src/                     # Código-fonte principal
│   ├── app_deepseek.py      # Arquivo principal da aplicação
│   ├── config.py            # Configurações da aplicação
│   ├── utils/               # Funções auxiliares ou utilitárias
│   └── __init__.py          # Para identificar como pacote Python
│
├── images/                  # Arquivos de mídia (exemplo: gráficos ou imagens)
│
├── docs/                    # Documentação do projeto
│   └── readme.md            # Documentação principal
│
├── config/                  # Arquivos de configuração
│   └── .env                 # Configurações sensíveis (API keys, tokens, etc.)
│
├── requirements.txt         # Dependências do Python
├── .gitignore               # Ignorar arquivos desnecessários no Git
├── venv/                    # Ambiente virtual Python (não recomendado versionar)
└── README.md                # Explicação geral do projeto
```

## Funcionalidades

1. Geração de Texto:

+ Insira uma pergunta na caixa de texto.

+ Clique em "Gerar Texto" para receber uma resposta gerada pela IA.

2. Configurações da API:

+ Acesse a aba "Configurações da API" para inserir a URL da API e sua chave de API.

+ Salve as configurações para que a aplicação funcione corretamente.

## Geração de Texo
![image](https://github.com/paulo-santos-ds/LLM_Generativa_DeepSeek/blob/main/imagens/interface.png)

## Aba de Configuração
![image](https://github.com/paulo-santos-ds/LLM_Generativa_DeepSeek/blob/main/imagens/configuracao_api.png)

## Como Usar

## Pré-requisitos
## Antes de executar o projeto, certifique-se de ter instalado:

+ Python 3.8 ou superior.

+ As bibliotecas listadas no arquivo requirements.txt.

## Conclusão
A interface oferece uma experiência intuitiva e fluida, facilitando a inserção de prompts e a visualização dos textos gerados de forma clara e eficiente. A aba de configurações adiciona flexibilidade ao aplicativo, permitindo ajustes rápidos e personalizações sem a necessidade de modificar o código-fonte.
A API de IA generativa, servindo como um ponto de partida robusto para futuras expansões. Possibilidades incluem a adição de mais parâmetros para aprimorar a geração de textos ou a integração com outras APIs, ampliando suas funcionalidades. Trata-se de uma ferramenta poderosa e versátil, ideal para explorar o potencial da IA em aplicações reais e impulsionar a inovação em diversos contextos.

## 🚀 Como Usar

1. Clone o repositório
```bash
 https://github.com/paulo-santos-ds/LLM_Generativa_DeepSeek
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app_deepseek.py
```

## Contato:
Linkedin: 
``` 
 https://www.linkedin.com/in/prasds
 ```

blog: 
``` 
https://prasds.blogspot.com/ 
```