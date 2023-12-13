from customtkinter import *
from PIL import Image, ImageTk

class LoginPage(CTkFrame):
    def __init__(self, master, onLogin):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.grid(column=0, row=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = CTkFrame(self, fg_color='white')
        container.grid(row=0, column=0)
        
        logoImage =  CTkImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo-text.png')), size=(160, 40))
        logo = CTkLabel(container, image=logoImage, text="")
        logo.grid(row=0, column=0, padx=24, pady=(24,40))

        npm_input = CTkEntry(container, placeholder_text='NPM')
        npm_input.configure(height=40)
        npm_input.grid(row=1, column=0, padx=24, pady=(0,24), sticky="ew")

        password_input = CTkEntry(container, placeholder_text='Password')
        password_input.configure(height=40)
        password_input.grid(row=3, column=0, padx=24, pady=(0,40), sticky="ew")
        
        login_button = CTkButton(container, text="Login", command=onLogin)
        login_button.configure(width=320, height=48, font=("Poppins", 16, "bold"))
        login_button.grid(row=4, column=0, padx=24, pady=(0, 24) ,sticky="ew")
    
