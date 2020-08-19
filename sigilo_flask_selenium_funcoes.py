from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


#
# Objetivo é modificar o Nível de sigilo de Determinado Sequencial em um Processo Esoecífico no Sistema Projudi do Paraná
#


# <option value="1" selected="selected">Segredo</option>
# <option value="2">Sigilo Mínimo</option>
# <option value="3">Sigilo Médio</option>
# <option value="4">Sigilo Intenso</option>
# <option value="5">Sigilo Absoluto</option></select>



##################################################Funções##################################################################################################################

#
# função auxiliar
#

def sigilomodificacao(contador,NIVEL_SIGILO,driver):
    
    try:
        elemselect = Select(driver.find_element_by_id('idNivelSigilo'))
        elemselect.select_by_visible_text(NIVEL_SIGILO)
    except:
        #print(f'Erro em Selecionar Elemento{SEQUENCIAL}.{contador+1} para Modificação para {NIVEL_SIGILO}.\nAutomação Encerrada.')
        driver.quit()

    time.sleep(1)
    elem = driver.find_element_by_id('saveButton')
    elem.click()
    try:
        driver.switch_to.alert.accept() # qdo se trata de redução do nível de sigilo não existe alerta do javascript
    except:
        pass
    #print(f'Modificação do Sigilo Documento Sequencial {SEQUENCIAL}.{contador+1} efetivada para {NIVEL_SIGILO}')
    
    
# fim da função auxiliar

#
# função principal
#

