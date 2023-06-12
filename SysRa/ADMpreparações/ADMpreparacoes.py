from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep


class Page:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def open_website(self, url):
        self.driver.get(url)

class LoginPage(Page):
    def login(self, name, senha):
        sleep(1)
        
        name_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[1]/div/input')  
        name_element.click()
        sleep(1)
        name_element.send_keys(name)   
        sleep(1)
        
        senha_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[2]/div/input')
        senha_element.click()
        sleep(1)
        senha_element.send_keys(senha)
        
        logar = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[4]/div/button')
        sleep(1)
        logar.click()
        sleep(1)

class AdmPreparacoes(LoginPage):
    def admcardapio(self):
        self.login('111222333', '@Dev12345') 
        
        adm = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[1]')
        adm.click()
        sleep(3)

        preparacoes = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[2]')
        preparacoes.click()
        sleep(1)
    def pressionar_seta(self, direction, num_teclas, pressionar_enter=False):
        escolher = self.driver.find_element(By.XPATH, '/html/body')
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
    def preparacoesfiltro(self, nome):
        tipo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[1]/div[2]/div/div/div[1]')
        tipo.click()

        self.pressionar_seta(None, 0, pressionar_enter=True )
        sleep(1)

        descricao_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
        descricao_element.click()
        descricao_element.send_keys(nome)
        sleep(1)

        search = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[3]/span/span/div/div/button')
        search.click()


adm_preparacoes = AdmPreparacoes()
adm_preparacoes.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
adm_preparacoes.preparacoesfiltro('co')