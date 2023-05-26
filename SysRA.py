from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        senhahidden = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[2]/div/button')
        sleep(1)
        
        senhahidden.click()
        sleep(1)
       
        logar = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[4]/div/button')
        sleep(1)
        logar.click()

        sleep(3)

class AdmCardapio(LoginPage):
    def admcardapio(self):
        self.login('111222333', '@Dev12345') 
        adm = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[1]')
        adm.click()
        cardapio = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[1]')
        cardapio.click()
        data = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[3]/a')
        data.click()
    def cafedamanha(self, gramas):
        categoria = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]')
        categoria.click()
        sleep(1)
        alimento = self.driver.find_element(By.NAME, 'cafeDaManha.categoria')
        sleep(1)
        alimento.click()
        botao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao.click()
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        preparacaoChose = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]')
        preparacaoChose.click()
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        gramas_element.click()
        gramas_element.send_keys(gramas)


adm_cardapio = AdmCardapio()
adm_cardapio.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
adm_cardapio.admcardapio()
adm_cardapio.cafedamanha()



