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
        
        name_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[1]/div/inp7ut')  
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
        sleep(1)
        cardapio = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[1]')
        cardapio.click()
        sleep(1)
        
        data = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div/div/div/div[2]/div[6]/div[1]/div[2]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", data )
        sleep(1)
        data.click()

    def navbar(self, tab_name):    
        navbar = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul')
        if tab_name == 'lanche_manha':
            navbar_select = navbar.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul/li[2]')
            navbar_select.click()
        
        elif tab_name == 'almoco':
            navbar_select = navbar.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul/li[3]')
            navbar_select.click()
        
        elif tab_name == 'lanche_tarde':
            navbar_select = navbar.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul/li[4]')
            navbar_select.click()    
       
        elif tab_name == 'lanche_noite':
            navbar_select = navbar.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul/li[5]')
            navbar_select.click()
        
        elif tab_name == 'janta':
            navbar_select = navbar.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div/ul/li[6]')
            navbar_select.click() 
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
    
    def cafedamanha(self, gramas):
        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div')
        categorias.click()
        sleep(1)
    
        self.pressionar_seta(None, 0, pressionar_enter=True)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        sleep(2)
    
        self.pressionar_seta(None, 0, pressionar_enter=True)
    
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()
   
    def lanchedamanha(self, gramas):
        self.navbar('lanche_manha')

        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]')
        categorias.click()
        sleep(1)
        
        self.pressionar_seta(None, 0, pressionar_enter=True)
        sleep(1)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        sleep(2)
    
        self.pressionar_seta(None, 0, pressionar_enter=True)
    
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()
    
    def almoco(self, gramas):
        self.navbar('almoco')

        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]')
        categorias.click()
        sleep(1)
        
        self.pressionar_seta('down', 2, pressionar_enter=True)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        sleep(2)

        self.pressionar_seta(None, 0, pressionar_enter=True)
    
        
    
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()
    def lanchedatarde(self, gramas):
        self.navbar('lanche_tarde')

        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]')
        categorias.click()
        sleep(1)
        
        self.pressionar_seta('down', 2, pressionar_enter=True)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        sleep(2)
    
        self.pressionar_seta(None, 0, pressionar_enter=True)

    
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()
    def lanchedanoite(self, gramas):
        self.navbar('lanche_noite')

        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]')
        categorias.click()
        sleep(1)
        
        self.pressionar_seta('down', 2, pressionar_enter=True)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        sleep(2)
    
        self.pressionar_seta(None, 0, pressionar_enter=True)    
        
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()

    def janta(self, gramas):
        self.navbar('janta')

        categorias = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]')
        categorias.click()
        sleep(1)
        
        self.pressionar_seta('down', 2, pressionar_enter=True)

        botao_categoria = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div/div[2]/span/span/div/div/button')
        botao_categoria.click()
    
        preparacao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]')
        preparacao.click()
        sleep(2)
    
        self.pressionar_seta(None, 0, pressionar_enter=True)
    
        gramas_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/div[2]/input')
        
        gramas_element.send_keys(gramas)
        sleep(1)
        
        grama_button = gramas_element.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[2]/div/div[2]/span/span/div/div/button')
        sleep(3)
        grama_button.click()  
        sleep(3)
    def confirmar(self):
        avancar = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[3]/div/div/button')      
        avancar.click()
        confirm = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div/div[2]/div[2]/button')
        confirm.click()
adm_cardapio = AdmCardapio()
adm_cardapio.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
adm_cardapio.admcardapio()    
adm_cardapio.cafedamanha('10')
adm_cardapio.lanchedamanha('10')
adm_cardapio.almoco('10')
adm_cardapio.lanchedatarde('10')
adm_cardapio.lanchedanoite('10')
adm_cardapio.janta('10')
adm_cardapio.confirmar()



