# Flask DANFE Generator

Este é um aplicativo web simples desenvolvido em Flask que permite o upload de arquivos XML de notas fiscais eletrônicas (NF-e) e gera o Documento Auxiliar da Nota Fiscal Eletrônica (DANFE) em formato PDF.

## Funcionalidades

- Upload de arquivos XML de NF-e.
- Geração de DANFE em PDF a partir do XML enviado.
- Download do PDF gerado diretamente pelo navegador.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- Flask
- brazilfiscalreport (para gerar o DANFE)
  
## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

    **Nota:** Se o arquivo `requirements.txt` ainda não existir, crie um com o seguinte conteúdo:

    ```text
    Flask
    brazilfiscalreport
    ```

4. **Configuração:**

   Crie um arquivo `config.py` com as seguintes configurações:

    ```python
    import os

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output')
    LOGO_PATH = os.path.join(BASE_DIR, 'static', 'logo.png')
    ```

5. **Crie os diretórios necessários:**

    Se os diretórios `uploads`, `output` e `static` (com um arquivo de logo) ainda não existirem, crie-os manualmente ou o aplicativo Flask irá criá-los automaticamente.

    ```bash
    mkdir -p uploads output static
    ```

6. **Adicione o arquivo de logo:**

    Coloque a imagem de logo em `static/logo.png` (ou altere o caminho `LOGO_PATH` conforme necessário).

## Como Executar

1. **Inicie o servidor Flask:**

    ```bash
    python app.py
    ```

2. **Acesse o aplicativo:**

   Abra seu navegador e vá para `http://127.0.0.1:5000/`.

## Uso

1. Na página principal, faça o upload de um arquivo XML de NF-e.
2. Após o upload, o DANFE será gerado e exibido diretamente no navegador como um PDF.

## Estrutura do Projeto

```plaintext
/
│
├── app.py                # Arquivo principal do aplicativo Flask
├── config.py             # Configurações do aplicativo
├── requirements.txt      # Dependências do Python
├── templates/
│   └── upload.html       # Template HTML para a página de upload
├── uploads/              # Diretório para armazenar arquivos XML enviados
├── output/               # Diretório para armazenar PDFs gerados
└── static/
    └── logo.png          # Logotipo utilizado no DANFE
#   F l a s k - D A N F E - G e n e r a t o r 
 
 
