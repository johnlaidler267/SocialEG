# Import tkinter and ttk modules
from tkinter import font, ttk
import tkinter as tk

# * == Import GUI pages ================================================
from login import Login
from landing import Landing
from select_mode import SelectMode
from settings import Settings
from header import Header

# -- Social Interaction Dashboards --------------------------------

# Follow-Only Mode
from following import Following

# Unfollow-Only Mode
from unfollowing import Unfollowing

# Automatic Mode
from automatic_following import AutomaticFollowing
from automatic_unfollowing import AutomaticUnfollowing

# Job Completed (Applies to all dashboard pages)
from finished import Finished

# ----------------------------------------------------------------

# * ======================================================================

# Import sys for accessing the system path
import sys

sys.path.append("/Users/johnnylaidler/SocialEG/")

print("HERES THE SYSTEM PATH BUDYD")
print(sys.path)


class GUI(tk.Tk):
    def __init__(self):
        # Initialize the base class of your GUI class, which is tk.Tk
        super().__init__()

        # GUI window setup
        self.title("Instagram Engagement Bot")
        self.geometry("500x500")

        # Create a container to hold the pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # I need to set the style to default so that later custom styles will apply. (Not sure why)
        mystyle = ttk.Style()
        mystyle.theme_use("default")

        # Create instances of the GUI pages
        self.login = Login(self.container, self)
        self.landing = Landing(self.container, self)
        self.select_mode = SelectMode(self.container, self)
        self.following = Following(self.container, self)
        self.finished = Finished(self.container, self)
        self.settings = Settings(self.container, self)
        self.unfollowing = Unfollowing(self.container, self)
        self.automatic_following = AutomaticFollowing(self.container, self)
        self.automatic_unfollowing = AutomaticUnfollowing(self.container, self)
        self.header = Header(self.container, self)

        # Show the first page by default
        self.automatic_unfollowing.show()


app = GUI()
app.mainloop()
