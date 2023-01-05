from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

browser = webdriver.Firefox()

def TestLoginWithUserRoot(rootUser, rootPassword):
  browser.get("http://localhost/mantisbt/mantisbt-2.25.4/login_page.php?cookie_error=1")
  ## digitar no campo de id "username" o texto "administrator"
  browser.find_element(By.ID, "username").send_keys(rootUser)
  ## clicar no elemento de xpath "//*[@id="login-form"]/fieldset/input[2]"
  browser.find_element(By.XPATH, "//*[@id=\"login-form\"]/fieldset/input[2]").click()
  ## digitar no elemento de id "password" o texto "root"
  browser.find_element(By.ID, "password").send_keys(rootPassword)
  ## clicar no elemento de xpath "//*[@id="login-form"]/fieldset/input[3]"
  browser.find_element(By.XPATH, "//*[@id=\"login-form\"]/fieldset/input[3]").click()
  ## verificar se o nome no elmento de xpath "//*[@id="navbar-container"]/div[2]/ul/li[3]/a/span" e igual a "administrator"
  userBoxNameText = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/ul/li[3]/a/span").text
  if userBoxNameText == rootUser:
    browser.close()
  else:
    print("login user is not expected")

TestLoginWithUserRoot("administrator", "root")