# Projudi_Parana_Modificacao_Sigilo_Documentos_Site_Python_Flask_Selenium_via_Web_Server
Instalando um servidor Flask para hospedar o site que manipula o sigilo de documentos no Projudi Paraná


O pacote deste github é o ambiente que usei no meu visual studio code
Abra o terminal via Visual Studio Code e instale: 

pip install pip

pip install selenium 

pip install flask

pip install python-dotenv


(um de cada vez na linha de comando)
(no ambiente Ubuntu linux vc tem de usar o comando pip3 ao invés de pip)

Não esqueça de instalar o python 3 na sua máquina também...

Além destas ferramentas você vai precisar do Jquery e Javascript que já são acionados pelos códigos Html dos arquivos do projeto.

Você vai precisar instalar o chromeDriver na sua máquina, veja como fazer em:
https://chromedriver.chromium.org/downloads

(se estiver no ambiente Ubuntu linux instale digitando o seguinte na linha do CLI: sudo apt install chromium-chromedriver)

(dica, anote o diretório onde o chromeDriver.exe foi instalado ou chromedriver se Ubuntu)

Depois de finalizar a instalação do ChromeDriver abra o arquivo deste projeto sigilo_flask_selenium_funcoes.py e mude o caminho de instalação do ChromeDriver.exe na linha 53.
(esta providência, em regra, é necessária para usuários do Windows)
Você pode apagar a menção do caminho absoluto do na linha 53 do script do python  se o ChromeDriver.exe já estiver no PATH do seu sistema operacional.

