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
        sleep(5)

class AdmIngredientes(LoginPage):
    def admingredientes(self):
        self.login('20221045050443', '87489308Ca#') 

        
        adm = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]')
        adm.click()
        sleep(3)

        ingredientes = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[3]')
        ingredientes.click()
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
    def search_ingredientes(self, nome_element, proteinas_element, carboidratos_element, lipideos_element, energia_element, retinol_element, vitaminac_element, sodio_element):
        novo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div[3]/span/div/button')
        novo.click() 
        nome = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div/div[2]/input')
        nome.click()
        nome.send_keys(nome_element)

        proteinas = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[1]/div[2]/input')
        proteinas.click()
        proteinas.send_keys(proteinas_element)
        
        carboidratos = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/div[2]/input')
        carboidratos.click()
        carboidratos.send_keys(carboidratos_element)

        lipideos = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[3]/div[2]/input')
        lipideos.click()
        lipideos.send_keys(lipideos_element)

        energia = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div[1]/div[2]/input')
        energia.click()
        energia.send_keys(energia_element)

        ferro = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div[3]/div[2]/input')

        retinol = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div[3]/div[2]/input')
        retinol.clcik()
        retinol.send_keys(retinol_element)

        vitaminac =self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[4]/div[2]/div[2]/input')
        vitaminac.click()
        vitaminac.send_keys(vitaminac_element)

        sodio = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[4]/div[3]/div[2]/input')
        sodio.click()
        sodio.send_keys(sodio_element)

            
adm_ingredientes = AdmIngredientes()
adm_ingredientes.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
adm_ingredientes.admingredientes()            