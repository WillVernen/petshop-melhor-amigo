# Projeto Hotsite: Petshop "Melhor Amigo"

Este é o arquivo de entrega do projeto de hotsite para o Petshop "Melhor Amigo", conforme solicitado no briefing.

## Pré-requisitos

Para executar este projeto localmente, é necessário ter os seguintes softwares instalados:
* Python 3.x
* MySQL Server

## Instruções de Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto.

### 1. Configuração do Banco de Dados

- Abra seu cliente MySQL e execute os seguintes comandos para criar o banco de dados e a tabela necessários:

```sql
CREATE DATABASE petshop_db;

USE petshop_db;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    mensagem TEXT NOT NULL,
    newsletter BOOLEAN,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Configuração da Aplicação

1.  **Extraia o arquivo .ZIP** em um local de sua preferência.
2.  **Abra a pasta do projeto** em um terminal ou prompt de comando.
3.  **Crie um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    ```
4.  **Ative o ambiente virtual:**
    -   **Windows:** `venv\Scripts\activate`
    -   **macOS/Linux:** `source venv/bin/activate`
5.  **Instale as dependências** do projeto com o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```
6.  **Configure a conexão com o banco de dados:**
    -   Abra o arquivo `app.py`.
    -   Localize e altere as seguintes linhas com suas credenciais do MySQL:
        ```python
        app.config['MYSQL_USER'] = 'seu_usuario_mysql'
        app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
        ```

### 3. Executando o Servidor

- Com tudo configurado, execute o seguinte comando no terminal:
  ```bash
  python app.py
  ```
- Abra seu navegador e acesse a URL: **http://127.0.0.1:5000**

O site estará no ar e totalmente funcional.
