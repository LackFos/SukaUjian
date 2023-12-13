from Database.Connect import Connect
from Database.Error import DatabaseErrorException
from abc import ABC, abstractmethod

class BaseDatabaseOperation(ABC):
    def __init__(self, table_name):
        self.db = Connect()
        self.table_name = table_name

    @abstractmethod
    def perform_operation(self):
        pass

class InsertOperation(BaseDatabaseOperation):
    def perform_operation(self, data):
        self.db.insert(self.table_name, data)

class UpdateOperation(BaseDatabaseOperation):
    def perform_operation(self, criteria, new_data):
        existing_data = self.db.get(self.table_name, criteria)

        if not existing_data:
            print(f"{self.table_name} not found in the database.")
            return

        criteria = criteria
        self.db.update(self.table_name, criteria, new_data)

class DeleteOperation(BaseDatabaseOperation):
    def perform_operation(self, criteria):
        existing_data = self.db.get(self.table_name, criteria)

        if not existing_data:
            print(f"{self.table_name} not found in the database.")
            return

        self.db.delete(self.table_name, criteria)
        print("Data berhasil dihapus")

class Kelas(BaseDatabaseOperation):
    def __init__(self):
        super().__init__("kelas")
        self.__nomor = ""
        self.__capacity = 0
        self.__occupied = ""
        self.quit_menu = False  # Flag to determine if the user wants to quit
    

    def perform_operation(self):
        while not self.quit_menu:
            print("Sila Pilih Operasi:")
            print("1. Masukkan Kelas (Insert)")
            print("2. Membarui Kelas (Update)")
            print("3. Hapus Kelas (Delete)")
            print("4. Pilih Kelas (Select)")
            print("5. Quit")

            operation = input("Sila Pilih Nomer Operasi: ")

            if operation == "1":
                self.insert_operation()
            elif operation == "2":
                self.update_operation()
            elif operation == "3":
                self.delete_operation()
            elif operation == "4":
                self.select_operation()
            elif operation == "5":
                self.quit_menu = True
            else:
                print("Tiada Nomer Operasi yang sah.")

    def insert_operation(self):
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
                print("Masukkan True atau False.")

        db = Connect()
        data = {
            "NomerKelas": self.__nomor,
            "Capacity": self.__capacity,
            "Occupied": self.__occupied
        }
        db.insert("kelas", data)

    def update_operation(self):
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

    def delete_operation(self):
        self.__nomor = input("Masukkan Nomer Kelas yang ingin dihapus: ")
        db = Connect()
        criteria = {"NomerKelas": self.__nomor}
        existing_data = db.get("kelas", criteria)

        if not existing_data:
            print("Nomer Kelas tidak ditemukan dalam database.")
            return

        criteria = {"NomerKelas": self.__nomor}
        db.delete("kelas", criteria)
        print("Data berhasil dihapus")

    def select_operation(self):
        db = Connect()
        result = db.select("kelas")
        print(result)

kelas = Kelas()
kelas.perform_operation()

