from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from json import loads
from behave import given, when, then

class Page:
    @given('O usuário entra na página de login')
    def go_to_page(context):
        context.browser = webdriver.Firefox()
        context.browser.get('https://sysra-h.maracanau.ifce.edu.br/login')

class LoginPage(Page):
    @when('O usuário digitar os seus dados de login')
    def login(context):
        sleep(1)
        texto_do_step = loads(context.text)
        name_element = context.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[1]/div/input')  
        name_element.click()
        sleep(1)
        name_element.send_keys(texto_do_step['matricula'])   
        sleep(1)
     
        senha_element = context.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[2]/div/input')
        senha_element.click()
        sleep(1)
        senha_element.send_keys(texto_do_step['senha'])
        
        logar = context.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[4]/div/button')
        sleep(1)
        logar.click()
        sleep(5)

class AdmCursos(LoginPage):
    @then('O usuário entrará na página inicial e irá clicar em ADM, e depois em cursos')
    def admcursos(context):
        #self.login('20221045050443', '87489308Ca#')

        adm = context.browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]')
        adm.click()
        sleep(2)

        curso = context.browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[5]')
        curso.click()
        sleep(2)
class CriarCurso(AdmCursos):
        def pressionar_seta(context, direction, num_teclas, pressionar_enter=False):
            escolher = context.browser.find_element(By.XPATH, '/html/body')
            keys = {
            'up': Keys.ARROW_UP,
            'down': Keys.ARROW_DOWN
            }

            if num_teclas > 0:
                for _ in range(num_teclas):
                    escolher.send_keys(keys[direction])
                sleep(1)
            if (pressionar_enter==True):
                escolher.send_keys(Keys.ENTER)
            sleep(1)
        
        def criarcurso(context):
            novo = context.browser.find_element(By.XPATH, '')