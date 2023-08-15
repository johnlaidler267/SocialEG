import tkinter as tk
from tkinter import font, ttk
from header import Header

import customtkinter


class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Create variables to hold input text
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.celebrity_username = tk.StringVar()

        Header(parent, controller).show()

        # Create a custom font with italic style
        italic_font = font.Font(family="Helvetica", size=15, slant="italic")

        # == Title and author labels ==================================================

        # Creates the login page title ("Instagram Engagement Bot")
        title_label = tk.Label(
            self, text="Instagram Engagement Bot", font=("Helvetica", 20, "bold")
        )
        title_label.pack(pady=(55, 0))

        # Creates the author label ("by John Laidler")
        author_label = tk.Label(self, text="by John Laidler", font=italic_font)
        author_label.pack(pady=(0, 5))

        # == Input fields ======================================================
        username_label = tk.Label(self, text="IG Username:", font=("Helvetica", 15))
        username_label.pack(pady=(50, 0))

        username_entry = customtkinter.CTkEntry(
            self, textvariable=self.username, width=200
        )
        username_entry.pack(pady=10)

        password_label = tk.Label(self, text="IG Password:", font=("Helvetica", 15))
        password_label.pack()

        password_entry = customtkinter.CTkEntry(
            self, show="*", textvariable=self.password, width=200
        )
        password_entry.pack(pady=10)

        # == Buttons ===========================================================

        # Submit button
        submit_button = customtkinter.CTkButton(
            self, text="Log In", font=("Helvetica", 15), command=self.submit
        )
        submit_button.pack(pady=20)

    def submit(self):
        # Retrieve the input values from the variables
        USERNAME = self.username.get()
        PASSWORD = self.password.get()
        CELEB_ACCOUNT = self.celebrity_username.get()

        # Goes to the landing page
        self.goto_Landing()

    def goto_Landing(self):
        # Hide current page and show the second page
        self.controller.login.pack_forget()
        self.controller.landing.show()

    def show(self):
        # Show this page
        self.pack()
