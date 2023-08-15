import tkinter as tk
from tkinter import font, ttk
import customtkinter

from login import Login

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


class SelectMode(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # set up the select mode form to select the bots mode (follow, unfollow, automatic)
        self.initialize_select_form()

    def initialize_select_form(self):

        # == Initialize Select Mode Form Frame ==============================================================

        select_form = customtkinter.CTkFrame(self)
        select_form.grid(row=0, column=0, padx=0, pady=0)
        select_form.grid_columnconfigure(0, minsize=500)
        select_form.grid_rowconfigure(0, minsize=100)
        select_form.grid_rowconfigure((1, 3), minsize=75)
        select_form.grid_rowconfigure(5, minsize=70)

        # Select Mode Label
        select_mode_label = ttk.Label(
            select_form, text="Select Mode", font=("Helvetica", 30, "bold")
        )
        select_mode_label.grid(row=0, column=0, padx=0, pady=(30, 0))

        # = Select Mode Checkbox Buttons =================================================================

        def set_mode(mode):
            # Depending on which action button is selected, set redirect_func to the approporiate page
            redirect_func = ""
            if mode == "follow":
                redirect_func = self.goto_Following
                unfollow_checkbox.deselect()
                automatic_checkbox.deselect()
            elif mode == "unfollow":
                redirect_func = self.goto_Unfollowing
                follow_checkbox.deselect()
                automatic_checkbox.deselect()
            else:
                redirect_func = self.goto_AutomaticFollowing
                follow_checkbox.deselect()
                unfollow_checkbox.deselect()

            # configure the button to redirect to the appropriate page
            begin_bot_btn.configure(command=redirect_func)

        # Selects the follow-only mode
        follow_checkbox = customtkinter.CTkCheckBox(
            master=select_form,
            text="Follow",
            command=lambda: set_mode("follow"),
            font=("Helvetica", 20),
        )
        follow_checkbox.grid(row=1, column=0, padx=10, pady=10)

        # Selects the unfollow-only mode
        unfollow_checkbox = customtkinter.CTkCheckBox(
            master=select_form,
            text="Unfollow",
            command=lambda: set_mode("unfollow"),
            font=("Helvetica", 20),
        )
        unfollow_checkbox.grid(row=2, column=0, padx=10, pady=10)

        # Selects the automatic mode
        automatic_checkbox = customtkinter.CTkCheckBox(
            master=select_form,
            text="Automatic",
            command=lambda: set_mode("automatic"),
            font=("Helvetica", 20),
        )
        automatic_checkbox.grid(row=3, column=0, padx=10, pady=10)

        separator = ttk.Separator(select_form, orient="horizontal")
        separator.grid(row=4, column=0, padx=0, pady=30, sticky="ew", columnspan=2)

        # = Place Begin Bot Btn ===============================================================

        # Initializes the 'Begin Bot' button for the selected mode
        begin_bot_btn = customtkinter.CTkButton(
            select_form,
            text="Begin Bot",
            font=("Helvetica", 20),
        )
        begin_bot_btn.grid(row=5, column=0, padx=10, pady=(0, 30))

    def goto_Following(self):
        self.controller.select_mode.pack_forget()
        self.controller.following.show()

    def goto_Unfollowing(self):
        self.controller.select_mode.pack_forget()
        self.controller.unfollowing.show()

    def goto_AutomaticFollowing(self):
        self.controller.select_mode.pack_forget()
        self.controller.automatic_following.show()

    def show(self):
        # Show this page
        self.pack()
