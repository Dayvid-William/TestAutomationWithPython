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


def testCreateUser(newUser, passwordNewUser, email, realName):
  browser.find_element(By.XPATH, "//*[@id=\"sidebar\"]/ul/li[6]/a/span").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[1]/div/div[1]/a").click()

  
  browser.find_element(By.ID, "user-username").send_keys(newUser)
  browser.find_element(By.ID, "user-realname").send_keys(realName)
  browser.find_element(By.ID, "email-field").send_keys(email)
  browser.find_element(By.XPATH, "//*[@id=\"user-access-level\"]").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div/div/table/tbody/tr[4]/td[2]/select/option[4]").click()

  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[3]/input").click()
  time.sleep(60)
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/ul/li[2]/a").click()
  time.sleep(10)


  newUserTextBox = browser.find_element(By.LINK_TEXT, newUser).text
  if newUserTextBox == newUser:
    print("new user successfully created!")
  else:
    print("new user is not expected!")


def testAddRealName(realName, user):
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


def testChangeAccessLevel(user):
  browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/ul/li[6]/a/i").click()
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  browser.find_element(By.LINK_TEXT, user).click()

  browser.find_element(By.ID, "edit-access-level").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div/div/table/tbody/tr[4]/td[2]/select/option[4]").click()
  browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div[2]/input").click()
  
  time.sleep(120)
  browser.find_element(By.LINK_TEXT, "Gerenciar Usuários").click()
  time.sleep(10)
  
  accessLevelTextBox = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody/tr[2]/td[4]").text
  if accessLevelTextBox == "desenvolvedor":
    print("Access level changed successfully!")
  else:
    print("Acess level is not expected!")


testLoginWithUserRoot("administrator", "root")
#testCreateUser("Thiago12", "12345", "thiago@email.com", "Thiago")
#testChangeAccessLevel("Thiago12")
#testAddRealName("dayvid", "Dayvid")
#testSwitchEmail("email@email.com")