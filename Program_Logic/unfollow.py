from Program_Logic.setup import *

class Unfollow:
    def __init__(self, driver, username):
        self.driver = driver
        self.username = username
        
    def unfollow_not_following_back(self):
        self.driver.get("https://www.instagram.com/" + self.username + "/")
        
        time.sleep(getRandomTime())
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        followers_list = self.get_list(self.driver, followers_button)
        print(len(followers_list))
        
        self.driver.get("https://www.instagram.com/" + self.username + "/")
        
        time.sleep(getRandomTime())
        following_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
        following_list = self.get_list(self.driver, following_button)
        print(len(following_list))
        
        not_following_back = self.find_not_following_back(followers_list, following_list)
        print(len(not_following_back))
        
        self.unfollow(not_following_back)

    def get_list(self, button):
        button.click()
        list = []
        index, num_followers = 0, int(button.text)
        
        time.sleep(getRandomTime())
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        
        for x in range(0,5):
            prev_height, height = 0, 2
            while prev_height != height:
                prev_height = height
                time.sleep(getRandomTime())
                height = self.driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                    return arguments[0].scrollHeight;
                    """, scroll_box)

        while len(list) < num_followers-1:
            follower_list = self.driver.find_elements_by_xpath("//*[@class='Jv7Aj mArmR MqpiF  ']")
            list.append(follower_list[index].text)
            index += 1
        
        return list

    def find_not_following_back(followers, following):
        not_following_back = []
        for username in following:
            if username not in followers:
                not_following_back.append(username)
        return not_following_back

    def unfollow(self, not_following_back):
        usernames = self.driver.find_elements_by_xpath("//*[@class='Jv7Aj mArmR MqpiF  ']")
        unfollow_buttons = self.driver.find_elements_by_xpath("//button[text()='Following']")
        accounts = {usernames[i]: unfollow_buttons[i] for i in range(len(usernames))}
        
        for username, unfollow in accounts.items():
            if username.text in not_following_back:
                unfollow.click()
                time.sleep(getRandomTime())
                confirm = self.driver.find_element_by_xpath("//button[text()='Unfollow']")
                time.sleep(getRandomTime())
                confirm.click()     
                time.sleep(getRandomTime())   