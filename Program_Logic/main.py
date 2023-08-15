import time
from Program_Logic.follow import follow_ten_accounts
from Program_Logic.unfollow import Unfollow
from Program_Logic.setup import set_up, login, getRandomTime


def control(username, password, famous_person_account):

    # Print input for verification
    print('Inside main.py')
    print('Username:', username)
    print('Password:', password)
    print('Famous Person Account:', famous_person_account)

    # Set up the WebDriver
    driver = set_up()

    # Open the Instagram account of the famous person
    driver.get('https://www.instagram.com/' +
               famous_person_account + '/followers')

    # Log in using provided credentials
    login(driver, username, password)

    print('Login successful')

    follow_total = 0
    ONE_HOUR = 3600
    HOURLY_LIMIT = 100
    TARGET_FOLLOWER_COUNT = 1000

    # Loop until 1000 followers have been added
    while follow_total < TARGET_FOLLOWER_COUNT:
        follow_current_hour, elapsed_time, start_time = 0, 0, time.time()

        # Loop for one hour
        while elapsed_time < ONE_HOUR:
            # Check if the hourly follow limit (100) has been reached
            if follow_current_hour > HOURLY_LIMIT:
                # Wait for the remaining time in the hour
                while elapsed_time < ONE_HOUR:
                    elapsed_time = time.time() - start_time
                break

            # Sleep for a random time before following accounts
            time.sleep(getRandomTime())

            # Follow ten accounts
            follow_ten_accounts(driver)
            follow_current_hour += 10
            follow_total += 10

            # Refresh the famous person's account page (to get new accounts)
            driver.get('https://www.instagram.com/' +
                       famous_person_account + '/')

            # Calculate elapsed time
            elapsed_time = time.time() - start_time

    # Uncomment the following lines to enable unfollowing
    # unfollow = Unfollow()
    # unfollow.unfollow_not_following_back()


# Entry point of the program
if __name__ == "__main__":
    main()
