from tkinter import *
from tkinter.messagebox import showinfo

# Fungsi Operasi
def hitung_operasi():
    try:
        Bil1_VALL = float(Bil1.get())
        Bil2_VALL = float(Bil2.get())

        operasi = var_operasi.get()

        if operasi == "Penjumlahan":
            hasil = Bil1_VALL + Bil2_VALL
        elif operasi == "Pengurangan":
            hasil = Bil1_VALL - Bil2_VALL
        elif operasi == "Perkalian":
            hasil = Bil1_VALL * Bil2_VALL
        elif operasi == "Pembagian":
            if Bil2_VALL != 0:
                hasil = Bil1_VALL / Bil2_VALL
            else:
                hasil = "Error (Pembagian oleh 0)"
        else:
            hasil = "Pilih operasi"

        label_hasil.config(text="Hasil: " + str(hasil))

    except ValueError:
        label_hasil.config(text="Masukkan bilangan yang valid")

# Membuat window
windowUtama = Tk()
windowUtama.title("Kalkulator")
windowUtama.geometry("450x350+550+100")

# Membuat entry
label_bil1 = Label(windowUtama, text="Bilangan 1:")
label_bil1.pack(pady=(50, 0))
Bil1 = Entry(windowUtama)
Bil1.pack(pady=(0, 10))

label_bil2 = Label(windowUtama, text="Bilangan 2:")
label_bil2.pack(pady=(10, 0))
Bil2 = Entry(windowUtama)
Bil2.pack(pady=(0, 10))

# Membuat Pilihan Operasi
label_operasi = Label(windowUtama, text="Pilih Operasi:")
label_operasi.pack()
var_operasi = StringVar()
var_operasi.set("Penjumlahan")
operasi_menu = OptionMenu(windowUtama, var_operasi, "Penjumlahan", "Pengurangan", "Perkalian", "Pembagian")
operasi_menu.pack(pady=(0, 10))

# Membuat button
tombol1 = Button(windowUtama, text='Submit', command=hitung_operasi)
tombol1.pack()

label_hasil = Label(windowUtama, text="Hasil: ")
label_hasil.pack()

windowUtama.mainloop()