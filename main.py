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
    
    follow_total = 0
    while follow_total < 1000:
        
        follow_hour, elapsed_time, start_time = 0, 0, time.time()
        
        while elapsed_time < 3600:
            
            #sets a limit of 100 followers
            if(follow_hour > 100):
                while elapsed_time < 3600:
                    elapsed_time = time.time() - start_time
                break
            
            time.sleep(getRandomTime())
            
            follow_ten_accounts(driver)
            follow_hour += 10
            follow_total += 10
            
            driver.get('https://www.instagram.com/' + famous_person_account + '/')
            
            elapsed_time = time.time() - start_time
    
    #unfollow = Unfollow()
    #unfollow.unfollow_not_following_back()

main()