# Importações necessárias:
# request: para acessar os dados enviados no formulário
# redirect, url_for: para redirecionar o usuário após o envio
# flash: para exibir mensagens temporárias ao usuário
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS E DA APLICAÇÃO ---

# Chave secreta para o Flask usar nas mensagens 'flash'
app.secret_key = 'melhoramigo'  # Troque por qualquer string complexa "melhoramigo"

# Configurações de conexão com o banco de dados MySQL
# Ou o IP do seu servidor de banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'       # <<< COLOQUE SEU USUÁRIO DO MYSQL AQUI
app.config['MYSQL_PASSWORD'] = 'root'  # <<< COLOQUE SUA SENHA DO MYSQL AQUI
app.config['MYSQL_DB'] = 'petshop_db'   # O nome do banco de dados que criamos

# Inicializa a extensão MySQL
mysql = MySQL(app)


# --- ROTAS DA APLICAÇÃO ---

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/produtos.html')
def produtos():
    return render_template('produtos.html')


@app.route('/galeria.html')
def galeria():
    return render_template('galeria.html')


@app.route('/contato.html')
def contato():
    return render_template('contato.html')

# --- ROTA PARA PROCESSAR O FORMULÁRIO ---


@app.route('/enviar', methods=['POST'])
def enviar():
    """
    Esta rota só aceita requisições do tipo POST.
    Ela será acionada pelo 'action' do nosso formulário de contato.
    """
    # Verifica se a requisição é um POST
    if request.method == 'POST':
        # Pega os dados dos campos do formulário
        nome = request.form['name']
        email = request.form['email']
        telefone = request.form['phone']
        mensagem = request.form['message']
        # 'request.form.get' é usado para checkboxes, pois se não for marcado, não envia valor.
        # Se 'newsletter' existir, 'sim' será salvo. Caso contrário, 'nao' será salvo.
        newsletter_str = request.form.get(
            'newsletter')  # Retorna 'sim' ou None
        newsletter = True if newsletter_str == 'sim' else False

        # Cria um cursor. É com ele que executamos os comandos SQL.
        cur = mysql.connection.cursor()

        # O comando SQL para inserir os dados na tabela 'contatos'
        # Usamos '%s' como placeholders para evitar injeção de SQL, uma prática de segurança.
        sql = "INSERT INTO contatos (nome, email, telefone, mensagem, newsletter) VALUES (%s, %s, %s, %s, %s)"

        # Executa o comando, passando a tupla de valores
        cur.execute(sql, (nome, email, telefone, mensagem, newsletter))

        # Comita a transação (salva as mudanças no banco de dados)
        mysql.connection.commit()

        # Fecha o cursor
        cur.close()

        # Cria uma mensagem de sucesso para o usuário
        flash('Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.', 'success')

        # Redireciona o usuário de volta para a página de contato
        return redirect(url_for('contato'))


if __name__ == '__main__':
    app.run(debug=True)
