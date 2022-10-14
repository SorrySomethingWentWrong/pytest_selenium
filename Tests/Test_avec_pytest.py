import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#import sys
## caution: path[0] is reserved for script path (or '' in REPL)
#sys.path.insert(1,'../Pages')
from Pages.kiwihr_login import kiwihr_login_page
@pytest.fixture() #Méthode prérequis pour l'exécution des méthodes test_* et *_test
def Setup():
     # create webdriver object
    global driver
    driver = webdriver.Chrome()
    login_page = kiwihr_login_page()
    driver.get(login_page.info['url'])  # type: ignore
    # Maximize Page
    driver.maximize_window()
    driver.implicitly_wait(6) # seconds
    elementlogin = driver.find_element(By.ID,'login')
    elementlogin.send_keys(login_page.info['login'])
    elementpassword = driver.find_element(By.ID,'password')
    elementpassword.send_keys(login_page.info['password'])
    #Pause execution until the test function ends
    yield
    driver.close()

def test_AddExepense(Setup):
    elementsubmit = driver.find_element(By.XPATH,"//button[@type='submit']")
    classname=elementsubmit.get_attribute("class")
    #print(classname)
    assert classname != "abcd"
    elementsubmit.click()
    element=driver.find_element(By.XPATH,"//span[contains(text(),'Notes de frais')]")
    element.click()
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/aside/ul/li[7]/div/div/ul/li[1]/a").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'Nouvelle note')]").click()
    driver.find_element(By.ID,'/expense/merchant').send_keys("Fournisseur2")
    driver.find_element(By.ID,'/expense/purchaseDate').send_keys("09/09/2022")
    driver.find_element(By.ID,'/expense/amount').send_keys("2000")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-icon']").click()
    driver.find_element(By.ID,'/merchant').send_keys("Fournisseur2")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

def test_AddExepense2(Setup):
    elementsubmit = driver.find_element(By.XPATH,"//button[@type='submit']")
    classname=elementsubmit.get_attribute("class")
    #print(classname)
    assert classname != "abcd"
    elementsubmit.click()
    element=driver.find_element(By.XPATH,"//span[contains(text(),'Notes de frais')]")
    element.click()
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/aside/ul/li[7]/div/div/ul/li[1]/a").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'Nouvelle note')]").click()
    driver.find_element(By.ID,'/expense/merchant').send_keys("Fournisseur2")
    driver.find_element(By.ID,'/expense/purchaseDate').send_keys("09/09/2022")
    driver.find_element(By.ID,'/expense/amount').send_keys("2000")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-icon']").click()
    driver.find_element(By.ID,'/merchant').send_keys("Fournisseur2")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

def test_AddExepense3(Setup):
    elementsubmit = driver.find_element(By.XPATH,"//button[@type='submit']")
    classname=elementsubmit.get_attribute("class")
    #print(classname)
    assert classname != "abcd"
    elementsubmit.click()
    element=driver.find_element(By.XPATH,"//span[contains(text(),'Notes de frais')]")
    element.click()
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/aside/ul/li[7]/div/div/ul/li[1]/a").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'Nouvelle note')]").click()
    driver.find_element(By.ID,'/expense/merchant').send_keys("Fournisseur2")
    driver.find_element(By.ID,'/expense/purchaseDate').send_keys("09/09/2022")
    driver.find_element(By.ID,'/expense/amount').send_keys("2000")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-icon']").click()
    driver.find_element(By.ID,'/merchant').send_keys("Fournisseur2")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
