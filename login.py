from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage:

    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def open_website(self, url):
        self.driver.get(url)

    def login(self, name, senha):
        sleep(3)
        name_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[1]/div/input')  
        name_element.click()
        sleep(3)
        name_element.send_keys(name)   
        
        sleep(3)
        senha_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[2]/div/input')
 
        senha_element.click()
        sleep(3)
        senha_element.send_keys(senha)
        logar = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[3]/form/div[4]/div/button')
        sleep(1)
        logar.click()

sleep(3)