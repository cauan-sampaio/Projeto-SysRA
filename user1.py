from SysRA import LoginPage
from SysRA import AdmCardapio
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

pagina_login = LoginPage()
pagina_login.open_website('https://sysra-h.maracanau.ifce.edu.br/login')
pagina_login.login('111222333', '@Dev12345')
# 111222333 , @Dev12345

adm_cardapio = AdmCardapio()
adm_cardapio.admcardapio()




