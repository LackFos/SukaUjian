from Database.Connect import Connect
import os
import mysql.connector
from dotenv import load_dotenv
from Database.Error import DatabaseErrorException

load_dotenv()

class Kelas:
    def __init__(self):
        self.__nomor = ""
        self.__capacity = 0
        self.__occupied = ""

    def insert_kelas(self):
        self.__nomor = input("Masukkan Nomer Kelas: ")
        while True:
            try:
                self.__capacity = int(input("Masukkan Kapasiti Kelas (20-60): "))
                if 20 <= self.__capacity <= 60:
                    break
                else:
                    print("Kapasiti harus antara 20 dan 60.")
            except ValueError:
                print("Masukkan nomer antara 20 dan 60.")

        while True:
            self.__occupied = input("Adakah Kelas ini sudah dipakai? (True/False): ")
            if self.__occupied.lower() in ["true", "false"]:
                break
            else:
                print("Masukkan 'True' atau 'False'.")

        db = Connect()
        data = {
            "NomerKelas": self.__nomor,
            "Capacity": self.__capacity,
            "Occupied": self.__occupied
        }
        db.insert("kelas", data)

    def update_kelas(self):
        self.__nomor = input("Masukkan Nomer Kelas yang ingin diperbarui: ")

        db = Connect()
        criteria = {"NomerKelas": self.__nomor}
        existing_data = db.get("kelas", criteria)

        if not existing_data:
            print("Nomer Kelas tidak ditemukan dalam database.")
            return

        existing_data = existing_data[0]  # Assuming it's a list, and we take the first item

        new_nomor = input("Masukkan Nomer Kelas Baru: ")
        while True:
            try:
                new_capacity = int(input("Masukkan Kapasiti Kelas Baru (20-60): "))
                if 20 <= new_capacity <= 60:
                    break
                else:
                    print("Kapasiti harus antara 20 dan 60.")
            except ValueError:
                print("Masukkan nomer antara 20 dan 60.")

        while True:
            new_occupied = input("Adakah Kelas ini sudah dipakai yang baru? (True/False): ")
            if new_occupied.lower() in ["true", "false"]:
                break
            else:
                print("Masukkan 'True' atau 'False'.")

        criteria = {"NomerKelas": self.__nomor}
        new_data = {
            "NomerKelas": new_nomor,
            "Capacity": new_capacity,
            "Occupied": new_occupied
        }
        db.update("kelas", criteria, new_data)

    def delete_kelas(self):
        self.__nomor = input("Masukkan Nomer Kelas yang ingin dihapus: ")

        db = Connect()
        criteria = {"NomerKelas": self.__nomor}
        existing_data = db.get("kelas", criteria)

        if not existing_data:
            print("Nomer Kelas tidak ditemukan dalam database.")
            return

        criteria = {"NomerKelas": self.__nomor}
        db.delete("kelas", criteria)

    def select_kelas(self):
        db = Connect()
        result = db.select("kelas")
        return result

# Create a Kelas object
kelas = Kelas()

print("Sila Pilih Operasi:")
print("1. Masukkan Kelas (Insert)")
print("2. Membarui Kelas (Update)")
print("3. Hapus Kelas (Delete)")
print("4. Pilih Kelas (Select)")
operation = int(input("Sila Pilih Nomer Operasi: "))

if operation == 1:
    kelas.insert_kelas()
elif operation == 2:
    kelas.update_kelas()
elif operation == 3:
    kelas.delete_kelas()
elif operation == 4:
    result = kelas.select_kelas()
    print(result)
else:
    print("Tiada Nomer Operasi.")
