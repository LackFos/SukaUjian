from customtkinter import *

class JadwalPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0)

        button = CTkButton(self, text="jadwal")
        button.grid(row=0, column=0)