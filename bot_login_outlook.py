from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

#abrir o navegador
browser.get("https://outlook.live.com/")
#informar dados para login
browser.find_element(By.XPATH,'/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
browser.find_element(By.XPATH,'//*[@id="i0116"]').send_keys("coloque_o_seu_email")
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
browser.find_element(By.XPATH,'//*[@id="i0118"]').send_keys("coloque_a_sua_senha")
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="idBtn_Back"]').click()
time.sleep(5)
#efetuar logout
browser.find_element(By.XPATH,'//*[@id="O365_MainLink_MePhoto"]/div/div/div/div/div[2]/img').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]').click()
browser.find_element(By.XPATH,'//*[@id="mectrl_body_signOut"]').click()
time.sleep(5)