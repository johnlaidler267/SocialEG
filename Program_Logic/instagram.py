import instaloader

def get_profile_info(username, password):
    # Create an Instaloader instance
    L = instaloader.Instaloader()

    try:
        # Login to Instagram account
        L.context.log("Logging in as %s..." % username)
        L.load_session_from_file(username)
        if not L.context.is_logged_in:
            L.context.log("Session file does not exist yet - Logging in.")
            L.context.log("Session file does not exist yet - Logging in.")
            L.interactive_login(username)  # Interactive login
            L.save_session_to_file()

        # Load profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Retrieve profile picture URL
        profile_picture_url = profile.profile_pic_url
        print("Profile Picture URL:", profile_picture_url)

        # Retrieve follower count
        follower_count = profile.followers
        print("Follower Count:", follower_count)

        # Retrieve following count
        following_count = profile.followees
        print("Following Count:", following_count)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    username = "your_instagram_username"
    password = "your_instagram_password"
    get_profile_info(username, password)
Please replace "your_instagram_username" and "your_instagram_password" with the actual username and password of the Instagram account you want to retrieve information for.

Please note that using the Instagram API directly with username and password is not recommended due to security concerns. It's better to use official API tokens and follow Instagram's guidelines for authentication. However, for educational purposes, this script should work for your request.





