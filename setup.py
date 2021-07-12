from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from random import randint
from selenium.webdriver.common.keys import Keys

def set_up() :
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    print(driver.execute_script("return navigator.userAgent;"))
    
    return driver

def getRandomTime():
        randTime = randint(3, 60)
        return randTime

# log in
def login(driver, username, password):
    try:
        login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
        login_button.click()
    except:
        print('');

    username_textfield = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    password_textfield = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            

    username_textfield.send_keys(username)
    time.sleep(getRandomTime())
    password_textfield.send_keys(password)
    time.sleep(getRandomTime())
    
    submit = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button/div')
    submit.click()
    
    time.sleep(getRandomTime())
    
    try:
        not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
    except:
        return

def refresh_page(driver) :
    driver.get('https://www.instagram.com/kateupton/')