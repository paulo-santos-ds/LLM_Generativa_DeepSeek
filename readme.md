# @Prasds IA Generativa
Este projeto é uma aplicação web desenvolvida utilizando a biblioteca Streamlit em Python, que permite a geração de texto através de uma IA generativa, especificamente a DeepSeek-R1. A aplicação é dividida em duas abas principais: uma para a geração de texto e outra para a configuração da API necessária para a comunicação com o serviço de IA.


LLM_GENERATIVA_DEEPSEEK/
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


## Funcionalidades

1. Geração de Texto:

+ Insira uma pergunta na caixa de texto.

+ Clique em "Gerar Texto" para receber uma resposta gerada pela IA.

2. Configurações da API:

+ Acesse a aba "Configurações da API" para inserir a URL da API e sua chave de API.

+ Salve as configurações para que a aplicação funcione corretamente.

## Como Usar

## Pré-requisitos
## Antes de executar o projeto, certifique-se de ter instalado:

+ Python 3.8 ou superior.

+ As bibliotecas listadas no arquivo requirements.txt.

## Conclusão
O uso do Streamlit simplifica o desenvolvimento da interface, permitindo foco na lógica de negócio e integração com a API de IA. A aplicação é customizável, com possibilidades de ajustes nas configurações da API, e pode ser ampliada com novos parâmetros, integração com outras APIs e implantação em nuvem. É uma base sólida para explorar o potencial prático da IA generativa.

## 🚀 Como Usar

1. Clone o repositório
```bash
 https://github.com/paulo-santos-ds
```


2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app_deepseek.py
```