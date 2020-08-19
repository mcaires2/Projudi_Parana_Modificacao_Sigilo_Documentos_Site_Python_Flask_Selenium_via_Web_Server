from flask import render_template,request, redirect,url_for
from app import app

from sigilo_flask_selenium_funcoes import sigilomodificacao,Flask_Selenium




@app.route('/')
@app.route('/index')
def index():
   

   return render_template('marcosteste.html')


   #return render_template('marcosteste.html',title="Home",user=user,posts=posts,teste=Teste)

 #  the interesting here is that jinja2 can create and recreate html code on a loop over a python list 
 # of dicts ...

      # <body>
      #     <h1>Hi, {{user.username}}</h1>
      #     {% for post in posts %}
      #     <div>
      #         <p>{{ post.author.username }} says: <b>{{ post.body }}</b></p>
      #     </div>
      #     {% endfor %}
      # </body>

@app.route('/marcosluzform',methods=['POST', 'GET'])
def submit_form():
   if request.method=='POST':
      try:
         data = request.form.to_dict()
         PROCESSO_NUMERO = data['processoNr'] 
         SEQUENCIAL = data['sequencialNr']
         SEQUENCIAL = int(SEQUENCIAL)
         NIVEL_SIGILO = data['sigiloNivel']
         SUBSEQUENCIAL_1_INCLUIDO=data['subSequencial']
         LOGIN = data['login']
         SENHA = data['password']
         VARA_JUIZO = data['juizo']
      except:
         retorno = 'O método post não funcionou como deveria, operação cancelada...'
         return render_template('marcosteste2.html',feedback=retorno) # sai da rotina e não tenta a automação por erro no post

   try:
      retorno = Flask_Selenium(PROCESSO_NUMERO,SEQUENCIAL,NIVEL_SIGILO,SUBSEQUENCIAL_1_INCLUIDO,LOGIN,SENHA,VARA_JUIZO)
   except:
      retorno = " Erro de Execução da Automação em razão de que o Selenium não pode ser iniciado ou seguir o procedimento até o final, operação cancelada."
      
   return render_template('marcosteste2.html',feedback=retorno)

      




