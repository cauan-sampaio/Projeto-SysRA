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

class AdmCardapio(LoginPage):
    def admcardapio(self):
        self.login('111222333', '@Dev12345') 
        
        adm = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[1]')
        adm.click()
        
        cardapio = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[1]')
        cardapio.click()
        sleep(1)
        
        data = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[5]/div[1]/div[2]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", data )
        sleep(1)
        data.click()

    def navbar(self, tab_name):    
        navbar = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul')
        if tab_name == 'lanche_manha':
            navbar_select = navbar.find_element(By.XPATH, '//*[@id="react-aria9209103524-2-tab-lancheDaManha"]')
            navbar_select.click()
        
        elif tab_name == 'almoco':
            navbar_select = navbar.find_element(By.XPATH, '//*[@id="react-aria9209103524-2-tab-almoco"]')
            navbar_select.click()
        
        elif tab_name == 'lanche_tarde':
            navbar_select = navbar.find_element(By.XPATH, '//*[@id="react-aria9209103524-2-tab-lancheDaTarde"]')
            navbar_select.click()    
       
        elif tab_name == 'lanche_noite':
            navbar_select = navbar.find_element(By.XPATH, '//*[@id="react-aria9209103524-2-tab-lancheDaNoite"]')
            navbar_select.click()
        
        elif tab_name == 'janta':
            navbar_select = navbar.find_element(By.XPATH, '//*[@id="react-aria9209103524-2-tab-janta"]')
            navbar_select.click() 
    
    def cafedamanha(self, gramas):
        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div')
        categorias.click()
        sleep(1)
        
        categorias_select = categorias.find_element(By.XPATH, '/html/body')
        sleep(1)
        categorias_select.send_keys(Keys.ENTER)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
    
        preparacaoChose = self.driver.find_element(By.XPATH, '/html/body')
        sleep(1)
        preparacaoChose.send_keys(Keys.ENTER)
    
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()
   
    def lanchedamanha(self):
        self.navbar('lanche_manha')


adm_cardapio = AdmCardapio()
adm_cardapio.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
adm_cardapio.admcardapio()    
adm_cardapio.cafedamanha('10')
adm_cardapio.lanchedamanha




