from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

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

def testAddRealName(realName, rootUser):
  realNamey = "jenni"
  browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[6]/a/span").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr/td[1]/a").click()
  
  browser.find_element(By.ID, "edit-realname").clear()
  browser.find_element(By.ID, "edit-realname").send_keys(realName)
  browser.find_element(By.XPATH, "//*[@id=\"edit-user-form\"]/div/div[2]/div[2]/input").click()

  browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[6]/a/span").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()

  realNameTextBox = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr/td[2]").text
  if realNameTextBox == realName:
    print("Real name changed successfully!")
    browser.close()
  else:
    print("Real name is not expected!")

def testSwitchEmail(email):
  browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[6]/a/span").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  browser.find_element(By.XPATH, "//*[@id=\"main-container\"]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr/td[1]/a").click()
  
  browser.find_element(By.ID, "email-field").clear()
  browser.find_element(By.ID, "email-field").send_keys(email)
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div[2]/input").click()

  browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[6]/a/span").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  
  emailTextBox = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr/td[3]").text
  if emailTextBox == email:
    print("Email changed successfully!")
  else:
    print("Email is not expected!")

def testChangeAccessLevel():
  browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/ul/li[6]/a/i").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr/td[1]/a").click()

  browser.find_element(By.ID, "edit-access-level").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div/div/table/tbody/tr[4]/td[2]/select/option[5]").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div[2]/input").click()

  

testLoginWithUserRoot("administrator", "root")
testChangeAccessLevel()
#testAddRealName("dayvid", "administrator")
#testSwitchEmail("email@email.com")