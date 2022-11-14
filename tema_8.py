'''
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app


Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
'''


from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chrome = webdriver.Chrome()
chrome.get("https://phptravels.net")
chrome.find_element(By.ID, "currency").click()
chrome.find_element(By.ID, "languages").click()
chrome.find_element(By.ID, "ACCOUNT").click()
sleep(5)
chrome.quit()

'-------------------------------------------------------------'


chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com")
chrome.find_element(By.LINK_TEXT, "Buttons").click()
chrome.find_element(By.LINK_TEXT, "Form").click()
chrome.find_element(By.ID, "logo").click()
chrome.find_element(By.LINK_TEXT, "Key and Mouse Press").click()
sleep(5)
chrome.quit()

'________________________________________________________'


chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com")
chrome.find_element(By.PARTIAL_LINK_TEXT, "File D").click()
chrome.back()
chrome.find_element(By.PARTIAL_LINK_TEXT, "Key").click()
chrome.find_element(By.PARTIAL_LINK_TEXT, "Element").click()
sleep(5)
chrome.quit()


'__________________________________________________________'


chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID,'ez-accept-all').click()
chrome.find_element(By.NAME, "firstname").send_keys("Cristi")
chrome.find_element(By.NAME, "lastname").send_keys("Popescu")
chrome.find_element(By.NAME, "continents").click()
sleep(5)
chrome.quit()

'___________________________________________________________'

chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID,'ez-accept-all').click()
keyboard_list = chrome.find_elements(By.TAG_NAME, "input")
keyboard_list[0].send_keys("Gabi")
keyboard_list[1].send_keys("Coman")
keyboard_list[11].send_keys("12.11.2022")
sleep(5)
chrome.quit()

'----------------------------------------------------------------'


chrome = webdriver.Chrome()
chrome.get("https://phptravels.net/signup")
keyboard_class = chrome.find_elements(By.CLASS_NAME, "form-control")
keyboard_class[0].send_keys("Costel")
keyboard_class[1].send_keys("Andrei")
keyboard_class[2].send_keys("353546666545")
keyboard_class[3].send_keys("tns@gmail.com")
sleep(5)
chrome.quit()

'-----------------------------------------------------------------'


chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://phptravels.net/")
chrome.find_element(By.CSS_SELECTOR, "#checkin").click()
chrome.find_element(By.CSS_SELECTOR, ".checkout").click()
chrome.find_element(By.CSS_SELECTOR, "input[placeholder*='your email']").send_keys("office@romania.ro")
sleep(5)
chrome.quit()


'----------------------------------------------'

chrome.get("https://formy-project.herokuapp.com/buttons")
chrome.find_element(By.XPATH, "//button[contains(text(), 'Primary')]").click()
chrome.find_element(By.XPATH, "//button[contains(text(), 'Success')]").click()
chrome.find_element(By.XPATH, "//button[contains(text(), 'Info')]").click()
chrome.find_element(By.XPATH, "//button[contains(text(), 'War')]").click()
sleep(5)
chrome.quit()

'--------------------------------------------------------'

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/autocomplete")

chrome.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("tns@gmail.com")
chrome.find_element(By.XPATH, "//input[@id='locality']").send_keys("Suceava")
chrome.find_element(By.XPATH, "//input[@id='administrative_area_level_1']").send_keys("Romania")
sleep(3)
chrome.get("https://formy-project.herokuapp.com/buttons")
chrome.find_element(By.XPATH, "//button[contains(text(), 'Primary')]").click()
sleep(1)
chrome.find_element(By.XPATH, "//button[contains(text(), 'Success')]").click()
sleep(1)
chrome.find_element(By.XPATH, "//button[contains(text(), 'Info')]").click()
sleep(1)
chrome.find_element(By.XPATH, "//button[contains(text(), 'War')]").click()
sleep(1)
chrome.find_element(By.XPATH, "//button[contains(text(), 'NuExista1')] | //button[contains(text(), 'Middle')] | //button[contains(text(), 'NuExista2')]").click()
sleep(1)
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.XPATH, "//*[@id='job-title']").send_keys("Automation")
sleep(1)
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[4]').click()
sleep(1)
parent_text = chrome.find_element(By.XPATH,"//label[contains(text(), 'First name')]/parent::strong").text
print(parent_text)
sleep(1)
chrome.find_element(By.XPATH,"//label[contains(text(), 'First name')]/parent::strong/following-sibling::input").send_keys("STEFAN")
sleep(1)
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID,'ez-accept-all').click()
def checkbox(name,input_id):
    chrome.find_element(By.XPATH, f"//input[@name='{name}']")
    chrome.find_element(By.XPATH, f"//input[@id='{input_id}']").click()

checkbox("profession","profession-1")
checkbox("tool","tool-2")
sleep(10)
chrome.quit()
