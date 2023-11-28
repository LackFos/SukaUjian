from customtkinter import *
from ujian import UjianPage
from nilai import NilaiPage
from soal import SoalPage
from kelas import KelasPage
from jadwal import JadwalPage
from jawaban import JawabanPage
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

        l1 = CTkImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'ujianicon.png')), size=(24, 24))
        t1 = CTkButton(sidebar, image=l1, text="Ujian",  command=lambda: self.navigateTo("ujian"))
        t1.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t1.grid(row=1, column=0, padx=16, pady=(24, 0), sticky="ew")

        l2 = CTkImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'nilaiicon.png')), size=(24, 24))
        t2 = CTkButton(sidebar, image=l2, text="Nilai", command=lambda: self.navigateTo("nilai"))
        t2.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t2.grid(row=2, column=0, padx=16, pady=(16,0), sticky="ew")
    
        t3 = CTkButton(sidebar, text="Soal", command=lambda: self.navigateTo("soal"))
        t3.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t3.grid(row=3, column=0, padx=16, pady=(16,0), sticky="ew")

        t4 = CTkButton(sidebar, text="Kelas", command=lambda: self.navigateTo("kelas"))
        t4.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t4.grid(row=4, column=0, padx=16, pady=(16,0), sticky="ew")

        t5 = CTkButton(sidebar, text="Jadwal", command=lambda: self.navigateTo("jadwal"))
        t5.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t5.grid(row=5, column=0, padx=16, pady=(16,0), sticky="ew")

        t6 = CTkButton(sidebar, text="Jawaban", command=lambda: self.navigateTo("jawaban"))
        t6.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t6.grid(row=6, column=0, padx=16, pady=(16,0), sticky="ew")

        content = CTkFrame(self, fg_color='white', corner_radius=8)
        content.grid(row=0, column=1, sticky="nsew", pady=8, padx=8)
        
        self.pages = {
            "ujian": UjianPage(content),
            "nilai": NilaiPage(content),
            "kelas": KelasPage(content),
            "soal": SoalPage(content),
            "jadwal": JadwalPage(content),
            "jawaban": JawabanPage(content)
        }
        
        self.navigateTo("ujian")

    def navigateTo(self, selectedPage):
        self.pages[selectedPage].grid(column=0, row=0, sticky="NSWE")

        for key, page in self.pages.items():
            page.grid(row=0, column=0) if key == selectedPage else page.grid_forget()