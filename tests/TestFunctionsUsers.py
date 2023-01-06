from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

browser = webdriver.Firefox()

def testLoginWithUserRoot(rootUser, rootPassword):
  browser.get("http://localhost/mantisbt/mantisbt-2.25.4/login_page.php?cookie_error=1")
  browser.find_element(By.ID, "username").send_keys(rootUser)
  browser.find_element(By.XPATH, "//*[@id=\"login-form\"]/fieldset/input[2]").click()
  browser.find_element(By.ID, "password").send_keys(rootPassword)
 
  browser.find_element(By.XPATH, "//*[@id=\"login-form\"]/fieldset/input[3]").click()
  userBoxNameText = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/ul/li[3]/a/span").text
  if userBoxNameText == rootUser:
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

  realNameBoxText = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr/td[2]").text
  if realNameBoxText == realName:
    print("Real name changed successfully!")
    browser.close()
  else:
    print("Real name is not expected!")

  
testLoginWithUserRoot("administrator", "root")
testAddRealName("dayvid", "administrator")