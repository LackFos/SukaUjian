from customtkinter import *
import customtkinter as tk
from NavigasiJadwal.BuatJadwal import BuatJadwal
from NavigasiJadwal.HapusJadwal import HapusJadwal
from NavigasiJadwal.UpdateJadwal import UpdateJadwal
from NavigasiJadwal.LihatJadwal import LihatJadwal

class JadwalPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0)

        t1 = CTkButton(self, text="Buat Jadwal", command=lambda: self.navigateTo("BuatJadwal"))
        t1.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t1.grid(row=1, column=0, padx=16, pady=(16,0), sticky="ew")

        t2 = CTkButton(self, text="Lihat Jadwal", command=lambda: self.navigateTo("LihatJadwal"))
        t2.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t2.grid(row=2, column=0, padx=16, pady=(16,0), sticky="ew")

        t3 = CTkButton(self, text="Update Jadwal", command=lambda: self.navigateTo("UpdateJadwal"))
        t3.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t3.grid(row=3, column=0, padx=16, pady=(16,0), sticky="ew")

        t4 = CTkButton(self, text="Hapus Jadwal", command=lambda: self.navigateTo("HapusJadwal"))
        t4.configure(height=48, font=("Poppins", 16, "bold"), anchor="w")
        t4.grid(row=4, column=0, padx=16, pady=(16,0), sticky="ew")


        
        self.pages = {
            "Buat Jadwal": BuatJadwal(self),
            "Lihat Jadwal": LihatJadwal(self),
            "Update Jadwal": UpdateJadwal(self),
            "Hapus Jadwal": HapusJadwal(self),
        }

    def navigateTo(self, selectedPage):
        self.pages[selectedPage].grid(column=0, row=0, sticky="NSWE")

        for key, page in self.pages.items():
            page.grid(row=0, column=0) if key == selectedPage else page.grid_forget()



        # button = CTkButton(self, text="Buat Jadwal",)
        # button.grid(row=0, column=0, padx=24, pady=(24,16))

        # button = CTkButton(self, text="Tampilkan Jadwal",)
        # button.grid(row=1, column=0, padx=24, pady=(24,16))

        # button = CTkButton(self, text="Update Jadwal",)
        # button.grid(row=2, column=0, padx=24, pady=(24,16))

        # button = CTkButton(self, text="Delete Jadwal",)
        # button.grid(row=3, column=0, padx=24, pady=(24,16))



