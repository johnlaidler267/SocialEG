import tkinter as tk
from tkinter import font, ttk
import customtkinter

from login import Login

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class Finished(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # set up the data display for the landing page
        self.init_follow_accounts_display()

    def init_follow_accounts_display(self):
        follow_accounts_frame = ttk.Frame(self)
        follow_accounts_frame.grid(row=1, column=0, padx=0, pady=0)
        follow_accounts_frame.columnconfigure(0, minsize=500)
        follow_accounts_frame.rowconfigure(3, minsize=350)

        # Displays the current action (e.g. Following accounts)
        action_display_label = ttk.Label(
            follow_accounts_frame,
            text="Job Completed.",
            font=("Helvetica", 35, "bold"),
        )
        action_display_label.grid(row=1, column=0, padx=10, pady=(110, 10))

        # Displays the current action (e.g. Following accounts)
        action_display_label = ttk.Label(
            follow_accounts_frame,
            text="The current job was terminated sucessfully. ",
            font=("Helvetica", 14, "italic"),
        )
        action_display_label.grid(row=2, column=0, padx=10, pady=10)

        return_to_homepage_btn = customtkinter.CTkButton(
            follow_accounts_frame, text="Return to Homepage", command=self.goto_Landing, font=("Helvetica", 20)
        )
        return_to_homepage_btn.grid(row=3, column=0, padx=10, pady=(10, 250))

    def open_settings(self):
        # Replace this method with the actual logic to open the settings page
        print("Opening Settings Page")

    def goto_Landing(self):
        # Hide current page and show the first page
        self.controller.finished.pack_forget()
        self.controller.landing.show()

    def show(self):
        # Show this page
        self.pack()
