from selenium import webdriver
from time import sleep
import pyautogui
import pandas as pd
import pyperclip



driver = webdriver.Chrome()
driver.get("https://provedor.hubsoft.com.br/")
sleep(2)

pyautogui.click(507, 456)
pyautogui.write("seu email")
pyautogui.moveTo(517, 592)
pyautogui.click()
sleep(5)

pyautogui.click(501,523)
pyautogui.write("sua senha")
pyautogui.click(499, 628)
sleep(6)

#cliente
driver.find_element("xpath", '//*[@id="vertical-navigation"]/ms-navigation/ul/li/ul/li[3]/div/div').click()
sleep(2)
#consulta
driver.find_element("xpath", '//*[@id="vertical-navigation"]/ms-navigation/ul/li/ul/li[3]/ul/li[2]/div/a').click()

def consulta():
    global linha
    tabela = pd.read_csv('clientes.csv')
    for linha in tabela.index:
    
        linha = (str(tabela.loc[linha, "nome"]))
    pyautogui.write(linha)
consulta()


def hubsoft1():
    #nome do cliente
    driver.find_element("xpath", '/html/body/div[4]/md-dialog/form/md-dialog-content/div/hubsoft-consultar-cliente/div/md-input-container[2]/md-select').click()
    pyautogui.moveTo(661, 417)
    pyautogui.scroll(-100)
    sleep(3)
    #seleciona login radius
    pyautogui.click(687, 574)
    sleep(2)
    pyautogui.click(894, 411)
    sleep(2)
    pyautogui.click(717, 530)
    sleep(2)
    pyautogui.click(717, 530)
    sleep(5)
    #pegar Ip
    pyautogui.click(575, 471)
    sleep(7)

    pyautogui.doubleClick(289, 486)
    pyautogui.hotkey('Ctrl','c')
    pyautogui.click(264, 74)
    pyautogui.hotkey('Ctrl','v')
    pyautogui.hotkey('Enter')
    sleep(5)
hubsoft1()

#entrando
def roteador():
    try:
        pyautogui.write('Blackcat@2007')
        pyautogui.hotkey('Enter')
    except:
        print('senha incorreta {}'.format(linha))
        with open("erros_senha.xlsx", "a", newline="", encoding="utf-8") as arquivo:
            arquivo.write(f"{linha}")
    sleep(2)
    pyautogui.click(569, 214)
    sleep(2)
    pyautogui.click(611, 281)
    sleep(3)
roteador()
#verificação se tem ipv6 ou não
def comparar_texto_selecionado(texto_1):
    #cria a planilha


    # Obter o texto da área de transferência
    texto_selecionado = pyperclip.paste()

    
    if texto_selecionado == texto_1:
        print(f"""Selecionado:'{texto_selecionado} tem IPv6""")  
        return True
    else:
        print(f"O texto selecionado '{texto_selecionado}' Não tem IPv6.")
        pyautogui.click(211, 371)
        sleep(1)
        pyautogui.click(140, 315)
        sleep(1)
        pyautogui.click(914, 398)
        sleep(1)
        pyautogui.click(589, 396)
        sleep(1)
        pyautogui.scroll(-2000)
        sleep(1)
        pyautogui.click(572, 312)
        sleep(1)
        pyautogui.click(579, 359)
        sleep(1)
        pyautogui.click(613, 437)
        sleep(1)
        pyautogui.click(875, 691)
        sleep(5)
        print(f"IPv6 Ativo: {linha}")
        sleep(5)
        return False
if __name__ == "__main__":

    sleep(3)
    pyautogui.tripleClick(477, 372)

    pyautogui.hotkey('Ctrl', 'c')

    # Texto pré-definido para comparação
    texto_1 = [
        "::"
    ]
    # Comparar o texto selecionado com o texto pré-definido
    comparar_texto_selecionado(texto_1)

driver.find_element('xpath', '/html/body/div[4]/md-dialog/form/md-dialog-content/div/hubsoft-consultar-cliente/div/md-input-container[1]/input').click()

pyautogui.hotkey('Ctrl', 'a')
pyautogui.hotkey('Del')
sleep(3)
pyautogui.write(linha[1])
driver.find_element('xpath', '/html/body/div[4]/md-dialog/form/md-dialog-content/div/hubsoft-consultar-cliente/div/div/button').click()
hubsoft1()
roteador()
comparar_texto_selecionado()