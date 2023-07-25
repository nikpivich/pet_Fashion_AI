# Python program to create a basic GUI
# application using the customtkinter module

import customtkinter as ctk
import tkinter as tk
from PIL import Image

from ai_gen import ai_get, download_picture, insert_image

# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("Dark")

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")

appWidth, appHeight = 1200, 680


# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")

        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                      text="Prompt")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                                      placeholder_text="Teja")
        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200,
                                         height=100)
        self.displayBox.grid(row=0, column=1, columnspan=4,
                             padx=20, pady=20, sticky="nsew")

        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                        text="Gender")
        self.genderLabel.grid(row=2, column=0,
                              padx=20, pady=20,
                              sticky="ew")
        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="Prefer\
                                                 not to say")

        self.maleRadioButton = ctk.CTkRadioButton(self,
                                                  text="Male",
                                                  variable=self.genderVar,
                                                  value="He is")
        self.maleRadioButton.grid(row=2, column=1, padx=20,
                                  pady=20, sticky="ew")

        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                                    text="Female",
                                                    variable=self.genderVar,
                                                    value="She is")
        self.femaleRadioButton.grid(row=2, column=2,
                                    padx=20,
                                    pady=20, sticky="ew")

        self.noneRadioButton = ctk.CTkRadioButton(self,
                                                  text="Prefer not to say",
                                                  variable=self.genderVar,
                                                  value="They are")
        self.noneRadioButton.grid(row=2, column=3,
                                  padx=20, pady=20,
                                  sticky="ew")

        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self,
                                            text="Color")
        self.occupationLabel.grid(row=4, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")

        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self,
                                                      values=["White",
                                                              "Black",
                                                              "Green",
                                                              "Olive",
                                                              "Sand",
                                                              "Purple"])
        self.occupationOptionMenu.grid(row=4, column=1,
                                       padx=20, pady=20,
                                       columnspan=6, sticky="ew")

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text="Generate Results",
                                                   command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")

        your_image = ctk.CTkImage(light_image=Image.open("./pictures/final.png"),
                                  size=(400, 400))
        label = ctk.CTkLabel(self, image=your_image, text='')
        label.grid(row=0, column=500)

    def generateResults(self):
        url = ai_get(self.displayBox.get("1.0", "2.0"))
        download_picture(url, "./pictures/print2.png")
        insert_image("./pictures/print2.png", f"./pictures/shirts/black_t-shirt.png",
                     ((300, 300), (355, 350)), "./pictures/final2.png")

        your_image = ctk.CTkImage(light_image=Image.open("./pictures/final2.png"),
                                  size=(400, 400))
        label = ctk.CTkLabel(self, image=your_image, text='')
        label.grid(row=0, column=500)


if __name__ == "__main__":
    app = App()
    app.mainloop()
