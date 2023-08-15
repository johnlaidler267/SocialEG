import time

from selenium.webdriver.common.by import By

from Program_Logic.setup import getRandomTime, refresh_page


def follow_ten_accounts(driver):
    """
    Follows ten Instagram accounts from the followers list of the target account.

    Args:
        driver (WebDriver): The WebDriver instance used for interacting with the webpage.

    Returns:
        None
    """
    # Define Xpaths
    FOLLOW_BTN_XPATH = "//button[text()='Follow']"

    # Wait for a random amount of time
    time.sleep(getRandomTime())

    # Set an implicit wait for a random amount of time
    driver.implicitly_wait(getRandomTime())

    # Find the 'Follow' buttons
    ACCOUNTS_TO_FOLLOW = driver.find_elements(By.CLASS_NAME, '_acan')

    # If there are less than 10 'Follow' buttons initially, try to refresh and find again
    if len(ACCOUNTS_TO_FOLLOW) < 10:
        # This line seems incorrect. You might need to correct it based on your actual code.
        driver.wait(getRandomTime())
        ACCOUNTS_TO_FOLLOW = driver.find_elements(By.CLASS_NAME, '_acan')
        refresh_page()

    accounts_followed = 0

    # Iterate through the 'Follow' buttons and click them
    for follow_btn in ACCOUNTS_TO_FOLLOW:
        try:
            follow_btn.click()
            accounts_followed += 1
            if accounts_followed == 10:
                return
        except:
            continue

        # Wait for a random amount of time before following the next account
        time.sleep(getRandomTime())
