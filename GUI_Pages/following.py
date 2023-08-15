import tkinter as tk
from tkinter import font, ttk
import customtkinter

from login import Login

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class Following(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Styling
        self.style = ttk.Style()
        self.style.configure(
            "headerStyle.TFrame", foreground="white", background="gray"
        )

        self.style.configure("headerStyle.Label", foreground="white", background="gray")

        self.rowconfigure(1, minsize=460, weight=1)
        self.columnconfigure(0, minsize=500, weight=1)

        # set up the data display for the landing page
        self.init_follow_accounts_display()

    def init_follow_accounts_display(self):
        unfollow_accounts_frame = ttk.Frame(self)
        unfollow_accounts_frame.grid(row=1, column=0, pady=0, sticky="nsew")
        unfollow_accounts_frame.columnconfigure(0, minsize=500)

        # Displays the type of mode (e.g. automatic, follow, unfollow)
        mode_display_label = ttk.Label(
            unfollow_accounts_frame,
            text="Mode: Follow-Only",
            font=("Helvetica", 15, "italic"),
        )
        mode_display_label.grid(row=0, column=0, padx=10, pady=(30, 5))

        # Displays the current action (e.g. Following accounts)
        action_display_label = ttk.Label(
            unfollow_accounts_frame,
            text="Following Accounts...",
            font=("Helvetica", 30, "bold"),
        )
        action_display_label.grid(row=1, column=0, padx=10, pady=10)

        self.progressbar_1 = customtkinter.CTkProgressBar(unfollow_accounts_frame)
        self.progressbar_1.grid(row=2, column=0, padx=10, pady=10)

        # Displays stats related to current action (e.g. total followed, net followers, time elapsed)
        total_followed_label = ttk.Label(
            unfollow_accounts_frame,
            text="Total Followed: 1000",
            font=("Helvetica", 15),
        )
        total_followed_label.grid(row=3, column=0, padx=10, pady=(40, 20))

        time_elapsed_label = ttk.Label(
            unfollow_accounts_frame,
            text="Time Elapsed: 1000",
            font=("Helvetica", 15),
        )
        time_elapsed_label.grid(row=4, column=0, padx=10, pady=10)

        # set up the button to commence the action (following, unfollowing) process
        self.init_stop_btn(unfollow_accounts_frame)

    def init_stop_btn(self, frame):
        stop_btn = customtkinter.CTkButton(
            frame, text="Stop", command=self.goto_Finished
        )
        stop_btn.grid(row=5, column=0, padx=10, pady=40)

    def open_settings(self):
        # Replace this method with the actual logic to open the settings page
        print("Opening Settings Page")

    def goto_Finished(self):
        # Hide current page and show the first page
        self.controller.following.pack_forget()
        self.controller.finished.show()

    def show(self):
        # Show this page
        self.pack()
