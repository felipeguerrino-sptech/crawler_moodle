from time import sleep

import os
import getpass
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    os.system("sh verify-selenium.sh")
    with open('./log.txt', 'r') as f:
        if f.read() == "False\n":
            print("Webdriver não encontrado...")
            print("Instalando webdriver...")
            install_webdriver()
        else:
            ra = input('Insira o RA: ')
            senha = getpass.getpass(prompt='Insira a senha: ')
            get_github_token(ra, senha)
    

def get_github_token(ra, senha):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_experimental_option('prefs', {'download.default_directory': '/home/aluno/temp'})

    driver = webdriver.Chrome(options=options)
    driver.get("https://moodle.sptech.school/")
    
    username = driver.find_element(By.ID, 'username')
    username.send_keys(ra)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(senha)
    driver.find_element(By.ID, 'loginbtn').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'icon').click() 
    driver.find_element(By.XPATH, '//a[@href="https://moodle.sptech.school/user/files.php"]').click()    
    assert 'Arquivos privados' in driver.title
    sleep(5)
    driver.find_element(By.XPATH, "//div[text()='github.txt']").click()
    driver.find_element(By.CLASS_NAME, 'fp-file-download').click()
    sleep(2)
    driver.close()

def install_webdriver():
    wget.download('https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip')
    os.system('unzip ./chromedriver_linux64.zip')
if __name__ == '__main__':
    main()