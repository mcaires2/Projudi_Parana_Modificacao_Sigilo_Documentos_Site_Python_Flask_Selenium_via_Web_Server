# Projudi_Parana_Modificacao_Sigilo_Documentos_Site_Python_Flask_Selenium_via_Web_Server
Instalando um servidor Flask para hospedar o site que manipula o sigilo de documentos no Projudi Paraná


O pacote deste github é o ambiente que usei no meu visual studio code
Abra o terminal via Visual Studio Code e instale: 

pip install pip
pip install selenium 
pip install flask

(um de cada vez na linha de comando)

Não esqueça de instalar o python 3 na sua máquina também...

Além destas ferramentas você vai precisar do Jquery e Javascript que já são acionados pelos códigos Html dos arquivos do projeto.

Você vai precisar instalar o chromeDriver na sua máquina, veja como fazer em:
https://chromedriver.chromium.org/downloads

(dica, anote o diretório onde o chromeDriver.exe foi instalado)

Depois de finalizar a instalação do ChromeDriver.exe abra o arquivo deste projeto sigilo_flask_selenium_funcoes.py e mude o caminho de instalação do ChromeDriver.exe na linha 53.
(esta providência, em regra, é necessária para usuários do Windows)
Você pode apagar a menção do caminho absoluto do na linha 53 do script do python  se o ChromeDriver.exe já estiver no PATH do seu sistema operacional Linux ou Windows

# (line 53)
driver= webdriver.Chrome(r'C:\Users\marcos\AppData\Local\SeleniumBasic\chromedriver.exe') 

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


link do vídeo....

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
