# Projeto Hotsite: Petshop "Melhor Amigo"

[cite_start]Hotsite para o Petshop "Melhor Amigo", desenvolvido com Flask, Python e MySQL. [cite_start]O projeto inclui páginas de produtos, galeria de fotos e um formulário de contato funcional. [cite: 13, 14, 15]

## Instalação e Execução

Existem duas maneiras de obter o projeto: baixando o ZIP ou clonando via Git.

### Opção 1: Via `git clone` (Recomendado)

1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone https://github.com/WillVernen/petshop-melhor-amigo.git
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd petshop-melhor-amigo
    ```
3.  Pule para a seção **"Configuração do Ambiente"** abaixo.

### Opção 2: Baixando o .ZIP

1.  Baixe o arquivo `.ZIP` deste repositório.
2.  Extraia o conteúdo em um local de sua preferência.

---

### Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o projeto.

#### 1. Banco de Dados

- Abra seu cliente MySQL e execute os seguintes comandos:

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

#### 2. Aplicação

1.  **Crie um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    ```
2.  **Ative o ambiente virtual:**
    -   **Windows:** `venv\Scripts\activate`
    -   **macOS/Linux:** `source venv/bin/activate`
3.  **Instale as dependências** do projeto:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure a conexão com o banco de dados** no arquivo `app.py`:
    ```python
    app.config['MYSQL_USER'] = 'seu_usuario_mysql'
    app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
    ```

#### 3. Executando o Servidor

- Com tudo configurado, execute o seguinte comando no terminal:
  ```bash
  python app.py
  ```
- Abra seu navegador e acesse: **http://127.0.0.1:5000**

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
