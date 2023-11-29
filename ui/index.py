from customtkinter import *
from login import LoginPage
from home import HomePage

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("SukaUjian")
        self.geometry("800x400")
        self.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo.ico'))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = CTkFrame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky="NSWE")

        self.pages = {
            "login": LoginPage(container, lambda: self.navigateTo("home")),
            "home": HomePage(container)
        }
        self.navigateTo("login")

    def navigateTo(self, selectedPage):
        self.pages[selectedPage].grid(column=0, row=0, sticky="NSWE")

        for key, page in self.pages.items():
            page.grid(row=0, column=0) if key == selectedPage else page.grid_forget()

app = App()
app.mainloop()
