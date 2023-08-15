import tkinter as tk
from tkinter import ttk
import customtkinter


class Header(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Header Frame
        header_frame = customtkinter.CTkFrame(self, fg_color="gray")
        header_frame.grid(row=0, column=0, pady=0, sticky="nsew")

        header_frame.columnconfigure(0, minsize="50")
        header_frame.columnconfigure(1, minsize="210")
        header_frame.columnconfigure(2, minsize="50")
        header_frame.columnconfigure(3, minsize="190")
        header_frame.rowconfigure(0, minsize="30")

        # =================================================================

        # Profile Picture, Name, and Username
        # Replace with your image file
        profile_image = tk.PhotoImage(file="")
        profile_label = ttk.Label(header_frame, image=profile_image)
        profile_label.image = profile_image
        profile_label.grid(row=0, column=0, padx=0, pady=0, rowspan=2)

        # =======================================================================

        name_label = customtkinter.CTkLabel(
            header_frame,
            text="John Doe",
            font=("Helvetica", 20, "bold"),
            text_color="white",
        )
        name_label.grid(row=0, column=1, pady=(10, 0))

        username_label = customtkinter.CTkLabel(
            header_frame,
            text="@johndoe",
            font=("Helvetica", 12),
            text_color="white",
        )
        username_label.grid(row=1, column=1, pady=(0, 10))

        # Followers and Following
        followers_label = customtkinter.CTkLabel(
            header_frame,
            text="Followers: 1000",
            font=("Helvetica", 12),
            text_color="white",
        )
        followers_label.grid(row=0, column=2, pady=(10, 0))

        following_label = customtkinter.CTkLabel(
            header_frame,
            text="Following: 500",
            font=("Helvetica", 12),
            text_color="white",
        )
        following_label.grid(row=1, column=2, pady=(0, 10))

        # =======================================================================

        # Settings Button

        settings_button = customtkinter.CTkButton(
            master=header_frame,
            text="⚙️",
            command=self.goto_Settings,
            fg_color="white",
            border_width=1,
            width=15,
        )
        settings_button.grid(row=0, column=3, padx=(0, 10), pady=10, rowspan=2)

    def goto_Settings(self):
        # Hide current page and show the second page
        self.controller.landing.pack_forget()
        self.controller.select_mode.pack_forget()
        self.controller.login.pack_forget()
        self.controller.settings.show()

    def show(self):
        # Show this page
        self.pack()
