import tkinter as tk
from tkinter import font, ttk
import customtkinter

from login import Login

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Configure grid
        self.grid_columnconfigure(0, weight=1)  # Assuming column 0 should expand
        self.grid_rowconfigure(0, weight=1)

        # Styling
        style = ttk.Style()
        style.configure(
            "Setting.Header.Label", foreground="black", background="lightgray"
        )
        style.configure("Setting.Divider.Label", foreground="white", background="gray")

        # set up the data display for the landing page
        self.init_settings_display()

        # set up the button to commence the action (following, Finished) process
        self.save_settings_btn()

    def init_settings_display(self):
        settings_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Bot Settings"
        )
        settings_frame.grid(
            row=1, column=0, padx=1, pady=1, sticky="nsew", columnspan=3
        )
        settings_frame.configure(width=500, height=300)
        settings_frame.grid_rowconfigure(0, weight=1)
        settings_frame.grid_columnconfigure(0, weight=1)

        ################################################################

        preserve_accounts_label = ttk.Label(
            settings_frame,
            text="Preserve Accounts",
            font=("Helvetica", 17, "bold"),
            style="Setting.Header.Label",
        )
        preserve_accounts_label.grid(row=3, column=0, padx=1, pady=10)

        preserve_accounts_desc = ttk.Label(
            settings_frame,
            text="These will not be unfollowed.",
            font=("Helvetica", 12),
        )
        preserve_accounts_desc.grid(row=4, column=0, padx=1, pady=1)

        # --------------------BTNS---------------------------------------------------

        # Btns for adding new users/viewing preserved accounts
        username_add_btn = customtkinter.CTkButton(
            settings_frame, text="Add Username", command=self.open_input_dialog_event
        )
        username_add_btn.grid(row=3, column=1, padx=10, pady=5, sticky="ewn")

        view_preserved_accounts_btn = customtkinter.CTkButton(
            settings_frame, text="View Accounts", command=self.open_input_dialog_event
        )
        view_preserved_accounts_btn.grid(row=4, column=1, padx=10, pady=5, sticky="ews")

        # -----------------------------------------------------------------------

        separator = ttk.Separator(settings_frame, orient="horizontal")
        separator.grid(row=6, column=0, padx=10, pady=40, sticky="ew", columnspan=2)

        ##################### Mode: Automatic Settings ############################################

        automatic_label = ttk.Label(
            settings_frame,
            text=" Mode: Automatic ",
            font=("Helvetica", 18, "bold"),
            style="Setting.Divider.Label",
        )
        automatic_label.grid(row=6, column=0, padx=10, pady=10)

        target_netfollowers_label = ttk.Label(
            settings_frame,
            text="Target Net-Followers",
            font=("Helvetica", 17, "bold"),
            style="Setting.Header.Label",
            wraplength=200,
        )
        target_netfollowers_label.grid(row=7, column=0, padx=10, pady=10)

        target_netfollowers_desc = ttk.Label(
            settings_frame,
            text="The bot should continue to run until this many are amassed. (Note: could take days).",
            font=("Helvetica", 12),
            wraplength=200,
        )
        target_netfollowers_desc.grid(row=8, column=0, padx=10, pady=1)

        # --------------------SLIDER---------------------------------------------------

        self.net_followers_slider = customtkinter.CTkSlider(
            settings_frame, from_=0, to=1, number_of_steps=4
        )
        self.net_followers_slider.grid(
            row=7, column=1, padx=(20, 10), pady=(15, 10), sticky="e", rowspan=2
        )

        # -----------------------------------------------------------------------

        separator = ttk.Separator(settings_frame, orient="horizontal")
        separator.grid(row=9, column=0, padx=10, pady=20, sticky="ew", columnspan=2)

        unfollow_after_label = ttk.Label(
            settings_frame,
            text="Begin Unfollowing After",
            font=("Helvetica", 17, "bold"),
            style="Setting.Header.Label",
            wraplength=200,
        )
        unfollow_after_label.grid(row=10, column=0, padx=10, pady=10)

        unfollow_after_desc = ttk.Label(
            settings_frame,
            text="After this time, the bot will switch to unfollowing those accounts which haven’t followed back",
            font=("Helvetica", 12),
            wraplength=200,
        )
        unfollow_after_desc.grid(row=11, column=0, padx=10, pady=1)

        # --------------------SLIDER---------------------------------------------------

        self.unfollow_after_slider = customtkinter.CTkSlider(
            settings_frame, from_=0, to=1, number_of_steps=4
        )
        self.unfollow_after_slider.grid(
            row=10, column=1, padx=(20, 10), pady=(20, 10), sticky="ew", rowspan=2
        )

        # -----------------------------------------------------------------------

        separator = ttk.Separator(settings_frame, orient="horizontal")
        separator.grid(row=12, column=0, padx=10, pady=40, sticky="ew", columnspan=2)

        ###################### Mode: Follow-Only##########################################

        follow_only_label = ttk.Label(
            settings_frame,
            text=" Mode: Follow-Only ",
            font=("Helvetica", 18, "bold"),
            style="Setting.Divider.Label",
        )
        follow_only_label.grid(row=12, column=0, padx=10, pady=10)

        # Target Following
        target_following_label = ttk.Label(
            settings_frame,
            text="Target Following",
            font=("Helvetica", 17, "bold"),
            style="Setting.Header.Label",
            wraplength=200,
        )
        target_following_label.grid(row=13, column=0, padx=10, pady=10)

        target_following_desc = ttk.Label(
            settings_frame,
            text="The bot should continue to run until this many are amassed. (Note: could take days).",
            font=("Helvetica", 12),
            wraplength=200,
        )
        target_following_desc.grid(row=14, column=0, padx=10, pady=1)

        # -------------------------SLIDER---------------------------------------------

        self.target_following_slider = customtkinter.CTkSlider(
            settings_frame, from_=0, to=1, number_of_steps=4
        )
        self.target_following_slider.grid(
            row=13, column=1, padx=(20, 10), pady=(20, 10), sticky="ew", rowspan=2
        )

        # -----------------------------------------------------------------------

        separator = ttk.Separator(settings_frame, orient="horizontal")
        separator.grid(row=15, column=0, padx=10, pady=40, sticky="ew", columnspan=2)

        ####################### Mode: Unfollow-Only #########################################

        unfollow_only_label = ttk.Label(
            settings_frame,
            text=" Mode: Unfollow-Only ",
            font=("Helvetica", 18, "bold"),
            style="Setting.Divider.Label",
        )
        unfollow_only_label.grid(row=15, column=0, padx=10, pady=10)

        # Target Unfollowing
        target_unfollowing_label = ttk.Label(
            settings_frame,
            text="Target Unfollowing",
            font=("Helvetica", 17, "bold"),
            style="Setting.Header.Label",
        )
        target_unfollowing_label.grid(row=16, column=0, padx=10, pady=10)

        target_unfollowing_desc = ttk.Label(
            settings_frame,
            text="The bot should continue to run until this many are amassed. (Note: could take days).",
            font=("Helvetica", 12),
            wraplength=200,
        )
        target_unfollowing_desc.grid(row=17, column=0, padx=10, pady=1)

        # -------------------------SLIDER---------------------------------------------

        self.target_following_slider = customtkinter.CTkSlider(
            settings_frame, from_=0, to=1, number_of_steps=4
        )
        self.target_following_slider.grid(
            row=16, column=1, padx=(20, 10), pady=(20, 10), sticky="ew", rowspan=2
        )

        # -----------------------------------------------------------------------

    def save_settings_btn(self):
        save_settings_btn = customtkinter.CTkButton(
            self, text="Save & Return", command=self.save_and_goto_landing
        )
        save_settings_btn.grid(row=3, column=0, padx=10, pady=20)

    def open_settings(self):
        # Replace this method with the actual logic to open the settings page
        print("Opening Settings Page")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog"
        )
        print("CTkInputDialog:", dialog.get_input())

    def save_and_goto_landing(self):
        # Hide current page and show the first page
        self.controller.settings.pack_forget()
        self.controller.landing.show()

    def show(self):
        # Show this page
        self.pack()
