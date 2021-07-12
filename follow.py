from setup import *
        
def follow_ten_accounts(driver) :
    followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers.click()

    time.sleep(getRandomTime())

    driver.implicitly_wait(getRandomTime())
        
    follow = driver.find_elements_by_xpath("//button[text()='Follow']")
    
    if len(follow) < 10:
        driver.wait(getRandomTime())
        follow = driver.find_elements_by_xpath("//button[text()='Follow']")
        refresh_page()
        
    count = 0
    
    for btn in follow:
        try:
            btn.click()
            
            count += 1
            if count == 10:
                return
        except:
            continue
        
        time.sleep(getRandomTime())