def Flask_Selenium(PROCESSO_NUMERO,SEQUENCIAL,NIVEL_SIGILO,SUBSEQUENCIAL_1_INCLUIDO,LOGIN,SENHA,VARA_JUIZO):

    
    driver= webdriver.Chrome(r'C:\Users\mcair\AppData\Local\SeleniumBasic\chromedriver.exe') # COLOQUE AQUI O CAMINHO ABSOLUTO DO WINDOWS DE ONDE O SELENIUM CHROME DRIVER.EXE ESTÁ INSTALADO, NO LINUX ELE VAI PARA O PATH AO SER INSTALADO VIA PIP



    #
    # A PARTIR DESTE PONTO NÃO MODIFICAR - AUTOMÁTICO 
    #


    # checar se a opção de sigilo escolhida pelo usuário é válida, caso negativo interrompe a execução do script

    Controle_Opcao_Nivel_Sigilo =0

    if NIVEL_SIGILO =="Segredo": Controle_Opcao_Nivel_Sigilo=1
    if NIVEL_SIGILO =="Sigilo Mínimo": Controle_Opcao_Nivel_Sigilo=1
    if NIVEL_SIGILO =="Sigilo Médio": Controle_Opcao_Nivel_Sigilo=1
    if NIVEL_SIGILO =="Sigilo Intenso": Controle_Opcao_Nivel_Sigilo=1
    if NIVEL_SIGILO =="Sigilo Absoluto": Controle_Opcao_Nivel_Sigilo=1

    if Controle_Opcao_Nivel_Sigilo ==0: 
        #print(f'Escolha do Nível de Sigilo "{NIVEL_SIGILO}" Inexistente Dentre as Opções Permitidas.\nAutomação Encerrada')
        raise SystemExit

    # fim da checagem da escolha do usuário em relação ao nível de sigilo


    # rotina que pergunta se o sub movimento .1 tb terá o sigilo modificado (por vezes é o movimento que se usa para certidão da juntada dos outros movimentos)

    # SUBSEQUENCIAL_1_INCLUÍDO = input(f'O sequencial {SEQUENCIAL}.1 também deve ter o sigilo modificado?(S/N)').upper()
    # SUBSEQUENCIAL_1_INCLUÍDO= SUBSEQUENCIAL_1_INCLUÍDO[0] # vou armazenar apenas a primeira letra - transformada em maiuscula se caso for  da resposta do usuário, <S> ou <N>

    SUBSEQUENCIAL_1_INCLUIDO = SUBSEQUENCIAL_1_INCLUIDO.upper()
    if (SUBSEQUENCIAL_1_INCLUIDO !="S" and SUBSEQUENCIAL_1_INCLUIDO !="N"):SUBSEQUENCIAL_1_INCLUIDO ="S"


    if (SUBSEQUENCIAL_1_INCLUIDO=='S'):
        #print(f' A opção escolhida foi no sentido de que o sub movimento {SEQUENCIAL}.1 também terá o sigilo modificado.')
        controleSequencial =0
    else:
        #print(f' A opção escolhida foi no sentido de que o sub movimento {SEQUENCIAL}.1 NÃO terá o sigilo modificado.')
        controleSequencial =1

    # fim da rotina de definição do submovimento .1


    #
    # Dados informados, automação propriamente iniciada utilizando Selenium
    #



    driver.get (r'https://projudi2.tjpr.jus.br/projudi/usuario/logon.do?actionType=inicio&r=0.5366016759244643')
    time.sleep(1)

    
    #login e senha

    try:
        elem = driver.find_element_by_xpath("//*[@id='login']")
        elem.clear()
        elem.send_keys(LOGIN)

        elem = driver.find_element_by_xpath("//*[@id=\'senha\']")
        elem.clear()
        elem.send_keys(SENHA)
        time.sleep(1)

        elem = driver.find_element_by_xpath("//*[@id='btEntrar']")
        elem.click()
    except:
        #print("Site Projudi Iniciado mas com problemas.\nTente Novamente mais tarde.\nAutomação Encerrada")
        pass


    try:
        elem = driver.find_element_by_xpath("//a[contains(text(),'" + VARA_JUIZO + "')]")
        elem.click()
    except:
        #print("Vara ou Juízo não Encontrado ou Desnecessário")
        pass

    time.sleep(1)

    driver.get ("https://projudi2.tjpr.jus.br/projudi/processo/buscaProcesso.do?actionType=iniciarSimples")

    i = 0


    # rotina que localiza formulário de busca simples no Projudi, se não encontrar encerra o script

    for x in range(6):
        try:
            elemBuscarProcessoSimplesForm = driver.find_element_by_id('buscaProcessoForm')
            #print(f'Formulário de Busca de Processo Encontrado na {x+1}ª tentativa')
            controle=0
            break
        except:
            time.sleep(1)
            controle = 1
            
    if controle >0: 
        #print('Elemento HTML Não Encontrado.\n Automação encerrada')
       ## driver.quit()
       pass

    # fim da rotina de controle do formulário de busca simples do processo

    # form de buscar processo na tela, achar o campo e descarregar o conteúdo do número de processo informado na variável PROCESSO_NÚMERO

    elem = driver.find_element_by_id('numeroProcesso')
    elem.clear()
    elem.send_keys(PROCESSO_NUMERO)
    time.sleep(1)

    elemBuscarProcessoSimplesForm.submit() # submit no formulário = clicar o enter
    time.sleep(1)
    #print(f'Processo Número: {PROCESSO_NUMERO} localizado, interação com modificações de sigilo iniciada')


    # rotina que vai localizar o sequencial informado pelo usuário - checar se existe

    SEQUENCIAL =str(SEQUENCIAL) # converter integer to string 


    for x in range(6):
        try:
            elemSequencial = driver.find_element_by_xpath("(.//td[not(contains(text(),':'))][contains(text(),'" + SEQUENCIAL + "')]/..//b[1]//a[1])")
            #print(f'Sequencial {SEQUENCIAL} encontrado na {x+1}ª tentativa')
            controle=0
            break
        except:
            time.sleep(1)
            controle = 1
            
    if controle >0: 
        #print(f'Sequencial {SEQUENCIAL} Não Encontrado. \nAutomação encerrada')
       driver.quit()
       pass

    # fim da rotina que checa existência do sequencial



    # início do loop para modificaçao do siglo nos sequenciais
    
    elemSequencial.click()


    # pegando lista de elementos html para Alterar Nível de Sigilo
    time.sleep(1)
    try:
        elemSequencialSigilo = driver.find_elements_by_partial_link_text("Alterar Nível do Sigilo")
        #print('Lista dos Elementos HTML para modificação de sigilo localizada' )
        tamanho_array_elementos =len(elemSequencialSigilo)
    except:
        #print(f'Lista dos Elementos HTML não localizada. \nAutomação encerrada')
        driver.quit()
        pass


    # - loop modificação efetiva do sigilo com função auxiliar

    
        

    #
    # Loop de modificação do Sigilo Documentos 
    #

    contador=0
    for item in range(tamanho_array_elementos):
        time.sleep(1)
        if contador >= controleSequencial:
            elemSequencialSigilo = driver.find_elements_by_partial_link_text("Alterar Nível do Sigilo")
            elemSequencialSigilo[contador].click()
            sigilomodificacao(contador,NIVEL_SIGILO,driver)
        contador = contador +1


    # fim do loop 
    elem = driver.find_element_by_id('backButton')
    elem.click()
    time.sleep(1)

    #print(' ')
    #print(' ')
    #print(f'Modificação do sigilo dos documentos para {NIVEL_SIGILO}, no Processo Número {PROCESSO_NUMERO}, finalizada com sucesso.')

    driver.quit()
    return "Execução Modificação do Sigilo Processual no Projudi Bem Sucedida - :)"


