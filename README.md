# Hotsite Petshop "Melhor Amigo"

Hotsite desenvolvido para o Petshop "Melhor Amigo", utilizando Python, Flask e MySQL. O projeto é uma aplicação web completa e funcional que atende aos requisitos do cliente, incluindo a promoção de produtos e serviços e a captação de contatos.

## ✨ Funcionalidades

* **Página Inicial:** Apresentação da marca, serviços e promoções.
* **Página de Produtos e Serviços:** Detalhamento dos itens oferecidos, como banho, tosa e rações.
* **Galeria de Fotos:** Exibição dos clientes pets do estabelecimento.
* **Página de Contato:** Formulário funcional integrado com banco de dados MySQL para salvar as mensagens dos visitantes.
* **Design Responsivo:** Layout adaptado para visualização em desktops e dispositivos móveis.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Flask
* **Banco de Dados:** MySQL
* **Frontend:** HTML5, CSS3
* **Versionamento:** Git, GitHub

## 🚀 Instalação e Execução

Siga os passos abaixo para executar o projeto em sua máquina local.

#### Pré-requisitos

* Python 3.x
* Git
* MySQL Server

#### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/WillVernen/petshop-melhor-amigo.git](https://github.com/WillVernen/petshop-melhor-amigo.git)
    cd petshop-melhor-amigo
    ```

2.  **Crie e configure o banco de dados** executando os seguintes comandos no seu cliente MySQL:
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

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv
    
    # Ativar (Windows)
    venv\Scripts\activate
    
    # Ativar (macOS/Linux)
    source venv/bin/activate
    ```

4.  **Instale as dependências** do projeto:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure a conexão com o banco de dados** no arquivo `app.py`, alterando as linhas a seguir com suas credenciais:
    ```python
    app.config['MYSQL_USER'] = 'seu_usuario_mysql'
    app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
    ```

6.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

7.  Abra seu navegador e acesse: `http://127.0.0.1:5000`

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
