from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Firefox()

def testLoginWithUserRoot(rootUser, rootPassword):
  browser.get("http://localhost/mantisbt/mantisbt-2.25.4/login_page.php?cookie_error=1")
  browser.maximize_window()
  browser.find_element(By.ID, "username").send_keys(rootUser)
  browser.find_element(By.XPATH, "//*[@id=\"login-form\"]/fieldset/input[2]").click()
  browser.find_element(By.ID, "password").send_keys(rootPassword)
 
  browser.find_element(By.XPATH, "//*[@id=\"login-form\"]/fieldset/input[3]").click()
  userNameTextBox = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/ul/li[3]/a/span").text
  if userNameTextBox == rootUser:
    print("Successful login!")
  else:
    print("Login user is not expected!")


def testCreateNewProfile(Plat, os, osb, description):
  browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[6]/a").click()
  
  ##clicar no elmento de link text "Gerenciar Perfís Globais"
  browser.find_element(By.LINK_TEXT, "Gerenciar Perfís Globais").click()
  ##digitar no elmento de id "platform" o texto do parametro "plat"
  browser.find_element(By.ID, "platform").send_keys(Plat)
  ##digitar no elemento de id "os" o texto do parametro "os"
  browser.find_element(By.ID, "os").send_keys(os)
  ##ditar no campo de id "os_build" o texto do parametro "osb"
  browser.find_element(By.ID, "os_build").send_keys(osb)
  ##digitar no campo de id "description" o texto do parametro "description"
  browser.find_element(By.ID, "description").send_keys(description)
  ## clicar no elemnto de xpath "//*[@id="account-profile-form"]/fieldset/div/div[3]/button"
  browser.find_element(By.XPATH, "//*[@id=\"account-profile-form\"]/fieldset/div/div[3]/button").click()
  ##verificar se o perfil foi adicionado
  time.sleep(3)
  perfilTextBox = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]").text
  
  if perfilTextBox == Plat:
    print("Profile create successful !")
  else:
    print("Profile was not created !")
  
  

testLoginWithUserRoot("administrator", "root")
testCreateNewProfile("python", "linux", "10.32", "Profile for tests")