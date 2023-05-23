from login import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

pagina_login = LoginPage()
pagina_login.open_website('https://sysra-h.maracanau.ifce.edu.br/login')


pagina_login.login('111222333', '@Dev12345')
                #111222333 , @Dev12345