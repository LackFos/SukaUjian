from customtkinter import *
from ujian import UjianPage
from nilai import NilaiPage
from PIL import Image, ImageTk

class HomePage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0)

        sidebar = CTkFrame(self, fg_color='white', corner_radius=8)
        sidebar.grid(row=0, column=0, sticky="ns", pady=8, padx=(8,0))
        
        logoImage = CTkImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo-text.png')), size=(160, 40))
        logo = CTkLabel(sidebar, image=logoImage, text="")
        logo.grid(row=0, column=0, padx=24, pady=(24,16))

        tombolUjianLogo = CTkImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'ujianicon.png')), size=(24, 24))
        tombolUjian = CTkButton(sidebar, image=tombolUjianLogo, text="Ujian",  command=lambda: self.navigateTo("ujian"))
        tombolUjian.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        tombolUjian.grid(row=1, column=0, padx=16, pady=(24, 0), sticky="ew")

        tombolNilaiLogo = CTkImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'nilaiicon.png')), size=(24, 24))
        tombolNilai = CTkButton(sidebar, image=tombolNilaiLogo, text="Nilai", command=lambda: self.navigateTo("nilai"))
        tombolNilai.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        tombolNilai.grid(row=2, column=0, padx=16, pady=(16), sticky="ew")
    
        content = CTkFrame(self, fg_color='white', corner_radius=8)
        content.grid(row=0, column=1, sticky="nsew", pady=8, padx=8)
        
        self.pages = {
            "ujian": UjianPage(content),
            "nilai": NilaiPage(content)
        }
        
        self.navigateTo("ujian")

    def navigateTo(self, selectedPage):
        self.pages[selectedPage].grid(column=0, row=0, sticky="NSWE")

        for key, page in self.pages.items():
            page.grid(row=0, column=0) if key == selectedPage else page.grid_forget()