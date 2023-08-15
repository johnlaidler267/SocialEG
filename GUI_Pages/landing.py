import tkinter as tk
from tkinter import font, ttk
import customtkinter

from login import Login


class Landing(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Set up the data display for the landing page
        self.initialize_data_display_frame()

    def initialize_data_display_frame(self):

        # Custom fonts for the data frame
        header_font = ("Helvetica", 16, "bold")
        data_font = ("Helvetica", 13)

        # Initialize the data frame (that holds all the account data to be displayed)
        data_frame = customtkinter.CTkFrame(self, width=500, corner_radius=0)
        data_frame.grid(row=1, column=0, padx=0, pady=0)

        # FUNCTIONS ==========================================================================================

        # Initializes the frame for follower stats (followers, followed, unfollowed, non-followers)
        def init_follower_stats_frame():

            # ====================================================================================================

            # Set up follower frame
            follower_frame = customtkinter.CTkFrame(data_frame)
            follower_frame.grid(row=0, column=0, padx=0, pady=0)

            follower_frame.grid_columnconfigure(1, minsize=300)
            follower_frame.grid_columnconfigure(0, minsize=200)

            # ====================================================================================================

            # Header for the follower stats
            follower_header = customtkinter.CTkLabel(
                follower_frame, text="Follower Stats", font=header_font
            )
            follower_header.grid(row=0, column=0, padx=10, pady=5)

            # ====================================================================================================

            # Data for the follower stats
            follower_data_labels = [
                "Net Followers:",
                "Followed:",
                "Unfollowed:",
                "Non-Followers:",
            ]

            follower_data_values = ["1000", "500", "100", "400"]

            row = 1
            for label, value in zip(follower_data_labels, follower_data_values):
                label_value_frame = customtkinter.CTkFrame(follower_frame)
                label_value_frame.grid(row=row, column=0, padx=10, pady=2)

                customtkinter.CTkLabel(
                    label_value_frame, text=label, font=data_font, width=12, anchor="w"
                ).grid(row=row, column=0, padx=2, pady=2)
                customtkinter.CTkLabel(
                    label_value_frame, text=value, font=data_font, width=5, anchor="e"
                ).grid(row=row, column=1, padx=2, pady=2)

                row += 1

            # ====================================================================================================

            # Canvas for the graph displaying follower stats
            follower_graph_canvas = tk.Canvas(follower_frame, width=250, height=150)
            follower_graph_canvas.grid(row=0, column=1, padx=10, pady=10, rowspan=10)


        # Initializes the engagement stats frame (Likes, Comments, Shares on recent photo)
        def init_engagement_stats_frame():

            # ====================================================================================================

            # Set up engagement stats frame
            engagement_frame = customtkinter.CTkFrame(data_frame)

            engagement_frame.grid(row=1, column=0, padx=0, pady=0)

            engagement_frame.grid_columnconfigure(1, minsize=300)
            engagement_frame.grid_columnconfigure(0, minsize=200)

            # ====================================================================================================

            # Header for the engagement stats frame
            engagement_header = customtkinter.CTkLabel(
                engagement_frame, text="Engagement", font=header_font
            )

            engagement_header.grid(row=0, column=0, padx=10, pady=(20,0))

            # ====================================================================================================

            # Data for the engagement stats
            engagement_data_labels = ["Likes:", "Comments:", "Shares:"]
            engagement_data_values = ["200", "50", "30"]

            # Dynamically generates the grid of labeled statistics to present data,
            # with each statistic's label left-aligned and value right-aligned.
            row = 1
            for label, value in zip(engagement_data_labels, engagement_data_values):
                label_value_frame = customtkinter.CTkFrame(engagement_frame)
                label_value_frame.grid(row=row + 1, column=0, padx=1, pady=1)

                customtkinter.CTkLabel(
                    label_value_frame, text=label, font=data_font, width=8, anchor="w"
                ).grid(row=row, column=0, padx=1, pady=1)
                customtkinter.CTkLabel(
                    label_value_frame, text=value, font=data_font, width=5, anchor="e"
                ).grid(row=row, column=1, padx=5, pady=2)

                row += 1

            # ====================================================================================================

            # Canvas for the graph of post engagement
            engagement_graph_canvas = tk.Canvas(engagement_frame, width=250, height=150)

            engagement_graph_canvas.grid(row=0, column=1, padx=10,  pady=(20,10), rowspan=10)

            # Creates the graph for post engagement

        # ====================================================================================================

        # function that sets up the action stats frame set up the follower stats frame
        init_follower_stats_frame()

        # set up the engagement stats frame
        init_engagement_stats_frame()

        # Set up the button to commence the bot's action: (e.g. following, unfollowing)
        self.initialize_action_button(data_frame)

    def create_rectangle(self, canvas, x1, y1, x2, y2):
        return canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")

    def initialize_action_button(self, frame):
        action_button = customtkinter.CTkButton(
            frame, text="Begin Bot", command=self.goto_select_mode
        )
        action_button.grid(row=2, column=0, padx=10, pady=15)

    def open_settings(self):
        # Replace this method with the actual logic to open the settings page
        print("Opening Settings Page")

    def goto_select_mode(self):
        # Hide current page and show the first page
        self.controller.landing.pack_forget()
        self.controller.select_mode.show()

    def show(self):
        # Show this page
        self.pack()
