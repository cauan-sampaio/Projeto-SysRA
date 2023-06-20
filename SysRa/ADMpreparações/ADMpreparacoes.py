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

class AdmPreparacoes(LoginPage):
    def admpreparacoes(self):
        self.login('20221045050443', '87489308Ca#') 

        
        adm = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]')
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
            '''            
    def preparacoesfiltro(self, nome):
         tipo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[1]/div[2]/div/div/div[1]')  
         tipo.click()

        self.pressionar_seta(None, 0, pressionar_enter=True )
        
        search = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[3]/span/span/div/div/button')
        search.click()
        ''' 
        '''
    def cadastrarpreparacao(self, nome_preparacao, fator_correcao):   
        novo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div[3]/span/a/button')
        novo.click()
        sleep(1)

        nome = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div[2]/input')
        nome.click()
        nome.send_keys(nome_preparacao)

        tipo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]')
        tipo.click()

        self.pressionar_seta('down', 3, pressionar_enter=True)

        gluten = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]')
        gluten.click()

        self.pressionar_seta(None, 0, pressionar_enter=True)    

        lactose = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[4]/div[2]/div/div/div[1]/div[2]')
        lactose.click()

        self.pressionar_seta(None, 0, pressionar_enter=True)

        ingredientes_nome = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div[2]/div/div/div[1]/div[2]')
        ingredientes_nome.click()
        sleep(1)

        self.pressionar_seta('down', 6, pressionar_enter=True)

       
        fatorcorrecao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[3]/div[2]/input')
        fatorcorrecao.click()
        fatorcorrecao.send_keys(fator_correcao)
        sleep(1)
        add = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[5]/button')
        add.click()
        sleep(1)

        save = self.driver.find_element(By.CSS_SELECTOR, 'div.sc-gXmSlM:nth-child(2) > button:nth-child(1)')
        self.driver.execute_script("arguments[0].scrollIntoView();", save )
        sleep(1)
        save.click()
        sleep(3)

        ok = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        ok.click()
        '''
    def editarpreparacao(self, nome_preparacao1, ingredientes_nome, fator_correcao1):
        body = self.driver.find_element(By.XPATH, '/html/body')
    
        sleep(2)
        edit = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/a/span/span/div/div/button')
        edit.click()
       
        nome = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div[2]/input')
        nome.click()
        nome.clear()
        nome.send_keys(nome_preparacao1)

        tipo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[2]')
        tipo.click()

        self.pressionar_seta(None, 0, pressionar_enter=True)

        gluten = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]')
        gluten.click()

        self.pressionar_seta('down', 1, pressionar_enter=True)    

        lactose = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div/div[4]/div[2]/div/div/div[1]/div[2]')
        lactose.click()

        self.pressionar_seta('down', 1, pressionar_enter=True)

        ingredientes = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[1]/div[2]/div/div/div[1]')
        ingredientes.click()
        sleep(2)
        body.send_keys(ingredientes_nome)


        sleep(1)

        self.pressionar_seta('down', 4, pressionar_enter=True)

       
        fatorcorrecao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[3]/div[2]/input')
        fatorcorrecao.click()
        fatorcorrecao.send_keys(fator_correcao1)
        sleep(1)
        add = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div[2]/form/div/div[5]/button')
        add.click()
        sleep(1)

        save = self.driver.find_element(By.CSS_SELECTOR, 'div.sc-gXmSlM:nth-child(2) > button:nth-child(1)')
        self.driver.execute_script("arguments[0].scrollIntoView();", save )
        sleep(1)
        save.click()
        sleep(3)

        ok = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        ok.click()


adm_preparacoes = AdmPreparacoes()
adm_preparacoes.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
adm_preparacoes.admpreparacoes()
#adm_preparacoes.preparacoesfiltro('co')
#adm_preparacoes.cadastrarpreparacao('vitamina de abacate12', '876')
adm_preparacoes.editarpreparacao('Filé mingnon3','Filé', '90')