# (line 53)
driver= webdriver.Chrome(r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe') **

se estiver no Path
driver = webdriver.Chrome()

se quiser ativar o modo headless porque não tem display nas máquinas em cloud inserir dentro da função Flask_Selenium(...)

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')

driver= webdriver.Chrome(r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe')

ou se estiver no Ubuntu o caminho provavel será:
driver= webdriver.Chrome(chrome_options=chrome_options, executable_path=r'user/lib/bin/chromedriver')

Após tudo instalado, abra o terminal pelo Visual Studio Code e digite

flask run

Você vai obter uma resposta semelhante a esta:

* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Copie o ondereço gerado pelo flask para o seu navegador local e tecle enter
Pronto, o site está rodando na sua máquina local do Windows e pronto para uso.
Veja o vídeo deste projeto funcionando no link 


# link do vídeo....

https://drive.google.com/file/d/1xk2-_TQuv3qPCDfcpXUYleYgWL6dgWFe/view?usp=sharing


*** Lembre-se que este é um ambiente de testes que simula o ambiente de usuário (site) e do servidor que hospedará o site, não deve ser usado em produção

Depois que você fizer o deploy num ambiente de produção tudo isto ficará no back end e não será visto pelo usuário (nem o Selenium, não esqueça de colocar ele em headless mode). A partir do deploy, o usuário irá navegar até o seu site, alimentar as informações e apertar o botão; todo resto acontecerá no webserver...



# English Use Summary:

Jquery and Javascript already embeded on the html code

Install chromeDriver from https://chromedriver.chromium.org/downloads

Take notice the dir where it will be installed on your computer...

After instalaltion do the following:

Open the file sigilo_flask_selenium_funcoes.py and change the full path where the chromedriver.exe has been installed on your windows machine.

(line 53)

driver= webdriver.Chrome(r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe') 


# ** Colocar o Selenium no Headless Mode ...


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')


driver= webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe')

ou se estiver no Ubuntu o caminho provavel será:
driver= webdriver.Chrome(chrome_options=chrome_options, executable_path=r'user/lib/bin/chromedriver')


# Orientações para instalar a versão do Ubuntu em Modo Desenvolvedor mas Funcional em Cloud


Ambiente Virtual Ubuntu Linux

1 apt install python3-venv

2 sudo apt install python3-venv

 passo 1 e 2 não precisa se repetir, apenas uma vez na máquina ubuntu

4 cd /home/marcos/projetos     # entrando no diretório onde vou criar o ambiente virtual (pode mudar)

5 python3.6 -m venv sigilo_site   # sigilo_site aqui é o nome do ambiente virtual que criei, pode ser qq nome

6 source sigilo_site/bin/activate  # ativa o cursor para dentro do ambiente virtual, detalhe: esteja dentro do seu diretório  qdo ativar isso  (no nosso caso teste  cd /home/marcos/projetos)

↓↓↓ - a partir da ativação do ambiente virtual vc pode passar a usar só pip ou python porque o ambiente virtual já foi ativado para o python3 ( no passo 2)

7 pip install wheel
8 pip install uwsgi flask
9 pip install python-dotenv

ATENÇÃO:
NÃO ESQUECER DE LIBERAR A PORTA 5000 NA MÁQUINA  UBUNTU (sudo ufw allow 5000)
NÃO ESQUECER DE LIBERAR A PORTA 5000 NO FIREWALL DO GOOGLE CLOUD OU SEMELHANTE (ENTRADA E SAÍDA)

NAO USAR O DIR DO AMBIENTE VIRTUAL PARA SALVAR SEUS ARQUIVOS DO PROJETO (no nosso caso tudo tem de ser salvo no cd /home/marcos/projetos/ enquanto o ambiente virtual que criamos fica no cd /home/marcos/projetos/sigilo_site

10 Extrair os arquivos do arquivo .rar e salvar a estrutura de diretórios e files como ali mas dentro do diretório /home/marcos/projetos/

11 - Navegue até o diretório  cd /home/marcos/projetos/ (local que está salvo Sigilo_Flask_Selenium.py)   e  digite python3 Sigilo_Flask_Selenium.py


12 - Você verá a mensagem no prompt de comando:

 * Serving Flask app "Sigilo_Flask_Selenium" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


13 - Pronto, agora é só substituir para o IP da Sua Máquina em Cloud e manter :5000 (que é a porta de comunicação). 
No nosso exemplo ficou http://34.75.217.110:5000/


# Implantação Modo Produção Definitivo no Ubuntu 18.04

Depois de testar a versão Windows e Ubuntu no ambiente de desevolvimento passei para a última etapa deste projeto: Implantação Modo Produção Definitivo no Ubuntu 18.04

Por primeiro tive de voltar ao básico:

1 sudo apt-get install libapache2-mod-wsgi

2 sudo service apache2 restart

3 criar um arquivo Sigilo_Flask_Selenium.wsgi com o seguinte conteúdo:


    import sys

    sys.path.insert(0, '/home/marcos/projetos')     # ← adapte para o caminho do diretório do seu projeto


    from app import app as application


4 Salvar o arquivo e colocar no diretório do projeto - no nosso caso /home/marcos/projetos


############


Depois de vencer esta etapa inicial aproveitei para fechar a porta 5000 no google cloud e na máquina ubuntu (tinha aberto para poder rodar a versão de testes lembra!?)


############



5 Esta etapa envolve configurações do servidor apache2, é ponto crucial e fundamental...


5.1 Certifique-se que o seu usuário Ubuntu tem todas as permissões de acesso (veja chmod, chown ou chgrp)

5.2 Crie um arquivo flask_sigilo.conf no seu bloco de notas preferido (não por extensão .txt) e salve no diretório sites-available  do apache2 ( meu caso: /etc/apache2/sites-available/)

5.3 Abra este arquivo para edição e cole:



            <VirtualHost *:80>
            # The ServerName directive sets the request scheme, hostname and port that

            # the server uses to identify itself. This is used when creating

            # redirection URLs. In the context of virtual hosts, the ServerName

            # specifies what hostname must appear in the request's Host: header to

            # match this virtual host. For the default virtual host (this file) this

            # value is not decisive as it is used as a last resort host regardless.

            # However, you must set it for any further virtual host explicitly.

            #ServerName www.example.com



            WSGIDaemonProcess FlaskApp python-path=/home/marcos/projetos/sigilo_site/lib/python3.6/site-packages

            WSGIProcessGroup FlaskApp

            WSGIScriptAlias / /home/marcos/projetos/Sigilo_Flask_Selenium.wsgi

                    ServerAdmin webmaster@localhost

            DocumentRoot /home/marcos/projetos

                
            <Directory /home/marcos/projetos/>

                    Order allow,deny

            Allow from all

            </Directory>

                    

            # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,

            # error, crit, alert, emerg.

            # It is also possible to configure the loglevel for particular

            # modules, e.g.

            #LogLevel info ssl:warn


            ErrorLog ${APACHE_LOG_DIR}/error.log

            CustomLog ${APACHE_LOG_DIR}/access.log combined

                    LimitRequestBody 104857600    

                    # Limite acima é requisições de até 100MB



            # For most configuration files from conf-available/, which are

            # enabled or disabled at a global level, it is possible to

            # include a line for only one particular virtual host. For example the

            # following line enables the CGI configuration for this host only

            # after it has been globally disabled with "a2disconf".

            #Include conf-available/serve-cgi-bin.conf

            </VirtualHost>


            # vim: syntax=apache ts=4 sw=4 sts=4 sr noet



############

NÃO ESQUEÇA DE FAZER ADAPTAÇÕES A VERSÃO DO PYTHON, DO AMBIENTE VIRTUAL, DO NOME DE USUÁRIO, NOME DO ARQUIVO .WSGI NAS LINHAS :

WSGIDaemonProcess FlaskApp python-path=/home/marcos/projetos/sigilo_site/lib/python3.6/site-packages

WSGIScriptAlias / /home/marcos/projetos/Sigilo_Flask_Selenium.wsgi

DocumentRoot /home/marcos/projetos

<Directory /home/marcos/projetos/>


############


6 2 sudo service apache2 restart

7 Fim




Como não sou um cara de sorte tive de enfrentar um erro de permissão do apache2
#################################################################################



A maneira que encontrei para autorizar o Apache2 a lidar com o meu site (salvo num diretorio fora do comum /var/www/html) foi a seguinte:


1 Abrir o arquivo de configuração do apache 2 no caminho /etc/apache2/apache2.conf para edição no nano invocando permissão sudo ($ sudo nano /etc/apache2/apache2.conf)

2 Acrescentar a seguinte diretiva:



    <Directory /home/mcaires2/projetos/> # ← não esquecer de adaptar para diretório do seu projeto/ não esquecer da última / tb antes do>

        Options FollowSymLinks

        AllowOverride All

        Order deny,allow
        
        Allow from all

        Require all granted

    </Directory>

3 Salve e feche o arquivo

4 sudo service apache2 restart (para dar um recarregar no apache2 (sem isso as alterações não entram em vigor)

5 Sim, agora tudo está pronto e 100% ajustado para rodar seu projeto Sigilo Selenium Modificação


#################################################################################


Dicas Finais em razão de algumas incompatibilidades do servidor WSGI e o FLASK 


a. Vão perceber que optei pela função flash('mensagem') para armazenar feedback do caminhar da automação e mostrar para o usuário no final de tudo (como se fosse uma explicação do sucesso ou do erro do procedimento)

b. Como a lingua portuguesa é cheia de acentos e usa cedilhas você vai ter de se adaptar para poder usar nossa lingua mãe, preste atenção:



        b1 coloque a seguinte expressão na linha inicial de cada um dos seus arquivos .py do projeto:

        #-*- coding: utf-8 -*-S

        ela tem a função de viabilizar que o WSGI reconheça caracteres com acentuação e cedilha (cedilha em strings fora do comando flash())


        b2 tem de usar a técnica mais antiga para formatar strings usando conteúdo de variaveis no flash('sua mensagem) e não esqueça de informar u (de unicode antes das aspas duplas que abre a sua string)

        ex.: flash(u"Escolha do Nível de Sigilo '{}' Inexistente Dentre as Possibilidades Permitidas.".format(NIVEL_SIGILO),category="Erro")


        b3 não use cedilha de jeito nenhum dentro das mensagens que você vai gerar com o comando flash(u" sua string aqui"), se colocar cedilha vai ter uma incompatibilidade doida entre o apache2 e o WSGI 

c. Se precisar checar razões de erro do apache2, vá para o log, no Ubuntu 18.04 ele fica /var/log/apache2/error.log


#################################################################################

Aproveite e execute o site.

Dexei um arquivo .Zip com as modificações necessárias para habilitar a função flash no flask (inclusive um novo arquivo chamado config.py que se faz necessário na raiz do projeto)

Vá para o endereço IP da sua máquina, tudo deve estar ajustado agora.


