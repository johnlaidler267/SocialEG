from gui import Gui
from follow import *
from unfollow import Unfollow
from setup import *
       
def main() :
    gui = Gui()
    username, password, famous_person_account = gui.main_menu()
    
    driver = set_up() 
    driver.get('https://www.instagram.com/' + famous_person_account + '/')
    
    login(driver, username, password)
    
    for x in range(0,200):
        time.sleep(getRandomTime())
        follow_ten_accounts(driver)
        driver.get('https://www.instagram.com/' + famous_person_account + '/')
    
    unfollow = Unfollow()
    unfollow.unfollow_not_following_back()

main()