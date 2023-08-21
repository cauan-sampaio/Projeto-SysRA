
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

class AdmUsuarios(LoginPage):
    def admusuarios(self):
        self.login('20221045050443', '87489308Ca#') 

        
        adm = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]')
        adm.click()
        sleep(3)

        user = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/ul/li[5]/div[2]/a[4]')
        user.click()
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
    def adicionarusers(self, nome_element, nomesocial_element, email_element, telefone_element, cartao_element, indentificacao_element):
        novo = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div[3]/span/a/div/button')
        novo.click()
        sleep(2)
        wait = WebDriverWait(self.driver, 2)

        nome =/html/body/div/div[1]/div/div[1]/div[3]/span/div/button self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/input')
        nome.click()
        nome.send_keys(nome_element)
        sleep(1)

        nomesocial = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[2]/input')
        nomesocial.click()
        nomesocial.send_keys(nomesocial_element)
        sleep(1)

        email = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[3]/div[2]/input')
        email.click()
        email.send_keys(email_element)
        sleep(1)

        telefone = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[5]/div[2]/input')
        telefone.click()
        telefone.send_keys(telefone_element)

        cartao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[6]/div[2]/input')
        cartao.click()
        cartao.send_keys(cartao_element)
       
        cpf = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[1]/div[2]/div[1]/div[2]/div/div[4]/div[2]/input')
        cpf.click()
        cpf.send_keys(cpf_element)
    
        novo_cadastro = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div/div/div[2]/div/button')
        novo_cadastro.click()
        sleep(2)
       
        tipo = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[1]/div[2]/div/div/div[1]')))
        tipo.click()
        sleep(1)
        

        self.pressionar_seta(None, 0, pressionar_enter=True)
        
        indentificacao = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div[2]/input')
        indentificacao.click()
        indentificacao.send_keys(indentificacao_element)
           
        situacao = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[3]/div[2]/div/div/div[1]/div[2]')))
        situacao.click()

        self.pressionar_seta(None, 0, pressionar_enter=True)
        
        grupo_acesso = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[1]/div[2]/div/div[1]')
        grupo_acesso.click()
        sleep(2)

        self.pressionar_seta(None, 0, pressionar_enter=True)
        
        curso = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[1]/div[2]')))
        curso.click()
        sleep(2)

        self.pressionar_seta(None, 0, pressionar_enter=True)
        
        salvar_indentificação = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div[2]/button')
        salvar_indentificação.click()


        salvar_perfil = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[3]/div/button')
        body = self.driver.find_element(By.XPATH, '/html/body')
        body.send_keys(Keys.PAGE_DOWN)
        sleep(1)
        salvar_perfil.click()
        sleep(3)

        ok = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        ok.click()
    '''

    def editarusuarios(self, nome_element):
        body = self.driver.find_element(By.XPATH, '/html/body')
        filtros = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[1]/div[2]/div/div')
        filtros.click()
        sleep(1)

        self.pressionar_seta(None, 0, pressionar_enter=True)

        descricao = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[2]/div/div[2]/input')
        descricao.click()
        descricao.send_keys(nome_element)

        search = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[1]/form/div/div[3]/span/span/div/div/button')
        search.click()
        sleep(3)

        editar = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/a/span/span/div/div/button')
        editar.click()
        sleep(2)

        body.send_keys(Keys.PAGE_DOWN)
        sleep(2)

        editariden = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[5]/span/span/div/div/button')
        editariden.click()
        sleep(2)

        tipo_aluno = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[1]/div[2]/div/div/div[1]/div[2]')
        tipo_aluno.click()
        sleep(2)

        self.pressionar_seta('down', 1, pressionar_enter=True)
     
        curso = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div[1]/div[2]')
        curso.click()
        sleep(2)

        self.pressionar_seta(None, 0, pressionar_enter=True)

        salvariden = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div[2]/button')
        salvariden.click()

        body.send_keys(Keys.PAGE_DOWN)
        sleep(1)

        salvarperfil = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/form/div[3]/div/button')
        salvarperfil.click()
        sleep(2)

        useratu = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        useratu.click()

        body.send_keys(Keys.PAGE_UP)
        sleep(1)

        voltar = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div[3]/span/a/div/button')
        voltar.click()

adm_usuarios = AdmUsuarios()
adm_usuarios.open_website('https://sysra-h.maracanau.ifce.edu.br/login') 
adm_usuarios.admusuarios()    
#adm_usuarios.adicionarusers('Hans1', 'Vocalista do Blind Guardian', 'cauansampaio240@gmail.com', '85982309576', '023898', '203456')  
adm_usuarios.editarusuarios('hans')