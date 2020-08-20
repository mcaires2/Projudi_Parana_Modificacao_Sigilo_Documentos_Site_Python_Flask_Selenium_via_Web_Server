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

(dica, anote o diretório onde o chromeDriver.exe foi instalado)

Depois de finalizar a instalação do ChromeDriver.exe abra o arquivo deste projeto sigilo_flask_selenium_funcoes.py e mude o caminho de instalação do ChromeDriver.exe na linha 53.
(esta providência, em regra, é necessária para usuários do Windows)
Você pode apagar a menção do caminho absoluto do na linha 53 do script do python  se o ChromeDriver.exe já estiver no PATH do seu sistema operacional Linux ou Windows

# (line 53)
driver= webdriver.Chrome(r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe') **

se estiver no Path
driver = webdriver.Chrome()

Após tudo instalado, abra o terminal pelo Visual Studio Code e digite

flask run

Você vai obter uma resposta semelhante a esta:

* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


Copie o ondereço gerado pelo flask para o seu navegador e tecle enter
Pronto, o site está rodando na sua máquina e pronto para uso.
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

driver= webdriver.Chrome(r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe') # COLOQUE AQUI O CAMINHO ABSOLUTO DO WINDOWS DE ONDE O SELENIUM CHROME DRIVER.EXE ESTÁ INSTALADO, NO LINUX ELE VAI PARA O PATH AO SER INSTALADO VIA PIP


# ** Colocar o Selenium no Headless Mode ...


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument('--headless')

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')


driver= webdriver.Chrome(chrome_options=chrome_options, executable_path="r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe'")


# Orientações para instalar a versão do Ubuntu em Modo Desenvolvedor mas Funcional em Cloud


Ambiente Virtual Ubuntu Linux

1 apt install python3-venv

2 sudo apt install python3-venv

 passo 1 e 2 não precisa se repetir, apenas uma vez na máquina ubuntu

4 cd /home/mcaires2/projetos     # entrando no diretório onde vou criar o ambiente virtual (pode mudar)

5 python3.6 -m venv sigilo_site   # sigilo_site aqui é o nome do ambiente virtual que criei, pode ser qq nome

6 source sigilo_site/bin/activate  # ativa o cursor para dentro do ambiente virtual, detalhe: esteja dentro do seu diretório  qdo ativar isso  (no nosso caso teste  cd /home/mcaires2/projetos)

↓↓↓ - a partir da ativação do ambiente virtual vc pode passar a usar só pip ou python porque o ambiente virtual já foi ativado para o python3 ( no passo 2)

7 pip install wheel
8 pip install uwsgi flask
9 pip install python-dotenv

ATENÇÃO:NÃO ESQUECER DE LIBERAR A PORTA 5000 NA MÁQUINA  UBUNTU (sudo ufw allow 5000)NÃO ESQUECER DE LIBERAR A PORTA 5000 NO FIREWALL DO GOOGLE CLOUD OU SEMELHANTE (ENTRADA E SAÍDA)

NAO USAR O DIR DO AMBIENTE VIRTUAL PARA SALVAR SEUS ARQUIVOS DO PROJETO (no nosso caso tudo tem de ser salvo no cd /home/mcaires2/projetos/ enquanto o ambiente virtual que criamos fica no cd /home/mcaires2/projetos/sigilo_site

10 Extrair os arquivos do arquivo .rar e salvar a estrutura de diretórios e files como ali mas dentro do diretório /home/mcaires2/projetos/

11 - Navegue até o diretório  cd /home/mcaires2/projetos/ (local que está salvo Sigilo_Flask_Selenium.py)   e  digite python3 Sigilo_Flask_Selenium.py


12 - Você verá a mensagem no prompt de comando:

3. Você verá a mensagem:
* Serving Flask app "meuprojeto" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


13 - Pronto, abora é só substituir para o IP da Sua Máquina em Cloud e manter :5000 (que é a porta de comunicação). No nosso exemplo ficou http://34.75.217.110:5000/




