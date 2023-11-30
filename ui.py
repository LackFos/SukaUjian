import customtkinter as tk
import tkinter
from Dosen import *
import datetime
import os

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

app=tk.CTk()
app.geometry("600x600")

def refresh():
    app.destroy()
    os.system('C:/Users/asus/AppData/Local/Programs/Python/Python310/python.exe c:/Users/asus/Documents/GitHub/SukaUjian/ui.py')

tabView = tk.CTkTabview(app)
tabView.configure(width=500)
tabView.pack(padx=0, pady=0)

tabView.add("Tambah Jadwal")
tabView.add("Update Jadwal")
tabView.add("Delete Jadwal")

def BuatJadwal():
    dosen.ExamSchedule(TambahTime.get(),TambahDate.get())
    refresh()

def UpdateJadwal():
    dosen.ExamSchedule(Updateid.get(),UpdateTime.get(),UpdateDate.get())
    refresh()

def DeleteJadwal():
    dosen.DeleteExam(Deleteid.get())
    refresh()


#Tab Tambah Jadwal
TambahTime = tk.CTkEntry(tabView.tab("Tambah Jadwal"), placeholder_text="Masukan Waktu ujian(HH:MM-HH:MM)")
TambahTime.pack(padx=0, pady=0)
TambahTime.configure(width=300)
TambahDate = tk.CTkEntry(tabView.tab("Tambah Jadwal"), placeholder_text="Masukan tanggal ujian(YYYY-MM-DD)")
TambahDate.pack(padx=0, pady=0)
TambahDate.configure(width=300)
Tambahsumbit=tk.CTkButton(tabView.tab("Tambah Jadwal"), text="Sumbit", command=BuatJadwal)
Tambahsumbit.pack(padx=0, pady=0)

#Tab Update Jadwal
Updateid = tk.CTkEntry(tabView.tab("Update Jadwal"), placeholder_text="Masukan id")
Updateid.pack(padx=0, pady=0)
Updateid.configure(width=300)
UpdateTime = tk.CTkEntry(tabView.tab("Update Jadwal"), placeholder_text="Masukan Waktu (HH:MM-HH:MM)")
UpdateTime.pack(padx=0, pady=0)
UpdateTime.configure(width=300)
UpdateDate = tk.CTkEntry(tabView.tab("Update Jadwal"), placeholder_text="Masukan tanggal (YYYY-MM-DD)")
UpdateDate.pack(padx=0, pady=0)
UpdateDate.configure(width=300)
Updatesumbit=tk.CTkButton(tabView.tab("Update Jadwal"), text="Sumbit", command=UpdateJadwal)
Updatesumbit.pack(padx=0, pady=0)

#Tab Delete Jadwal
Deleteid = tk.CTkEntry(tabView.tab("Delete Jadwal"), placeholder_text="Masukan id")
Deleteid.pack(padx=0, pady=0)
Deleteid.configure(width=300)
Deletesumbit=tk.CTkButton(tabView.tab("Delete Jadwal"), text="Sumbit", command=DeleteJadwal)
Deletesumbit.pack(padx=0, pady=0)

text1=tk.CTkTextbox(app)
text1.configure(width=500)
text1.pack(padx = 0, pady =0)
dosen=Jadwal(1)
text=dosen.DisplayExam()

text1.insert("0.0",text)

app.mainloop()