import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def set_up():
    """
    Set up and configure the Chrome WebDriver for automated tasks.

    Returns:
        WebDriver: The configured WebDriver instance.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                           "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

    return driver


def getRandomTime():
    """
    Generate a random time interval for waiting purposes.

    Returns:
        int: A random time interval.
    """
    return randint(3, 20)


def login(driver, username, password):
    """
    Perform the login action on Instagram.

    Args:
        driver (WebDriver): The WebDriver instance used for interacting with the webpage.
        username (str): The Instagram username.
        password (str): The Instagram password.

    Returns:
        None
    """
    # Xpaths (Update as needed)
    LOGIN_BTN_XPATH = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a'
    SUBMIT_LOGIN_FORM_XPATH = '//*[@id="loginForm"]/div/div[3]/button'
    NOT_NOW_BTN_XPATH = '//*[@id="mount_0_0_xP"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div'

    # Click the login button at the top of the (Celebrity) page
    try:
        LOGIN_BTN = driver.find_element(By.XPATH, LOGIN_BTN_XPATH)
        LOGIN_BTN.click()
    except:
        print("Login button not found.")

    # Find the username and password text fields
    USERNAME_FIELD = driver.find_element(By.NAME, 'username')
    PASSWORD_FIELD = driver.find_element(By.NAME, 'password')

    USERNAME_FIELD.send_keys(username)
    time.sleep(getRandomTime())
    PASSWORD_FIELD.send_keys(password)
    time.sleep(getRandomTime())

    # Submit the login form
    SUBMIT_LOGIN_BTN = driver.find_element(By.XPATH, SUBMIT_LOGIN_FORM_XPATH)
    SUBMIT_LOGIN_BTN.click()

    time.sleep(getRandomTime())

    # Hit 'Not Now' if the pop-up asks for it
    NOT_NOW_BTN = driver.find_element(By.CLASS_NAME, '_ac8f')
    NOT_NOW_BTN.click()


def refresh_page(driver, url):
    """
    Refresh the webpage with the given URL.

    Args:
        driver (WebDriver): The WebDriver instance used for interacting with the webpage.
        url (str): The URL to navigate to.

    Returns:
        None
    """
    driver.get(url)


# Example usage
if __name__ == "__main__":
    driver = set_up()
    # Replace with the desired URL
    refresh_page(driver, 'https://www.instagram.com/kateupton/')
    # Replace with your credentials
    login(driver, 'your_username', 'your_password')
    # Perform other actions using the driver
    driver.quit()  # Close the WebDriver when done
